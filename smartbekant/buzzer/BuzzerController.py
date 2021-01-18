import time
from .BuzzerProxy import BuzzerProxy

class BuzzerController:
    def __init__(self, buzzerGpio: int):
        self.__bz__ = BuzzerProxy(buzzerGpio)
        self.__bz__.off()

    def short_beep(self, times: int):
        x = 0
        while x < times:
            self.__bz__.on()
            time.sleep(0.05)
            self.__bz__.off()
            time.sleep(0.09)
            x += 1

    def long_beep(self):
        self.__bz__.on()
        time.sleep(0.3)
        self.__bz__.off()