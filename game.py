import tcod
import tcod.event
import events
import player

tcod.console_set_custom_font("terminal32x32_gs_ro.png",
                             tcod.FONT_LAYOUT_ASCII_INROW
                             | tcod.FONT_TYPE_GRAYSCALE)

SCREEN_WIDTH = 40
SCREEN_HEIGHT = 28


console = tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT,
                                 'raindrops-roguelike',
                                 renderer=tcod.RENDERER_OPENGL2, order='F',
                                 vsync=True,)
p = player.Player(0)

running = True
while running:
    console.clear()
    player.Player.draw(p)
    tcod.console_flush()
    events.Event_Handler.handle_event()
    for event in tcod.event.wait():
        if event.type == "QUIT":
            running = False

        elif event.type == "KEYDOWN":
            events.Event_Handler.addevent(event)
