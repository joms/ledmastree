"""LED wrapper class"""
import threading
import time
from RPi import GPIO

class Led:
    """LED wrapper class"""
    def __init__(self, id_, pwm):
        GPIO.setup(id_, GPIO.OUT)

        if pwm:
            self.pwm = GPIO.PWM(id_, 50)
        else:
            self.pwm = pwm

        self.id_ = id_
        self.state = GPIO.LOW
        self.update_status()

    def set_pwm(self, state):
        """Enable or disable PWM on the pin"""
        if state:
            if self.pwm:
                return self.get_status()
            self.pwm = GPIO.PWM(self.id_, 50)
            if self.state == GPIO.HIGH:
                self.pwm.start(100)
            else:
                self.pwm.start(0)
        else:
            if not self.pwm:
                return self.get_status()
            self.pwm.stop()
            self.pwm = False
        return self.get_status()

    def led_on(self):
        """Turn LED on"""
        if self.state == GPIO.HIGH:
            return self.get_status()

        self.state = GPIO.HIGH
        return self.update_status()

    def led_off(self):
        """Turn LED off"""
        if self.state == GPIO.LOW:
            return self.get_status()

        self.state = GPIO.LOW
        return self.update_status()

    def led_toggle(self):
        """Set LED to opposite state"""
        if self.state == GPIO.LOW:
            self.state = GPIO.HIGH
        else:
            self.state = GPIO.LOW
        return self.update_status()

    def led_blink(self, duration=.5):
        """Blink a LED"""
        self.led_toggle()
        time.sleep(duration)
        return self.led_toggle()

    def _pwm_on(self):
        for dc in range(0, 101, 5):
            self.pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)

    def _pwm_off(self):
        for dc in range(100, -1, -5):
            self.pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)

    def get_status(self):
        """Get LED status"""
        if not self.pwm:
            pwm = self.pwm
        else:
            pwm = True

        return {
            'id': self.id_,
            'state': self.state,
            'pwm': pwm
        }

    def update_status(self):
        """Update the LED according to state"""
        if self.pwm:
            if self.state == GPIO.HIGH:
                thread = threading.Thread(target=self._pwm_on, args=())
                thread.start()
            elif self.state == GPIO.LOW:
                thread = threading.Thread(target=self._pwm_off, args=())
                thread.start()
        else:
            GPIO.output(self.id_, self.state)

        return self.get_status()
