import tcod


class Entity():
    def __init__(
        self,
        con,
        x=1,
        y=1,
        char=' ',
        color=tcod.COLOR_LIGHTEST
    ):

        self.con = con
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        if self.x + dx > 39 or self.y + dy > 27 or self.x + dx < 0 or self.y + dy < 0:
            pass
        else:
            self.x += dx
            self.y += dy

    # def draw(self):
    #    tcod.console_put_char(self.con, self.x, self.y, self.char,
    #                          self.bg_blend)
