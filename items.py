import tcod


class Item():
    def __init__(
            self,
            con,
            x=1,
            y=1,
            char=' ',
            color=tcod.COLOR_LIGHTEST,
            name=' ',
            stat=' '
    ):
        self.con = con
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.stat = stat
