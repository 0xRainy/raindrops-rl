import tcod
import tcod.event
import events
import renderer
from entity import Entity

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
evnt_handler = events.Event_Handler(player)

monster = Entity(0, 2, 2, 'k', (255, 0, 0))
entities = [player, monster]

running = True
while running:
    console.clear()
    renderer.render(console, entities, SCREEN_WIDTH, SCREEN_HEIGHT)
    tcod.console_flush()
    evnt_handler.handle_event()
    for event in tcod.event.wait():
        if event.type == "QUIT":
            running = False

        elif event.type == "KEYDOWN":
            evnt_handler.addevent(event)

        else:
            pass
