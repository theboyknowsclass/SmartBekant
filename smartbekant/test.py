#!/usr/bin/env python
import keybow
import threading
import time
import subprocess
from gpiozero import LED
from gpiozero import Buzzer
from gpiozero import DistanceSensor
import board
import busio as io
import adafruit_ht16k33.segments
from decimal import Decimal
import math


background = [255, 100, 100]
doubleClickThreshold = 0.3
longPressThreshold = 0.75

currentClickCount = 1
clickThread = None
releaseThread = None
isLongPress = False

r,g,b = background

keybow.setup(keybow.MINI)
keybow.set_all(r, g, b)
keybow.show()

bz = Buzzer(27)
bz.off()

i2c = io.I2C(board.SCL, board.SDA)
display = adafruit_ht16k33.segments.Seg7x4(i2c)
display.fill(0)

sensor = DistanceSensor(echo=15, trigger=14, max_distance=3)

@keybow.on(index=0)
def handle_key(index, state):
   
    if state:
        keybow.set_led(index, 255, 50, 50)
        keybow.show()
    else:
        keybow.set_led(index, r, g, b)
        keybow.show()

@keybow.on(index=1)
def handle_key(index, state):
    if state:
        keybow.set_led(index, 50, 255, 50)
        keybow.show()

    else:
        keybow.set_led(index, r, g, b)
        keybow.show()


@keybow.on(index=2)
def handle_key(index, state):
    global doubleClickThreshold
    global longPressThreshold
    global currentClickCount
    global clickThread
    global releaseThread
    global isLongPress
    
    if state:
        keybow.set_led(index, 255, 50, 255)
        keybow.show
        isLongPress = False
        if clickThread is None:
            currentClickCount = 1
            clickThread = threading.Timer(doubleClickThreshold, handleClick)
            clickThread.start()
        else:
            clickThread.cancel()
            currentClickCount += 1
            clickThread = threading.Timer(doubleClickThreshold, handleClick)
            clickThread.start()
            
        if releaseThread is None:
            releaseThread = threading.Timer(longPressThreshold, longPressDetected)
            releaseThread.start()
        else:
            releaseThread.cancel()
            releaseThread = threading.Timer(longPressThreshold, longPressDetected)
            releaseThread.start()
    else:
        keybow.set_led(index, r, g, b)
        keybow.show()
        releaseThread.cancel()


def handleClick():
    global currentClickCount
    global clickThread
    global releaseThread
    global isLongPress
    if releaseThread is not None:
        releaseThread.join()
    print(f'Number of Clicks: {currentClickCount} - Long Press: {isLongPress}')
          
    if isLongPress:
        bz.on()
        time.sleep(0.3)
        bz.off()
    else:
        for x in range(0, currentClickCount):
            bz.on()
            time.sleep(0.05)
            bz.off()
            time.sleep(0.09)
    clickThread = None
    
    
def longPressDetected():
    global isLongPress
    isLongPress = True
    releaseThread = None
    
while True:
    distance = math.modf(round(sensor.distance * 100, 1))
    distanceString = str(int(distance[1])).zfill(3) + '.{:.0f}'.format(distance[0])
    print(f'Num: {distanceString}')
    display.print(distanceString)
    display.show()
    time.sleep(0.3)

