from rodi import Container
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker

from src.di.factories import provide_db_settings, provide_pool_sessions
from src.infrastructure.db.base import create_engine
from src.settings import DBSettings


def get_container() -> Container:
    container = Container()

    container.add_scoped_by_factory(provide_db_settings, DBSettings)
    container.add_singleton_by_factory(create_engine, AsyncEngine)
    container.add_scoped_by_factory(provide_pool_sessions, sessionmaker)

    return container
