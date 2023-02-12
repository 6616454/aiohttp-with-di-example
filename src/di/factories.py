from envdataclass import from_file
from rodi import ActivationScope

from src.business_logic.services.post import PostService
from src.infrastructure.db.client import SomeDatabaseClient
from src.settings import AppSettings


def build_settings(scope: ActivationScope) -> AppSettings:
    return from_file(AppSettings, '.env')


def build_db_client(scope: ActivationScope) -> SomeDatabaseClient:
    settings = scope.provider.get(AppSettings)

    return SomeDatabaseClient(settings.foo)


def build_post_service(scope: ActivationScope) -> PostService:
    db_client = scope.provider.get(SomeDatabaseClient)

    return PostService(db_client=db_client)
