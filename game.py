import tcod
import tcod.event
import events
import renderer
from items import Item
from levelmap import levelmap, player_x, player_y
from random import randint
from entity import Entity
from events import playerevents
from twitchobserver import Observer

tcod.console_set_custom_font("terminal32x32_gs_ro.png",
                             tcod.FONT_LAYOUT_ASCII_INROW
                             | tcod.FONT_TYPE_GRAYSCALE)


SCREEN_WIDTH = 40
SCREEN_HEIGHT = 28
MAP_WIDTH = 30
MAP_HEIGHT = 25
room_max_size = 7
room_min_size = 4
max_rooms = 30
max_monsters = 10
console = tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT,
                                 'raindrops-roguelike',
                                 renderer=tcod.RENDERER_OPENGL2, order='F',
                                 vsync=True,)

player = Entity(0, player_x, player_y, '@', (255, 255, 255))

levelmap.gen_map(max_rooms, room_min_size, room_max_size, MAP_WIDTH,
                 MAP_HEIGHT, player)

observer = Observer('Raindrops_RL', 'oauth:49yke9x8i41z2qlfeoufh4y45o1emy')
observer.start()
observer.join_channel('moonmoon_ow')

max_monsters = 0
twitch_names = []
monster = Entity(0, 2, 2, 'k', (255, 0, 0))
items = []
entities = []
tnames = []
evnt_handler = events.Event_Handler(player)
hx = 0
hy = 0


running = True
while running:
    console.clear(fg=(255, 0, 0))
    renderer.render(console, entities, items, levelmap, SCREEN_WIDTH,
                    SCREEN_HEIGHT)
    renderer.draw_entity(0, player)
    evnt_handler.handle_event()
    for event in observer.get_events():
        print(len(twitch_names), twitch_names)
        if event.type == 'TWITCHCHATMESSAGE':
            if event.nickname not in twitch_names:
                if max_monsters < 10:
                    twitch_names.append(event.nickname)
                    for n in twitch_names:
                        tnames.append(n)
                    while levelmap.is_solid(hx, hy) and twitch_names:
                        hx = randint(1, MAP_WIDTH - 1)
                        hy = randint(1, MAP_HEIGHT - 1)
                        if not levelmap.is_solid(hx, hy):
                            name = event.nickname
                            entities.append(Entity(0, hx, hy, name[:1].lower(),
                                            ((randint(100, 255),
                                              randint(100, 255),
                                              randint(100, 255)))))
                            twitch_names.pop(twitch_names.index(name))
                            max_monsters = max_monsters + 1
                            hx = 0
                            hy = 0
                            break
    for i in playerevents:
        if i == 'PLAYERMOVED':
            for entity in entities:
                if entity.char not in entities:
                    dname = entity.char
                    dcolor = entity.color
                    if randint(0, 1) == 1:
                        dx = entity.x + randint(-1, 1)
                        dy = entity.y + randint(-1, 1)
                        if (dy > MAP_HEIGHT - 1 or dx > MAP_WIDTH - 1 or dy < 0
                                or dx < 0 or levelmap.is_solid(dx, dy)):
                            pass
                        else:
                            entities.pop(entities.index(entity))
                            entities.append(Entity(0, dx, dy, dname, dcolor))
                            print(entity.char)
                            print(twitch_names)
                    else:
                        pass
            playerevents.pop(playerevents.index(i))
    for entity in entities:
        if (player.x, player.y) == (entity.x, entity.y):
            entities.pop(entities.index(entity))
            max_monsters = max_monsters - 1
            print(tnames)
            tnames.pop()
            items.append(Item(0, player.x, player.y, '!', (255, 255, 255),
                         'Potion', 'health'))
    for item in items:
        if (player.x, player.y) == (item.x, item.y):
            if 'SPACEPRESS' in playerevents:
                tcod.console_put_char(0, player.x, player.y, ' ')
                items.pop(items.index(item))
                playerevents.clear()
            else:
                pass
    # PrintNames()
    tcod.console_flush()
    for event in tcod.event.wait():
        if event.type == "QUIT":
            observer.stop()
            running = False

        elif event.type == "KEYDOWN":
            evnt_handler.addevent(event)
