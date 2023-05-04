import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.future.engine import Engine

from pathlib import Path  # Usado no SQLite3
from typing import Optional

from models.model_base import ModelBase


__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    """
    Funcao para configurar a conexao com o banco de dados
    """
    global __engine

    if __engine:
        return

    if sqlite:
        arquivo_db = 'db/picoles.sqlite'
        # definindo que o arquivo sera criado dentro do diretorio "pai"
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={
                                    "check_same_thread": False})
    else:
        conn_str = "postgresql://postgres:password@localhost:5432/picoles"
        __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    """
    Funcao para criar a sessao de conexao com o banco de dados
    """
    global __engine

    if not __engine:
        create_engine()  # funcao para quem usar o sqlite3 (precisa alterar na funcao: create_engine(sqlite: bool = True))

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session


def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()

    import models.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
