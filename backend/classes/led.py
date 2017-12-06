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
        self.update()

    def setPwm(self, state):
        """Enable or disable PWM on the pin"""
        if state:
            if self.pwm:
                return self.get()
            self.pwm = GPIO.PWM(self.id_, 50)
            if self.state == GPIO.HIGH:
                self.pwm.start(100)
            else:
                self.pwm.start(0)
        else:
            if not self.pwm:
                return self.get()
            self.pwm.stop()
            self.pwm = False
        return self.get()

    def on(self):
        """Turn LED on"""
        if self.state == GPIO.HIGH:
            return self.get()

        self.state = GPIO.HIGH
        return self.update()

    def off(self):
        """Turn LED off"""
        if self.state == GPIO.LOW:
            return self.get()

        self.state = GPIO.LOW
        return self.update()

    def toggle(self):
        """Set LED to opposite state"""
        if self.state == GPIO.LOW:
            self.state = GPIO.HIGH
        else:
            self.state = GPIO.LOW
        return self.update()

    def blink(self, duration=.5):
        """Blink a LED"""
        self.toggle()
        time.sleep(duration)
        return self.toggle()

    def _pwmOn(self):
        for dc in range(0, 101, 5):
            self.pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)

    def _pwmOff(self):
        for dc in range(100, -1, -5):
            self.pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)

    def get(self):
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

    def update(self):
        """Update the LED according to state"""
        if self.pwm:
            if self.state == GPIO.HIGH:
                thread = threading.Thread(target=self._pwmOn, args=())
                thread.start()
            elif self.state == GPIO.LOW:
                thread = threading.Thread(target=self._pwmOff, args=())
                thread.start()
        else:
            GPIO.output(self.id_, self.state)

        return self.get()
