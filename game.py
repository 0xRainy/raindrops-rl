import tcod
import tcod.event
import events
import renderer
from random import randint
from entity import Entity
from events import playerevents

tcod.console_set_custom_font("terminal32x32_gs_ro.png",
                             tcod.FONT_LAYOUT_ASCII_INROW
                             | tcod.FONT_TYPE_GRAYSCALE)

SCREEN_WIDTH = 40
SCREEN_HEIGHT = 28

player_x = 1
player_y = 1

console = tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT,
                                 'raindrops-roguelike',
                                 renderer=tcod.RENDERER_OPENGL2, order='F',
                                 vsync=True,)
player = Entity(0, player_x, player_y, '@', (255, 255, 255))

twitch_names = ['Sticc', 'Maki', 'Emi', 'Bones']
monster = Entity(0, 2, 2, 'k', (255, 0, 0))
entities = [monster]
evnt_handler = events.Event_Handler(player)

for name in twitch_names:
    entities.append(Entity(0, randint(1, SCREEN_WIDTH - 1), randint(1, SCREEN_HEIGHT - 1), name[:1].lower(), ((randint(100, 255), randint(100, 255), randint(100, 255)))))

running = True
while running:
    console.clear(fg=(255, 0, 0))
    renderer.draw_entity(0, player)
    renderer.render(console, entities, SCREEN_WIDTH, SCREEN_HEIGHT)
    tcod.console_flush()
    evnt_handler.handle_event()
    for i in playerevents:
        if i == 'PLAYERMOVED':
            for entity in entities:
                dname = entity.char
                entities.pop(entities.index(entity))
                dx = entity.x + randint(-1, 1)
                dy = entity.y + randint(-1, 1)
                entities.append(Entity(0, dx, dy, dname, ((randint(100, 255), randint(100, 255), randint(100, 255)))))
        playerevents.pop(playerevents.index(i))
    for event in tcod.event.wait():
        if event.type == "QUIT":
            running = False

        elif event.type == "KEYDOWN":
            evnt_handler.addevent(event)

        else:
            pass
