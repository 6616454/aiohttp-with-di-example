from rodi import Container

from src.di.factories import provide_db_settings
from src.settings import DBSettings


def get_container() -> Container:
    container = Container()

    container.add_scoped_by_factory(provide_db_settings, DBSettings)

    return container
