from rest_framework.exceptions import APIException
from rest_framework.response import Response


def exception_handler(exception: Exception, context: dict) -> Response:
    if isinstance(exception, APIException):
        return Response(exception.detail, exception.status_code)
    return Response(str(exception), status=500)
