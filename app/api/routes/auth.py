from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import create_access_token, verify_password
from app.models import AdminUser
from app.schemas.auth import AuthLoginRequest, AuthLoginResponse, AuthUserResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=AuthLoginResponse)
def login(payload: AuthLoginRequest, db: Session = Depends(get_db)):
    user = db.query(AdminUser).filter(AdminUser.email == payload.email.lower()).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": {"code": "invalid_credentials", "message": "Invalid email or password"}},
        )

    token = create_access_token(subject=user.email)
    return AuthLoginResponse(
        user=AuthUserResponse(id=user.id, email=user.email, role=user.role),
        token=token,
    )


@router.post("/logout")
def logout():
    return {"status": "ok", "message": "For JWT auth, logout is handled client-side by discarding token"}
