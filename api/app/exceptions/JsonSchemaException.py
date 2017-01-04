class JsonSchemaException(Exception):
    def __init__(self, messages):
        self.messages = messages

    def to_dict(self):
        return {
            'messages': self.messages
        }
