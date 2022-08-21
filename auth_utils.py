from datetime import datetime, timedelta

import jwt
from decouple import config
from fastapi import HTTPException, status
from passlib.context import CryptContext

JWT_KEY = config("JWT_KEY")


class AuthJwtCsrf:
    pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret_key = JWT_KEY

    def generate_hash_pw(self, password: str) -> str:
        return self.pwd_ctx.hash(password)

    def verify_pw(self, plain_pw, hashed_pw):
        return self.pwd_ctx.verify(plain_pw, hashed_pw)

    def encode_jwt(self, email) -> str:
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, minutes=5),
            "iat": datetime.utcnow(),
            "sub": email
        }
        return jwt.encode(
            payload,
            self.secret_key,
            algorithm="HS256"
        )

    def decode_jwt(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="The JWT has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="JWT is not valid")
