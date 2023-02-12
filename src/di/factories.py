from envdataclass import from_file
from rodi import ActivationScope

from src.settings import DBSettings


def provide_db_settings(scope: ActivationScope) -> DBSettings:
    return from_file(DBSettings, '.env')
