from gpiozero import OutputDevice

class DeskDriverProxy:
    def __init__(self, up_pin, down_pin):
        self.__up_driver__ = OutputDevice(up_pin)
        self.__down_driver__ = OutputDevice(down_pin)

    def stop(self):
        self.__up_driver__.off()
        self.__down_driver__.off()

    def up(self):
        self.stop()
        self.__up_driver__.on()

    def down(self):
        self.stop()
        self.__down_driver__.on()
