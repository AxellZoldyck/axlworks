from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.config import settings
from app.db import get_db
from app.dependencies import get_current_ceo
from app.models import AuditLog, CEOUser
from app.schemas import CEOResponse, LoginRequest, TokenResponse
from app.security import create_access_token, verify_password
router = APIRouter(prefix="/auth", tags=["Authentication"])
@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, request: Request, db: Session = Depends(get_db)) -> TokenResponse:
    user = db.scalar(select(CEOUser).where(CEOUser.email == payload.email.lower()))
    if user is None or not user.is_active or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email or password is incorrect")
    db.add(AuditLog(actor_type="ceo",actor_id=str(user.id),action="auth.login",resource_type="ceo_user",resource_id=str(user.id),request_id=request.headers.get("X-Request-ID"),details={}))
    db.commit()
    return TokenResponse(access_token=create_access_token(user.id),expires_in=settings.jwt_access_token_minutes*60)
@router.get("/me", response_model=CEOResponse)
def me(current_user: CEOUser = Depends(get_current_ceo)) -> CEOUser:
    return current_user
@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(_: CEOUser = Depends(get_current_ceo)) -> None:
    # Stateless token: client discards it. Server-side revocation is a pending hardening task.
    return None
