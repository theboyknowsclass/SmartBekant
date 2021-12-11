import threading

import zope.event
import zope.event.classhandler

from smartbekant.keyboard.ClickEvent import ClickEvent
from smartbekant.keyboard.KeyBowEvent import KeyBowEvent


class ClickManager:
    def __init__(self, double_click_threshold=0.3, long_press_threshold=0.75, verbose=False):
        self.double_click_threshold = double_click_threshold
        self.long_press_threshold = long_press_threshold
        self.currentClickCount = 1
        self.clickThread = None
        self.releaseThread = None
        self.isLongPress = False
        self.verbose = verbose
        zope.event.classhandler.handler(KeyBowEvent, self.handle_key_event)

    def click_detected(self):
        if self.releaseThread is not None:
            self.releaseThread.join()
        if self.verbose:
            print(f'Number of Clicks: {self.currentClickCount} - Long Press: {self.isLongPress}')
        event = ClickEvent(self.currentClickCount, self.isLongPress)
        zope.event.notify(event)
        self.clickThread = None

    def long_press_detected(self):
        self.isLongPress = True
        self.releaseThread = None

    def handle_key_event(self, keybow_event: KeyBowEvent):
        if keybow_event.index < 2:
            return
        if keybow_event.state:
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
            if self.releaseThread is not None:
                self.releaseThread.cancel()
