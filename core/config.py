from typing import List
from pydantic import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    API_PREFIX : str = "\api"
    DEBUG :bool = False
    DATABASE_URL:str
    ALLOWED_ORIGINS:str = ""
    OPENAPI_API_KEY: str

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v:str)->List[str]:
        return v.slit(",") if v else []
    
    class Config:
        env_file= ".env"
        env_file_encoding="utf-8"
        case_sensitive = True

settings = Settings()