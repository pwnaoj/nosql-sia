"""sia.py"""
from ..atlas.api import Api


class NosqlSia(Api):

    def __init__(self) -> None:
        super().__init__()


nosqlsia = NosqlSia()
