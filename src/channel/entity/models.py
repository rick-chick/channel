from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime
from jose import jwt, JWTError
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"
SECRET_KEY = "SECRET_KEY"


class User(BaseModel):
    id: str
    email: str
    password: Optional[str] = None
    password_hash: Optional[str] = None
    devices: List["Device"] = []

    def hash_password(self):
        if (self.password):
            self.password_hash = pwd_context.hash(self.password)

    def is_authenticated(self) -> bool:
        if not self.password_hash or not self.password:
            return False
        return pwd_context.verify(self.password, self.password_hash)

    def create_jwt(self) -> str:
        return jwt.encode(
            {
                "sub": self.id
            },
            SECRET_KEY,
            algorithm=ALGORITHM
        )


class UserToken(BaseModel):
    id: Optional[str] = None
    token: str

    def is_authenticated(self) -> bool:
        try:
            decorded = jwt.decode(
                self.token,
                SECRET_KEY,
                algorithms=ALGORITHM
            )
            if not decorded:
                return False
            self.id = decorded['sub']
            return True
        except JWTError:
            return False


class Device(BaseModel):
    id: Optional[int] = None
    user_id: str
    tags: List[str] = []
    api_key: str


class Channel(BaseModel):
    device_id: int
    id: Optional[int] = None
    tags: Optional[List[str]]
    name: str
    unit: str


class Record(BaseModel):
    device_id: int
    time: datetime
    values: Dict[int, float]
