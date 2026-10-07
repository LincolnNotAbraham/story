from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base 

from core.config import settings

engine = create_engine(
    url=settings.DATABASE_URL
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    """Fornece uma sessao do banco para injecao de dependencia (FastAPI)."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_table():
    """Cria as tabelas do banco de dados se ainda nao existirem."""
    from models.job import StoryJob
    from models.story import Story, StoryNode
    Base.metadata.create_all(bind=engine)