from aiohttp.web_routedef import UrlDispatcher

from src.presentation.api.handlers.post import router as posts_router


def setup_routes(router: UrlDispatcher) -> None:
    router.add_routes(posts_router)
