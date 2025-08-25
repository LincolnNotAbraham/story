from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel


class UserCreate(BaseModel): #oq servidor recebe
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    create_at: datetime
    
    class Config:
        from_attributes= True

class Token(BaseModel):
    acess_token: str
    token_typee: str

class TokenData(BaseModel):
    username: Optional[str] = None    

    