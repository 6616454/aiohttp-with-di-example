from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


def create_engine(database_url: str, echo_mode: bool = False):
    engine = create_async_engine(url=database_url, echo=echo_mode)
    return engine


def create_pool(engine: str) -> sessionmaker:
    pool = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
    )
    return pool
