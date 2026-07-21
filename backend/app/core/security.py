import uuid
from datetime import datetime, timedelta, timezone
from enum import Enum

import bcrypt
import jwt

from app.core.config import settings

# bcrypt's underlying algorithm only uses the first 72 bytes of the
# input — anything beyond that is silently ignored by the C library, but
# some builds raise instead. Truncating explicitly here makes the
# behavior consistent and prevents a long (but otherwise valid) password
# from throwing an error deep inside the bcrypt call.
_MAX_BCRYPT_BYTES = 72


class TokenType(str, Enum):
    ACCESS = "access"
    REFRESH = "refresh"


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")[:_MAX_BCRYPT_BYTES]
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode("utf-8")[:_MAX_BCRYPT_BYTES]
    return bcrypt.checkpw(password_bytes, hashed_password.encode("utf-8"))


def _create_token(subject: str, token_type: TokenType, expires_delta: timedelta) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": subject,
        "type": token_type.value,
        "iat": now,
        "exp": now + expires_delta,
        "jti": str(uuid.uuid4()),
    }
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def create_access_token(user_id: str) -> str:
    return _create_token(
        user_id,
        TokenType.ACCESS,
        timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )


def create_refresh_token(user_id: str) -> str:
    return _create_token(
        user_id,
        TokenType.REFRESH,
        timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
    )


def decode_token(token: str) -> dict:
    return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])