import busio as io
import adafruit_ht16k33.segments
import math

class DisplayProxy:
    def __init__(self, scl_pin, sda_pin):
        self.i2c = io.I2C(scl_pin, sda_pin)   
        self.display = adafruit_ht16k33.segments.Seg7x4(self.i2c)
        self.display.fill(0)

    def show(self, value: float):
        value_tuple = math.modf(value)
        string = str(int(value_tuple[1])).zfill(3) + '.{:.0f}'.format(value_tuple[0])
        self.display.print(string)
        self.display.show()




