from gpiozero import OutputDevice

class DeskDriverProxy:
    def __init__(self, up_pin, down_pin):
        self.up_driver = OutputDevice(up_pin)
        self.down_driver = OutputDevice(down_pin)

    def stop(self):
        self.up_driver.off()
        self.down_driver.off()

    def up(self):
        self.stop()
        self.up_driver.on()

    def down(self):
        self.stop()
        self.down_driver.on()
