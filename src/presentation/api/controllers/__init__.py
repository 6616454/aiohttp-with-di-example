from aiohttp.web_routedef import UrlDispatcher

from src.presentation.api.controllers.post import router as posts_router


def setup_controllers(router: UrlDispatcher) -> None:
    router.add_routes(posts_router)
