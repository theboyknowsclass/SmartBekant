import time

from smartbekant.buzzer.BuzzerController import BuzzerController
from smartbekant.data.ConfigurationManager import ConfigurationManager
from smartbekant.data.MemoryManager import MemoryManager
from smartbekant.desk_driver.DeskDriverProxy import DeskDriverProxy
from smartbekant.display.DisplayController import DisplayController
from smartbekant.distance_sensor.DistanceSensorProxy import DistanceSensorProxy


class SmartBekant:
    def __init__(self, height_tolerance=1.0, polling_interval=0.1):
        self.height_tolerance = height_tolerance
        self.polling_interval = polling_interval

        self.config = ConfigurationManager()
        self.buzzer = BuzzerController(self.config.buzzer_gpio)
        self.desk_driver = DeskDriverProxy(self.config.up_gpio, self.config.down_gpio)
        self.display = DisplayController(self.config.display_clock_gpio, self.config.display_data_gpio)
        self.height_sensor = DistanceSensorProxy(self.config.distance_sensor_echo_pin,
                                                 self.config.distance_sensor_trigger_pin)
        self.memory_manager = MemoryManager()

    def set_height(self, height: float):
        current_height = self.height_sensor.get_distance()
        if abs(current_height - height) < self.height_tolerance:
            return
        elif current_height > height:
            self.desk_driver.down()
            while current_height > height:
                current_height = self.height_sensor.get_distance()
                self.display.show(current_height)
                time.sleep(self.polling_interval)
            self.desk_driver.stop()
        else:
            self.desk_driver.up()
            while current_height < height:
                current_height = self.height_sensor.get_distance()
                self.display.show(current_height)
                time.sleep(self.polling_interval)
            self.desk_driver.stop()

    def set_height_from_memory(self, memory_location: int):
        self.buzzer.short_beep(memory_location)
        target_height = self.memory_manager.get_memory(memory_location)
        self.set_height(target_height)
        return

    def update_memory(self, memory_location: int):
        self.buzzer.long_beep()
        current_height = self.height_sensor.get_distance()
        self.memory_manager.set_memory(memory_location, current_height)
        return

    def start(self):
        self.buzzer.short_beep(3)
        while True:
            distance = self.height_sensor.get_distance()
            self.display.show(distance)
            time.sleep(0.3)
