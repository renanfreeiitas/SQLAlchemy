import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.future.engine import Engine

from pathlib import Path # Usado no SQLite3
from typing import Optional

from models.model_base import ModelBase


__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False):
    global __engine
    
    if __engine:
        return
    
    if sqlite:
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent  # definindo que o arquivo sera criado dentro do diretorio "pai"
        folder.mkdir(parents=True, exist_ok=True)
        
        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False})
    else:
        conn_str = ""
