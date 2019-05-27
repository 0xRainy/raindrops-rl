from collision import Collision
from tools import Rect

MAP_WIDTH = 30
MAP_HEIGHT = 25


class Level_Map:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.tiles = self.gen_tiles()

    def gen_tiles(self):
        tiles = [[Collision(True) for x in range(self.width)] for y in
                 range(self.height)]
        return tiles

    def make_room(self, room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].solid = False

    def gen_map(self):
        room1 = Rect(0, 0, 6, 6)
        room2 = Rect(8, 8, 6, 6)

        self.make_room(room1)
        self.make_room(room2)

    def is_solid(self, x, y):
        if self.tiles[x][y].solid:
            return True

        return False


levelmap = Level_Map(MAP_WIDTH, MAP_HEIGHT)
