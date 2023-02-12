from aiohttp.web import Application as AiohttpApplication, Request as AiohttpRequest
from rodi import Container


class Application(AiohttpApplication):
    container: Container | None = None


class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app()
