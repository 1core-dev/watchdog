from fastapi import HTTPException, status
from passlib.hash import bcrypt
from jose import jwt, JWTError
from pydantic import ValidationError
from .. import tables

from ..models.auth import User, Token
from ..settings import settings


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, plain_password: str) -> str:
        return bcrypt.hash(plain_password)

    @classmethod
    def validate_token(cls, token: str) -> User:
        exeption = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Couldn\'t validate credentials',
            headers={
                'WWW-Authenticate': 'bearer'
            }
        )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=settings.jwt_algorithm,
            )
        except JWTError:
            raise exeption from None

        user_data = payload.get('user')

        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise exeption from None
        return user

    @classmethod
    def create_token(cls, user: tables.User) -> Token:
        user_data = User.from_orm(user)
