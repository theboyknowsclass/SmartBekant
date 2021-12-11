import time

from gpiozero import Buzzer


class BuzzerController:
    def __init__(self, gpio: int):
        self.__bz__ = Buzzer(gpio)
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


if __name__ == "__main__":
    print(__name__)
    buzzer = BuzzerController(26)
    buzzer.short_beep(3)
