from src.business_logic.dto.post import PostDTO
from src.infrastructure.db.client import SomeDatabaseClient
from src.infrastructure.db.models.post import SomePostModel


class PostService:
    def __init__(self, db_client: SomeDatabaseClient):
        self._db = db_client

    def get_post_by_id(self, id_: str):
        post = self._db.get_by_id(SomePostModel, id_)
        return PostDTO(title=post['title'], body=post['body'])
