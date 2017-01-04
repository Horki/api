import os
import re
from flask import json, request
from jsonschema import Draft4Validator
from api.app.exceptions.JsonSchemaException import JsonSchemaException


def validate_json(app):
    uri = re.sub(r'/\d+', '/0', request.full_path)
    path = 'schemas%s/%s/request.schema.json' % (
        uri, request.method.lower())
    if not os.path.isfile(path):
        # schema doesn't exists, skip
        return None

    # load schema as <dict>
    schema = json.loads(open(os.path.abspath(path)).read())

    # load json schema validator
    v = Draft4Validator(schema)

    # append all errors to list
    errors = [
        error.message for error in sorted(
            v.iter_errors(
                request.data),
            key=str)]

    if len(errors):
        app.logger.error(errors)
        raise JsonSchemaException(errors)
