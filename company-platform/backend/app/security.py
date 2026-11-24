from datetime import datetime, timedelta, timezone
from uuid import UUID
import jwt
from pwdlib import PasswordHash
from app.core.config import settings
password_hash = PasswordHash.recommended()
def hash_password(password: str) -> str:
    if len(password) < 12:
        raise ValueError("Password must contain at least 12 characters")
    return password_hash.hash(password)
def verify_password(password: str, hashed: str) -> bool:
    try:
        return password_hash.verify(password, hashed)
    except Exception:
        return False
def create_access_token(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    payload = {"sub":str(user_id),"iat":now,"exp":now+timedelta(minutes=settings.jwt_access_token_minutes),"type":"access"}
    return jwt.encode(payload, settings.jwt_secret_key, algorithm="HS256")
def decode_access_token(token: str) -> UUID:
    payload = jwt.decode(token, settings.jwt_secret_key, algorithms=["HS256"], options={"require":["sub","exp","iat","type"]})
    if payload.get("type") != "access":
        raise jwt.InvalidTokenError("Invalid token type")
    return UUID(payload["sub"])
