# eventlist = []


class Event_Handler():
    def __init__(self, actor, eventlist=[]):
        self.actor = actor
        self.eventlist = eventlist

    def addevent(self, event):
        self.eventlist.append(event)

    def handle_event(self):
        for event in self.eventlist:
            print(event.scancode, event.type)
            if event.type == 'KEYDOWN':
                if event.scancode == 82:
                    self.actor.move(0, -1)
                elif event.scancode == 81:
                    self.actor.move(0, 1)

                elif event.scancode == 79:
                    self.actor.move(1, 0)

                elif event.scancode == 80:
                    self.actor.move(-1, 0)
        # dirty hack, for some reason KEYDOWN events are added to the
        # eventlist multiple times on any event
        self.eventlist.clear()
