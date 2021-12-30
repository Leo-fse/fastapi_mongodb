# The function of this file is to check wheter the request is authorized or not [ Verification of the protected route]


from typing import Optional

from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from .jwt_handler import decodeJWT


class jwtBearer(HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_Error)

    async def __call__(self, request: Request):
        credentials: Optional[HTTPAuthorizationCredentials] = await super(
            jwtBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid or Expired Token!")
            return credentials.credentials

        else:
            raise HTTPException(status_code=403, detail="Invalid or Expired Token!")

    def verify_jwt(self, jwtoken: str):
        isTokenValid: bool = False  # A false flag
        payload = decodeJWT(jwtoken)
        if payload:
            isTokenValid = True
        return isTokenValid
