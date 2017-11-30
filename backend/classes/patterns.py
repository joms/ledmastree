import threading
import time
from RPi import GPIO
import random

PATTERNLIST = [
    {
        "id": 0,
        "name": "Random Flash",
        "description": "Flash random LED",
        "parameters": [{
            "name": "speed",
            "type": "int"
        }],
        "trigger": "randomFlash"
    }, {
        "id": 1,
        "name": "Toggle",
        "description": "Loop over the leds and toggling them in order",
        "parameters": [{
            "name": "speed",
            "type": "int"
        }],
        "trigger": "togglePattern"
    }, {
        "id": 2,
        "name": "Toggle One",
        "description": "Loop over the leds and toggling one in order",
        "parameters": [{
            "name": "speed",
            "type": "int"
        }],
        "trigger": "toggleOnePattern"
    }  
]

class Patterns:
    def __init__(self, ledList):
        self.ledList = ledList

        self.activePattern = False
        self.eventThread = False
        self.thread = False

    def randomFlash(self, e, interval):
        # Apply PWM with a sin function
        for key, item_ in self.ledList.items():
            item_.on()

        while not e.isSet():
            for key, led in self.ledList.items():
                led.off()
                time.sleep(interval)
                led.on()
                e.wait(interval)

    def togglePattern(self, e, speed):
        for key, item_ in self.ledList.items():
            item_.on()

        while not e.isSet():
            for key, led in self.ledList.items():
                led.on()
                e.wait(speed)
            for key, led in self.ledList.items():
                led.off()
                e.wait(speed)

    def toggleOnePattern(self, e, speed):
        for key, item_ in self.ledList.items():
            item_.off()

        while not e.isSet():
            for key, led in self.ledList.items():
                led.on()
                e.wait(speed)
                led.off()
                e.wait(speed)

    def start(self, id_):
        pattern = PATTERNLIST[id_]
        func = getattr(self, pattern["trigger"])

        self.eventThread = threading.Event()
        self.thread = threading.Thread(name='non-block', target=func, args=(self.eventThread, .1))
        self.thread.start()
        
        self.activePattern = pattern
        return self.activePattern
        
    def stop(self):
        if self.eventThread:
            self.eventThread.set()
            self.eventThread = False
            self.thread = False

    def patternList(self):
        return PATTERNLIST
