import jwt
from uuid import UUID
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import CEOUser
from app.security import decode_access_token
bearer_scheme = HTTPBearer(auto_error=False)
def get_current_ceo(credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme), db: Session = Depends(get_db)) -> CEOUser:
    unauthorized = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required", headers={"WWW-Authenticate":"Bearer"})
    if credentials is None:
        raise unauthorized
    try:
        user_id: UUID = decode_access_token(credentials.credentials)
    except (jwt.InvalidTokenError, ValueError, TypeError):
        raise unauthorized
    user = db.get(CEOUser, user_id)
    if user is None or not user.is_active:
        raise unauthorized
    return user
