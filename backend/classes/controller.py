from RPi import GPIO
from .led import Led

LEDS = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

class Controller:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.leds = dict()

        for led_ in LEDS:
            self.leds[led_] = Led(led_)

    def toggle_all(self):
        for key, item_ in self.leds.items():
            item_.toggle()
        return self.get_all()

    def toggle(self, id_):
        if id_ in self.leds:
            return self.leds[id_].toggle()

        return False

    def on_all(self):
        for key, item_ in self.leds.items():
            item_.on()
        return self.get_all()

    def on(self, id_):
        if id_ in self.leds:
            return self.leds[id_].on()

        return False

    def off_all(self):
        for key, item_ in self.leds.items():
            item_.off()
        return self.get_all()

    def off(self, id_):
        if id_ in self.leds:
            return self.leds[id_].off()

        return False

    def get_all(self):
        data = []
        for key, item_ in self.leds.items():
            data.append(item_.get())
        return data

    def get(self, id_):
        if id_ in self.leds:
            return self.leds[id_].get()

        return False
