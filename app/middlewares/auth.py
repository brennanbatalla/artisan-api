from typing import Optional

from fastapi.security import HTTPBearer
from fastapi import HTTPException, Request


class TokenAuth(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(TokenAuth, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[bool]:
        token = request.headers.get('authorization')
        # TODO - validate token
        if not token:
            raise HTTPException(status_code=401, detail="Invalid token")
        return True