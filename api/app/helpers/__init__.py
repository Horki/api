# Generic error function
def make_error(status_code, sub_code, message):
    response = {
        'code': sub_code,
        'message': message
    }
    response.status_code = status_code
    return response
