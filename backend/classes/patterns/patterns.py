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
        "trigger": "random_flash"
    }, {
        "id": 1,
        "name": "Toggle",
        "description": "Loop over the leds and toggling them in order",
        "parameters": [{
            "name": "speed",
            "type": "int"
        }],
        "trigger": "toggle_pattern"
    }, {
        "id": 2,
        "name": "Toggle One",
        "description": "Loop over the leds and toggling one in order",
        "parameters": [{
            "name": "speed",
            "type": "int"
        }],
        "trigger": "toggle_one_pattern"
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
        "trigger": "sin_tree"
    }
]

class Patterns:
    """Led pattern controller class"""
    def __init__(self, led_list):
        self.led_list = led_list

    def get_pattern(self, id_):
        """Get pattern function by id"""
        return PATTERNLIST[id_]

    def get_patterns(self):
        """Get all patterns"""
        return PATTERNLIST

    def random_flash(self, e, interval):
        """Flash LEDs in a seemingly random sequence"""
        for key, item_ in self.led_list.items():
            item_.on()

        while not e.isSet():
            for key, led in self.led_list.items():
                led.off()
                time.sleep(interval)
                led.on()
                e.wait(interval)

    def toggle_pattern(self, e, speed):
        """Toggle LEDs in sequences"""
        for key, item_ in self.led_list.items():
            item_.on()

        while not e.isSet():
            for key, led in self.led_list.items():
                led.on()
                e.wait(speed)
            for key, led in self.led_list.items():
                led.off()
                e.wait(speed)

    def toggle_one_pattern(self, e, speed):
        """Toggle a single LED"""
        for key, item_ in self.led_list.items():
            item_.off()

        while not e.isSet():
            for key, led in self.led_list.items():
                led.on()
                e.wait(speed)
                led.off()
                e.wait(speed)

    def absint(self, e, freq=1):
        """Run a sine effect over the LEDs with key as parameter"""
        while not e.isSet():
            for key, led in self.led_list.items():
                if led.pwm:
                    #TODO Implement frequency
                    dc = math.fabs(math.sin(time.time() + key) * 100)
                    led.pwm.ChangeDutyCycle(dc)
            e.wait(.01)

    def sin_tree(self, e, freq=1000):
        """Apply a single sine effect to all LEDs"""
        while not e.isSet():
            for key, led in self.led_list.items():
                if led.pwm:
                    dc = math.fabs(math.sin(time.time()) * 100)
                    led.pwm.ChangeDutyCycle(dc)
            e.wait(.01)
