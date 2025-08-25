from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    API_PREFIX : str = "/api"
    DEBUG :bool = False
    DATABASE_URL: str = "sqlite:///./app.db"
    ALLOWED_ORIGINS:str = ""
    GOOGLE_API_KEY: str=""
    SECRET_KEY : str=""
    ALGORITHM: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v:str)->List[str]:
        return v.split(",") if v else []
    
    class Config:
        env_file= ".env"
        env_file_encoding="utf-8"
        case_sensitive = True

settings = Settings()