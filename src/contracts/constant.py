"""
    File used to enumerate Http response codes
"""
from enum import Enum


class Constants:
    """
        Class with every constant used in the app
    """

    class HttpResponseCodes(Enum):
        """
            Http response codes enum
        """
        SUCCESS = 200
        CREATED = 201
        BAD_REQUEST = 400
        UNAUTHENTICATED = 401
        FORBIDDEN = 403
        NOT_FOUND = 404
        NOT_ALLOWED = 405
        INTERNAL_SERVER_ERROR = 500