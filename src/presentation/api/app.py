from aiohttp.web import run_app

from aiohttp_apispec import setup_aiohttp_apispec

from src.di import setup_di
from src.presentation.api import Application
from src.presentation.api.handlers import setup_routes


def build_app() -> Application:
    app = Application()

    setup_routes(router=app.router)
    setup_aiohttp_apispec(
        app=app,
        title='My Documentation',
        version='v1',
        swagger_path='/api/docs'
    )
    setup_di(app=app)

    return app


if __name__ == "__main__":
    run_app(build_app())
