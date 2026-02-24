from rest_framework import status
from rest_framework.exceptions import APIException


    # --> Exceção personalizada para recursos duplicados.
class DuplicateResourceException(APIException):
    
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Recurso duplicado.'
    default_code = 'duplicate_resource'
    
    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code
        
        super().__init__(detail, code)
