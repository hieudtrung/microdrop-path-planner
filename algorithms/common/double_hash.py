from typing import Any


class BiHashMap:
    def __init__(self) -> None:
        self.mMap: dict[dict] = {}

    def put(self, key1: Any, key2: Any, value: Any) -> None:
        self.mMap[key1] = {key2: value}

    def get(self, key1: Any, key2: Any) -> Any:
        try:
            return self.mMap[key1][key2]
        except KeyError:
            return None

    def contains(self, key1: Any, key2: Any) -> bool:
        return (key1 in self.mMap.keys()) and (key2 in self.mMap[key1].keys())
    
    def clear(self) -> None:
        self.mMap.clear()
