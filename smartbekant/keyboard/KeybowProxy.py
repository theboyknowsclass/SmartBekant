import zope.event

from smartbekant.keyboard.KeyBowEvent import KeyBowEvent


class KeybowProxy:
    def __init__(self, background=[255, 100, 100], up_colour=[0, 255, 0], down_colour=[255, 0, 0],
                 memory_colour=[0, 0, 255]):
        self.background = background
        self.up_colour = up_colour
        self.down_colour = down_colour
        self.memory_colour = memory_colour

    def handle_key(self, index, state):
        event = KeyBowEvent(index, state)
        zope.event.notify(event)
