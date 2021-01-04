from gpiozero import Buzzer
import time

class BuzzerProxy:
    def __init__(self, on_pin: int):
        self.bz = Buzzer(on_pin)
        self.bz.off()

    def short_beep(self, times: int):
        for x in range(0, times):
            self.bz.on()
            time.sleep(0.05)
            self.bz.off()
            time.sleep(0.09)

    def long_beep(self):
        self.bz.on()
        time.sleep(0.3)
        self.bz.off()
