from common import RouteFinder, TileMap, BiHashMap
from reservation import ReservationTable
from node import Node
from route import Route, Step
import numpy as np


class WHCARouteFinder(RouteFinder):
    def __init__(self, reservation: ReservationTable, tile_map: TileMap) -> None:
        super().__init__()
        self.reservation = reservation
        self.tile_map = tile_map
        self.closed: list[Node] = []
        self.opened: list[Node] = []
        self.nodes = [[[]]]
        self.heuristic_cache = BiHashMap()

    def maxF(self) -> float:
        return self.tile_map.w * self.tile_map.h * 2

    def get_heuristic_cost(self):
        ...

    def get_available_neighbors(self, current: Node):
        ...

    def is_valid_location(self):
        ...

    def is_valid_move(self):
        ...

    def find(self, sX: int, sY: int, tX: int, tY: int) -> Route:
        # initial state for A*. The closed group is empty. Only the starting tile is in the opened list and it'e're already there
        self.closed.clear()
        self.opened.clear()
        self.heuristic_cache.clear()

        width, height, time = self.reservation.getDims()
        nodes = np.zeros((time, width, height), dtype=int).tolist()
        for i in range(width):
            for j in range(height):
                for k in range(time):
                    nodes[i][j][k] = Node(i, j, k, self.maxF())

        start_node = nodes[sX][sY][0]
        start_node.cost = 0.0
        hcost = self.get_heuristic_cost(sX, sY, 0, tX, tY)
        if hcost == None:
            hcost = self.maxF()

        start_node.heuristic = hcost
        self.opened.append(start_node)  # TODO replace normal list by SortedList

        while self.opened:  # Loop until the list `opened` is empty
            current = self.opened[0]
            if current.x == tX and current.y == tY and current.t == time - 1:
                route = Route()
                node = nodes[tX][tY][current.t]

                while node != start_node:
                    step = Step(node.x, node.y, node.t)
                    route.prepend_step(step)
                    node = node.parent
                    assert node == None, "Empty target"

                route.prepend_step(sX, sY, 0)
                return route

            self.opened.remove(current)
            self.closed.append(current)

            neighbors: list[Node] = self.get_available_neighbors(current)
            for neighbor in neighbors:
                if not self.is_valid_location(
                    sX, sY, neighbor.x, neighbor.y, neighbor.t
                ):
                    continue

                if not self.is_valid_move(
                    current.x, current.y, current.t, neighbor.x, neighbor.y, neighbor.t
                ):
                    continue

                next_step_cost = current.cost + self.get_movement_cost(
                    current.x, current.y, neighbor.x, neighbor.y, tX, tY
                )

                if next_step_cost < neighbor.cost:
                    if neighbor in self.opened:
                        self.opened.remove(neighbor)
                    if neighbor in self.closed:
                        self.closed.remove(neighbor)

                if not (neighbor in self.opened or neighbor in self.closed):
                    neighbor.cost = next_step_cost
                    hcost = self.get_heuristic_cost(
                        neighbor.x, neighbor.y, neighbor.t, tX, tY
                    )
                    if hcost == None:
                        hcost = self.maxF()

                    neighbor.heuristic = hcost
                    neighbor.parent = current
                    self.opened.append(neighbor)
