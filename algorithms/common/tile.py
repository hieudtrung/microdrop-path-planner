from __future__ import annotations

from math import abs, dist


class Tile:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.blocked: bool = False

    def __eq__(self, other: Tile) -> bool:
        return (self.x == other.x) and (self.y == other.y)

    def adjacent(self, other: Tile) -> bool:
        dx = abs(other.x - self.x)
        dy = abs(other.y - self.y)
        if dx == 0 and dy == 0:
            return False
        return dx <= 1 and dy <= 1

    def distance(self, other: Tile) -> float:
        return dist((self.x, self.y), (other.x, other.y))
