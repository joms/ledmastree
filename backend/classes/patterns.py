import threading
import time
from RPi import GPIO
import random

class Patterns:
    def __init__(self, ledList):
        self.ledList = ledList

        e = threading.Event()
        t = threading.Thread(name='non-block', target=self.randomFlash, args=(e, .5))
        t.start()

    def randomFlash(self, e, interval):
        for key, item_ in self.ledList.items():
            item_.on()

        while not e.isSet():
            led = random.choice(list(self.ledList))
            self.ledList[led].off()
            time.sleep(interval)
            self.ledList[led].on()
            if (not e.wait(interval)):
                time.sleep(interval)