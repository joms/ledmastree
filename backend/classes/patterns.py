import threading
import time
import math
from RPi import GPIO

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
    }, {
        "id": 3,
        "name": "Absint",
        "description": "Apply a random sine effect to all PWM enabled LEDs",
        "parameters": [{
            "name": "frequence",
            "type": "float"
        }],
        "trigger": "absint"
    }, {
        "id": 4,
        "name": "sinTree",
        "description": "Apply an even sine effect to all PWM enabled LEDs",
        "parameters": [{
            "name": "frequence",
            "type": "float"
        }],
        "trigger": "sinTree"
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

    def absint(self, e, freq = 1):
        while not e.isSet():
            for key, led in self.ledList.items():
                if (led.pwm):
                    #TODO Implement frequency
                    dc = math.fabs(math.sin(time.time() + key) * 100)
                    led.pwm.ChangeDutyCycle(dc)
            e.wait(.01)

    def sinTree(self, e, freq = 1000):
        while not e.isSet():
            for key, led in self.ledList.items():
                if (led.pwm):
                    dc = math.fabs(math.sin(time.time()) * 100)
                    led.pwm.ChangeDutyCycle(dc)
            e.wait(.01)

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
