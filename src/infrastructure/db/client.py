class SomeDatabaseClient:
    def __init__(self, bar: str):
        self.foo = bar

    def get_by_id(self, model: dict, id_: int) -> dict:
        return model.get(id_)
