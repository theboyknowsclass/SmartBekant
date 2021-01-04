from KeyBowEvent import *

class KeyBowClickEvent(KeyBowEvent):
    def __init__(self, index: int, state, click_count, long_press):
        KeyBowEvent.__init__(self, index, state)
        self.click_count = click_count
        self.long_press = long_press