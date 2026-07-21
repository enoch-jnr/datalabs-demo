import uuid

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_active_user
from app.core.security import TokenType, decode_token
from app.modules.audit.service import log_action
from app.modules.core import service
from app.modules.core.models import User
from app.modules.core.schemas import Token, TokenRefreshRequest, UserCreate, UserLogin, UserRead

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserRead, status_code=201)
async def register(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await service.register_user(db, payload)
    await log_action(db, action="USER_REGISTERED", resource_type="user", actor_id=user.id, resource_id=user.id)
    return user


@router.post("/login", response_model=Token)
async def login(payload: UserLogin, db: AsyncSession = Depends(get_db)):
    user = await service.authenticate_user(db, payload.email, payload.password)
    await log_action(db, action="USER_LOGIN", resource_type="user", actor_id=user.id, resource_id=user.id)
    return service.build_token_pair(user)


@router.post("/refresh", response_model=Token)
async def refresh(payload: TokenRefreshRequest, db: AsyncSession = Depends(get_db)):
    try:
        decoded = decode_token(payload.refresh_token)
        if decoded.get("type") != TokenType.REFRESH.value:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    result = await db.execute(select(User).where(User.id == uuid.UUID(decoded["sub"])))
    user = result.scalar_one_or_none()
    if user is None or not user.is_active:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    return service.build_token_pair(user)


@router.get("/me", response_model=UserRead)
async def me(current_user: User = Depends(get_current_active_user)):
    return current_user
