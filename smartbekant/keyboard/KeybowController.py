import keybow
import zope.event

from smartbekant.keyboard.KeyBowEvent import KeyBowEvent

keybow.setup(keybow.MINI)
UP = 0
DOWN = 1
MEMORY = 2


def set_led(button: int, colour):
    r, g, b = colour
    keybow.set_led(button, r, g, b)
    keybow.show()


def set_leds(colour):
    r, g, b = colour
    for i in range(3):
        keybow.set_led(i, r, g, b)
    keybow.show()


class KeybowController:
    def __init__(self, background=[255, 100, 100], up_colour=[0, 255, 0], down_colour=[255, 0, 0],
                 memory_colour=[0, 0, 255], verbose=False):
        self.background = background
        self.colours = {0: up_colour, 1: down_colour, 2: memory_colour}
        self.verbose = verbose
        set_leds(self.background)

    def handle_key(self, index: int, state: bool):
        event = KeyBowEvent(index, state)
        zope.event.notify(event)
        if self.verbose:
            print(f'key {index} has been {"pressed" if state else "released"}')
        if state is False:
            set_led(index, self.background)
        else:
            set_led(index, self.colours[index])
