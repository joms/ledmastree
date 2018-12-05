"""LED controller class binding up LEDs with the API and extra functionality"""
from RPi import GPIO
from .led import Led
from .patterns.controller import Controller as Patterns
from .twitter.twitter import Twitter
from .kafka.kafka import Kafka
import time

LEDS = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]


class Controller:
    """LED controller class"""
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.leds = dict()
        self.pwm = False

        for led_ in LEDS:
            self.leds[led_] = Led(led_, self.pwm)
            
        self.set_pwm_leds("on")
        for key, item_ in self.leds.items():
            item_.led_on()
            time.sleep(0.05)


        self.patterns = Patterns(self.leds)
        self.twitter = Twitter(self.leds)
        self.kafka = Kafka(self.leds)

    def toggle_all(self):
        """Toggle all LEDs"""
        for key, item_ in self.leds.items():
            item_.led_toggle()
        return self.get_all()

    def toggle(self, id_):
        """Toggle a single LED"""
        if id_ in self.leds:
            return self.leds[id_].toggle()

        return False

    def on_all(self):
        """Set all LEDs to on"""
        for key, item_ in self.leds.items():
            item_.led_on()
        return self.get_all()

    def on_led(self, id_):
        """Set a single LED to on"""
        if id_ in self.leds:
            return self.leds[id_].led_on()

        return False

    def off_all(self):
        """Set all LEDs to off"""
        for key, item_ in self.leds.items():
            item_.led_off()
        return self.get_all()

    def off(self, id_):
        """Set a single LED to off"""
        if id_ in self.leds:
            return self.leds[id_].led_off()

        return False

    def set_pwm_leds(self, state):
        """Set PWM state of all LEDs"""
        _s = state == 'on'
        if _s:
            if self.pwm:
                return self.get_all()
            for key, item_ in self.leds.items():
                item_.set_pwm(_s)
        else:
            if not self.pwm:
                return self.get_all()
            for key, item_ in self.leds.items():
                item_.set_pwm(_s)

        self.pwm = _s
        return self.get_all()

    def get_patterns(self):
        """Get all available patterns"""
        return self.patterns.patterns.get_patterns()

    def set_pattern(self, pattern_id, command):
        """Set status of a pattern"""
        if command == 'on':
            self.patterns.start(pattern_id)
        else:
            self.patterns.stop()

    def set_twitter(self, state):
        if state == 'on':
            self.twitter.start_stream()
        else:
            self.twitter.stop_stream()

    def set_kafka(self, state):
        if state == 'on':
            self.kafka.start_kafka()
        else:
            self.kafka.stop_kafka()

    def get_all(self):
        """Get status about all LEDs"""
        data = []
        for key, item_ in self.leds.items():
            data.append(item_.get_status())
        return data

    def get(self, id_):
        """Get status about a single LED"""
        if id_ in self.leds:
            return self.leds[id_].get_status()

        return False
