from aiohttp.web import run_app

from aiohttp_apispec import setup_aiohttp_apispec

from src.presentation.api.classes import Application
from src.presentation.api.handlers import setup_routes


def build_app() -> Application:
    app = Application()

    setup_routes(app.router)
    setup_aiohttp_apispec(
        app=app,
        title='My Documentation',
        version='v1',
        swagger_path='/api/docs'
    )

    return app


if __name__ == "__main__":
    run_app(build_app())
