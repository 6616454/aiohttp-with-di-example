from rodi import Container

from src.di.containers import get_container
from src.presentation.api import Application


def setup_di(app: Application) -> Container:
    app.container = get_container()
