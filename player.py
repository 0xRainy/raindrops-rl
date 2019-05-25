import tcod


class Player(object):
    def __init__(
        self,
        con,
        x=1,
        y=1,
        ch=64,
        bg_blend=tcod.BKGND_NONE
    ):

        self.con = con
        self.x = x
        self.y = y
        self.ch = ch
        self.bg_blend = bg_blend

    def move(x, y):
        Player.x += x
        Player.y += y

    def draw(self):
        tcod.console_put_char(self.con, self.x, self.y, self.ch, self.bg_blend)