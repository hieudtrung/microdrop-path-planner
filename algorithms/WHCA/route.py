from __future__ import annotations
from typing import Optional


class Step:
    def __init__(self, x: int, y: int, t: int) -> None:
        self.x = x
        self.y = y
        self.t = t

    def hash_code(self):
        return self.x * self.y

    def __eq__(self, other: Step) -> bool:
        return (self.x == other.x) and (self.y == other.y) and (self.t == other.t)


type Steps = list[Step]


class Path:
    def __init__(self, steps: Optional[Steps] = []) -> None:
        self.steps = steps

    @property
    def length(self):
        return len(self.steps) if self.steps else 0

    def prepend_step(self, step: Step) -> None:
        self.steps.insert(0, step)

    def get_step(self, index: int) -> Step:
        return self.steps[index]
