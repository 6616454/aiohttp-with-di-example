from rodi import Container

from src.business_logic.services.post import PostService
from src.di.factories import build_settings, build_db_client, build_post_service
from src.infrastructure.db.client import SomeDatabaseClient
from src.settings import AppSettings


def get_container() -> Container:
    container = Container()

    container.add_scoped_by_factory(build_settings, AppSettings)
    container.add_scoped_by_factory(build_db_client, SomeDatabaseClient)
    container.add_scoped_by_factory(build_post_service, PostService)

    return container
