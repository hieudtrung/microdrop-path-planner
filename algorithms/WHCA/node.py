from __future__ import annotations


class Node:
    """A base class for path finding algorithms"""

    def __init__(self, x: int, y: int, t: int) -> None:
        self.x = x
        self.y = y
        self.t = t
        self.cost: float = 0.0
        self.heuristic: float = 0.0
        self.parent: Node = None

    def getF(self) -> float:
        return self.heuristic + self.cost

    def __eq__(self, other: Node) -> bool:
        return (self.x == other.x) and (self.y == other.y)

    def compareTo(self, other: Node) -> int:
        f, of = self.getF(), other.getF()
        if f < of:
            return -1
        elif f > of:
            return 1
        else: # f = of
            return 0
