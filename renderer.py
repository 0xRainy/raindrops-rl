import tcod
import entity as ent


def render(con, entities, levelmap, screen_width, screen_height):
    for y in range(levelmap.width):
        for x in range(levelmap.height):
            wall = levelmap.tiles[x][y].solid
            if wall:
                draw_entity(0, ent.Entity(0, x, y, '#', (255, 255, 255)))
            else:
                draw_entity(0, ent.Entity(0, x, y, ' ', (0, 0, 0)))

    for entity in entities:
        draw_entity(con, entity)


def clear(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity):
    tcod.console_set_default_foreground(con, entity.color)
    tcod.console_put_char(con, entity.x, entity.y, entity.char,
                          tcod.BKGND_NONE)


def clear_entity(con, entity):
    tcod.console_put_char(con, entity.x, entity.y, ' ', tcod.BKGND_NONE)
