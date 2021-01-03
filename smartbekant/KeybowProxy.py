import keybow
import threading



class KeybowProxy:
    def __init__(self, background = [0, 0, 0], up_colour = [0, 255, 0], down_colour = [255, 0, 0], memory_colour = [0, 0, 255], double_click_threshold = 0.3, long_press_threshold = 0.75):
        self.background = background
        self.up_colour = up_colour
        self.down_colour = down_colour
        self.memory_colour = memory_colour
        self.double_click_threshold = double_click_threshold
        self.long_press_threshold = long_press_threshold
        self.currentClickCount = 1
        self.clickThread = None
        self.releaseThread = None
        self.isLongPress = False

        keybow.setup(keybow.MINI)

        self.r, self.g, self.b = background
        keybow.set_all(self.r, self.g, self.b)
        keybow.show()