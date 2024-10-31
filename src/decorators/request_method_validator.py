"""
    Request method verification
"""
from functools import wraps
from django.core.exceptions import BadRequest


def required_method(expected_method):
    """
        Function to verify request method

        Args:
            expected_method (str): 'GET', 'POST', ...

        Returns:
            Raise a BadRequest if args do not match
            Function result if the args match
    """
    def decorator(func):

        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if request.method != expected_method:
                raise BadRequest(f"Expected {expected_method}, but got {request.method}")
            return func(request, *args, **kwargs)
        return wrapper
    
    return decorator