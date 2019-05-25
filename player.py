import tcod


class Player():
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

    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

    def draw(self):
        self.con.put_char(self.x, self.y, self.ch, self.bg_blend)