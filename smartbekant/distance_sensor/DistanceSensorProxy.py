from gpiozero import DistanceSensor


class DistanceSensorProxy:
    def __init__(self, echo_pin: int, trigger_pin: int):
        self.sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin, max_distance=3)

    def get_distance(self):
        return round(self.sensor.distance * 100, 1)
    