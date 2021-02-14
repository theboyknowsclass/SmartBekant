import zope.event
import threading
from ClickEvent import ClickEvent

class ClickManager:
    def __init__(self, double_click_threshold = 0.3, long_press_threshold = 0.75):
        self.double_click_threshold = double_click_threshold
        self.long_press_threshold = long_press_threshold
        self.currentClickCount = 1
        self.clickThread = None
        self.releaseThread = None
        self.isLongPress = False
        

    def click_detected(self):
        if self.releaseThread is not None:
            self.releaseThread.join()
        print(f'Number of Clicks: {self.currentClickCount} - Long Press: {self.isLongPress}')
        event = ClickEvent(self.currentClickCount, self.isLongPress)
        zope.event.notify(event)
        self.clickThread = None
    
    def long_press_detected(self):
        self.isLongPress = True
        self.releaseThread = None

    def handle_key_event(self, state):
        if state:
            self.isLongPress = False
            if self.clickThread is None:
                self.currentClickCount = 1
                self.clickThread = threading.Timer(self.double_click_threshold, self.click_detected)
                self.clickThread.start()
            else:
                self.clickThread.cancel()
                self.currentClickCount += 1
                self.clickThread = threading.Timer(self.double_click_threshold, self.click_detected)
                self.clickThread.start()
                
            if self.releaseThread is None:
                self.releaseThread = threading.Timer(self.long_press_threshold, self.long_press_detected)
                self.releaseThread.start()
            else:
                self.releaseThread.cancel()
                self.releaseThread = threading.Timer(self.long_press_threshold, self.long_press_detected)
                self.releaseThread.start()
        else:
            self.releaseThread.cancel()
