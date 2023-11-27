import numpy as np
from typing import Optional


class ReservationTable:
    def __init__(self, width: int, height: int, time: int) -> None:
        self.w = width
        self.h = height
        self.c = time  # number of channels
        self.cells: np.ndarray = np.zeros(
            (self.c, self.w, self.h), dtype=bool
        )  # 1 = blocked, 0 = available

    def getDims(self):
        return self.w, self.h, self.c

    def clear(self) -> None:
        self.cells = np.zeros((self.c, self.w, self.h), dtype=bool)

    def blocked(self, x: int, y: int, t: Optional[int] = None) -> bool:
        return self.cells[t, x, y] if t else np.any(self.cells[:, x, y])

    def block(self, x: int, y: int, t: Optional[int] = None) -> None:
        # Must check argument validity as numpy automatically adds new elements if they are out-of-bound.
        assert (
            (0 <= x < self.w) and (0 <= y < self.h) and (0 <= t < self.c)
        ), "Position index is out of bound"

        if t:
            self.cells[t, x, y] = True
        else:
            self.cells[:, x, y] = True
