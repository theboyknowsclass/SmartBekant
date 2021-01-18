from gpiozero import Buzzer

class BuzzerProxy:
    def __init__(self, buzzerGpio: int):
        self.__bz__ = Buzzer(buzzerGpio)
        self.__bz__.off()

    def on(self):
        self.__bz__.on()

    def off(self):
        self.__bz__.off()
