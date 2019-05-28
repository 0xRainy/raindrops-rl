from collision import Collision
from tools import Rect
from random import randint

MAP_WIDTH = 30
MAP_HEIGHT = 25
player_x = 2
player_y = 2


class Level_Map:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.tiles = self.gen_tiles()

    def gen_tiles(self):
        tiles = [[Collision(True) for x in range(self.width)] for y in
                 range(self.height)]
        return tiles

    def gen_map(self, max_rooms, room_min_size, room_max_size, MAP_WIDTH,
                MAP_HEIGHT, player):
        # room1 = Rect(0, 0, 6, 6)
        # room2 = Rect(8, 8, 6, 6)

        # self.make_room(room1)
        # self.make_room(room2)
        rooms = []
        num_rooms = 0

        for r in range(max_rooms):
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            x = randint(0, MAP_WIDTH - w - 1)
            y = randint(0, MAP_HEIGHT - h - 1)

            new_room = Rect(x, y, w, h)

            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                self.make_room(new_room)
                (new_x, new_y) = new_room.center()
                if num_rooms == 0:
                    player.x = new_x
                    player.y = new_y
                else:
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
                    if randint(0, 1) == 1:
                        self.make_tunnelh(prev_x, new_x, prev_y)
                        self.make_tunnelv(prev_y, new_y, prev_x)
                    else:
                        self.make_tunnelv(prev_y, new_y, prev_x)
                        self.make_tunnelh(prev_x, new_x, prev_y)
                rooms.append(new_room)
                num_rooms += 1

    def make_room(self, room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].solid = False

    def make_tunnelh(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].solid = False

    def make_tunnelv(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].solid = False

    def is_solid(self, x, y):
        if self.tiles[x][y].solid:
            return True

        return False


levelmap = Level_Map(MAP_WIDTH, MAP_HEIGHT)
