from typing import Any


class DoubleHashMap:
    def __init__(self) -> None:
        self.mMap: dict[dict] = {}

    def put(self, key1: Any, key2: Any, value: Any) -> None:
        self.mMap[key1] = {key2: value}

    def get(self, key1: Any, key2: Any) -> Any:
        return self.mMap[key1][key2]
