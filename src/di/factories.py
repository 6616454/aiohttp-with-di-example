from envdataclass import from_file
from rodi import ActivationScope
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker

from src.infrastructure.db.base import create_pool
from src.settings import DBSettings


def provide_db_settings(scope: ActivationScope) -> DBSettings:
    return from_file(DBSettings, '.env')


def provide_pool_sessions(scope: ActivationScope) -> sessionmaker:
    engine = scope.provider.get(AsyncEngine)

    return create_pool(engine)
