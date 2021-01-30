from gpiozero import DistanceSensor

class DistanceSensorProxy:
    def __init__(self, echo_pin: int, trigger_pin: int):
        self.__sensor__ = DistanceSensor(echo=echo_pin, trigger=trigger_pin, max_distance=3)

    def get_distance(self):
        return round(self.__sensor__.distance * 100, 1)
    