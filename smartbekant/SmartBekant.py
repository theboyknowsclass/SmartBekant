from .buzzer.BuzzerController import BuzzerController
from .desk_driver.DeskDriverProxy import DeskDriverProxy
from .display.DisplayProxy import DisplayProxy
from .distance_sensor.DistanceSensorProxy import DistanceSensorProxy
import time

buzzer_gpio = 27

up_gpio = 1
down_gpio = 2

display_clock_gpio = 3
display_data_gpio = 2

distance_sensor_echo_pin = 15
distance_sensor_trigger_pin = 14

height_tolerance = 1.0
polling_interval = 0.1

buzzer = BuzzerController(buzzer_gpio)
desk_driver = DeskDriverProxy(up_gpio, down_gpio)
display = DisplayProxy(display_clock_gpio, display_data_gpio)
height_sensor = DistanceSensorProxy(distance_sensor_echo_pin, distance_sensor_trigger_pin)


def set_height(height: float):
    current_height = height_sensor.get_distance()

    if abs(current_height-height) < height_tolerance:
        return
    elif current_height > height:
        desk_driver.down()
        while current_height > height:
            current_height = height_sensor.get_distance()
            display.show(current_height)
            time.sleep(polling_interval)
        desk_driver.stop()
    else:
        desk_driver.up()
        while current_height < height:
            current_height = height_sensor.get_distance()
            display.show(current_height)
            time.sleep(polling_interval)
        desk_driver.stop()

def set_height_from_memory(memory_location: int):
    buzzer.short_beep(memory_location)
    return

def update_memory(memory_location: int):
    buzzer.long_beep()
    return