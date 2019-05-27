import tcod


class Entity():
    def __init__(
        self,
        con,
        x=1,
        y=1,
        char=' ',
        bg_blend=tcod.BKGND_NONE
    ):

        self.con = con
        self.x = x
        self.y = y
        self.char = char
        self.bg_blend = bg_blend

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        tcod.console_put_char(self.con, self.x, self.y, self.char,
                              self.bg_blend)
