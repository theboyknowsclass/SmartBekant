import busio as io
import adafruit_ht16k33.segments
import math

class DisplayProxy:
    def __init__(self, scl_pin, sda_pin):
        self.__i2c__ = io.I2C(scl_pin, sda_pin)   
        self.__display__ = adafruit_ht16k33.segments.Seg7x4(self.__i2c__)
        self.__display__.fill(0)

    def show(self, value: float):
        string = str(round(value,1))
        print(string)
        self.__display__.print(string)
        self.__display__.show()


if __name__ == "__main__":
    print(__name__)
    display = DisplayProxy(3, 2)
    display.show(222.2)