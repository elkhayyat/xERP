import traceback

from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    traceback.print_exc()
    return ErrorAPIResponse(message=exc.__str__(), error_type=type(exc).__name__)


class APIResponse(Response):
    def __init__(self, status, message='', error_type=None, data=None, pagination=None):
        response_data = {
            'status': status,
            'message': message,
        }
        if data is not None:
            response_data['data'] = data
        if pagination is not None:
            response_data['pagination'] = pagination
        if status == 'error':
            response_data['error_type'] = error_type
        super().__init__(response_data)


class SuccessAPIResponse(APIResponse):
    def __init__(self, message=None, data=None, pagination=None):
        super().__init__(status='success', message=message, data=data, pagination=pagination)


class ErrorAPIResponse(APIResponse):
    def __init__(self, message, error_type=None, data=None):
        super().__init__('error', message=message, data=data, error_type=error_type)
