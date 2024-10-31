
from django.core.exceptions import ObjectDoesNotExist, ValidationError, BadRequest
from src.contracts.constant import Constants
from src.services.api_response import send_json_response as api_response

http_codes = Constants.HttpResponseCodes

class ExceptionHandler:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Exception:
        return self.get_response(request)
    
    def process_exception(self, request, exception):
        exception_handlers = {
            ObjectDoesNotExist: (self.handle_exception, http_codes.NOT_FOUND, "Entity not found"),
            ValidationError: (self.handle_exception, http_codes.INTERNAL_SERVER_ERROR, "Unprocessable entity"),
            BadRequest: (self.handle_exception, http_codes.BAD_REQUEST, "Invalid request")
        }

        handler, code, message = self.get_exception_handler(exception, exception_handlers)
        
        return handler(exception, code, message, request)
    
    def get_exception_handler(self, exception, handlers):
        for exception_type, handler_info in handlers.items():
            if isinstance(exception, exception_type):
                return handler_info

        return self.handle_exception, http_codes.INTERNAL_SERVER_ERROR, "Internal server error"
    
    def handle_exception(self, exception, code, message, request):
        return api_response(
            code=code,
            result="error",
            message=message,
            data={"error": str(exception)},
            url=request.path,
            user=request.user.username if request.user.is_authenticated else "Anonymous",
            payload=request.body
        )