from tile import Tile


type Tiles = list[list[Tile]]


class TileMap:
    def __init__(self, width: int, height: int) -> None:
        self.w = width
        self.h = height
        self.create_tiles()

    def create_tiles(self) -> None:
        self.tiles: Tiles = [[]]
        for i in range(self.w):
            for j in range(self.h):
                self.tiles[i, j] = Tile(i, j)

    def blocked(self, x, y) -> bool:
        return self.tiles[x, y].blocked

    def block(self, x, y) -> None:
        self.tiles[x, y].blocked = True

    def free(self, x, y) -> None:
        self.tiles[x, y].blocked = False
