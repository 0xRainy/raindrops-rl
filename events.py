playerevents = []


class Event_Handler():
    def __init__(self, actor, eventlist=[]):
        self.actor = actor
        self.eventlist = eventlist

    def addevent(self, event):
        self.eventlist.append(event)

    def handle_event(self):
        for event in self.eventlist:
            if event.type == 'KEYDOWN':
                if event.scancode == 82 or event.scancode == 14:  # UP
                    self.actor.move(0, -1)

                elif event.scancode == 81 or event.scancode == 13:  # DOWN
                    self.actor.move(0, 1)

                elif event.scancode == 80 or event.scancode == 11:  # LEFT
                    self.actor.move(-1, 0)

                elif event.scancode == 79 or event.scancode == 15:  # RIGHT
                    self.actor.move(1, 0)

                elif event.scancode == 28:  # UP_LEFT
                    self.actor.move(-1, -1)

                elif event.scancode == 24:  # UP_RIGHT
                    self.actor.move(1, -1)

                elif event.scancode == 5:  # DOWN_LEFT
                    self.actor.move(-1, 1)

                elif event.scancode == 17:  # DOWN_RIGHT
                    self.actor.move(1, 1)
            self.eventlist.pop(self.eventlist.index(event))
            playerevents.append('PLAYERMOVED')

        # dirty hack, for some reason KEYDOWN events are added to the
        # eventlist multiple times on any event
        # self.eventlist.clear()
