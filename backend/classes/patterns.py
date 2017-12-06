"""LED pattern controller"""
import threading
import time
import math

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
    """Led pattern class"""
    def __init__(self, ledList):
        self.ledList = ledList

        self.activePattern = False
        self.eventThread = False
        self.thread = False

    def randomFlash(self, e, interval):
        """Flash LEDs in a seemingly random sequence"""
        for key, item_ in self.ledList.items():
            item_.on()

        while not e.isSet():
            for key, led in self.ledList.items():
                led.off()
                time.sleep(interval)
                led.on()
                e.wait(interval)

    def togglePattern(self, e, speed):
        """Toggle LEDs in sequences"""
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
        """Toggle a single LED"""
        for key, item_ in self.ledList.items():
            item_.off()

        while not e.isSet():
            for key, led in self.ledList.items():
                led.on()
                e.wait(speed)
                led.off()
                e.wait(speed)

    def absint(self, e, freq = 1):
        """Run a sine effect over the LEDs with key as parameter"""
        while not e.isSet():
            for key, led in self.ledList.items():
                if led.pwm:
                    #TODO Implement frequency
                    dc = math.fabs(math.sin(time.time() + key) * 100)
                    led.pwm.ChangeDutyCycle(dc)
            e.wait(.01)

    def sinTree(self, e, freq = 1000):
        """Apply a single sine effect to all LEDs"""
        while not e.isSet():
            for key, led in self.ledList.items():
                if led.pwm:
                    dc = math.fabs(math.sin(time.time()) * 100)
                    led.pwm.ChangeDutyCycle(dc)
            e.wait(.01)

    def start(self, id_):
        """Start a pattern"""
        pattern = PATTERNLIST[id_]
        func = getattr(self, pattern["trigger"])

        if self.eventThread:
            self.stop()

        self.eventThread = threading.Event()
        self.thread = threading.Thread(name='non-block', target=func, args=(self.eventThread, .1))
        self.thread.start()

        self.activePattern = pattern
        return self.activePattern

    def stop(self):
        """Stop a pattern"""
        if self.eventThread:
            self.eventThread.set()
            self.eventThread = False
            self.thread = False

    def patternList(self):
        """Get the patternlist"""
        return PATTERNLIST
