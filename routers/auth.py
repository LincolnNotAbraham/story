import jwt

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jwt import PyJWTError as JWTError
from datetime import datetime, timedelta



router = APIRouter(
    prefix="/auth",
    tags=["authentication"] 
)



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")




def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_pass: str, hashed_pass: str) ->bool:
    return pwd_context.verify(plain_pass, hashed_pass)

senha = "aa"
hash_teste = hash_password(senha);

print(f"hahs: {hash_teste}")
print(f"ver: {verify_password(senha,hash_teste)}")
