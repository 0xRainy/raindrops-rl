import player

eventlist = []


class Event_Handler(object):

    @classmethod
    def addevent(cls, event):
        eventlist.append(event)

    def handle_event():
        move = player.Player.move
        for event in eventlist:
            print(event.scancode)
            if event.type == 'KEYDOWN':
                if event.scancode == 82:
                    move(0, -1)
                    print('UP')
                elif event.scancode == 81:
                    move(0, 1)

                elif event.scancode == 79:
                    move(1, 0)

                elif event.scancode == 80:
                    move(-1, 0)
