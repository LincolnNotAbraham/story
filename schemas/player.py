from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel

class PlayerCreate(BaseModel):
    name: str
    session_id: str

class PlayerResponse(BaseModel):
    id: int
    name: str
    level: int
    experience: int
    attributes: Dict[str, int] 
    itens: Dict
    current_health: int
    max_health: int
    stories_complete: int
    
    class Config:
        from_atributes=True

class PlayerUpdate(BaseModel):
    experience: Optional[int] = None
    attributes: Optional[Dict[str, int]] = None
    itens: Optional[Dict] = None
    current_health: Optional[int] = None