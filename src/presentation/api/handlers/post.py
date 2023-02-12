from aiohttp.web_response import json_response
from aiohttp.web_routedef import RouteTableDef
from aiohttp_apispec import docs, response_schema

from src.business_logic.services.post import PostService
from src.presentation.api import Request
from src.presentation.api.handlers.responses.post import OutputPost

router = RouteTableDef()


@docs(
    tags=['posts'],
    summary='Get post',
    description='Get post by id'
)
@response_schema(OutputPost())
@router.get('/posts/{id}')
async def get_post(request: Request):
    post_service = request.app.container.resolve(PostService)

    post = post_service.get_post_by_id(int(request.match_info['id']))

    return json_response(OutputPost().dump(post))


@docs(
    tags=['posts'],
    summary='Get posts',
    description='Get all posts'
)
@router.get('/posts')
async def get_posts(request: Request):
    ...


@docs(
    tags=['posts'],
    summary='Create post',
    description='Create new post'
)
@router.post('/posts')
async def create_post(request: Request):
    ...


@docs(
    tags=['posts'],
    summary='Update post',
    description='Update(patch) post by id'
)
@router.patch('/posts/{id}')
async def update_post(request: Request):
    ...


@docs(
    tags=['posts'],
    summary='Delete post',
    description='Delete post by id'
)
@router.delete('/posts/{id}')
async def delete_post(request: Request):
    ...
