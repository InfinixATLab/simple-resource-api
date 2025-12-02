from rest_framework.views import exception_handler
from rest_framework.response import Response
from .exceptions import DuplicateResourceException


def custom_exception_handler(exc, context):
   
    response = exception_handler(exc, context)
    
    if isinstance(exc, DuplicateResourceException):
        custom_response_data = {
            'erro': str(exc.detail),
            'codigo': exc.default_code,
            'status': exc.status_code
        }
        return Response(custom_response_data, status=exc.status_code)
    
   
    if response is not None:

        if hasattr(response.data, 'detail'):
            custom_response_data = {
                'erro': response.data['detail'],
                'status': response.status_code
            }
        else:
            custom_response_data = response.data
        
        response.data = custom_response_data
    
    return response
