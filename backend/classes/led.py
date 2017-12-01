from RPi import GPIO
import time

class Led:
    def __init__(self, id_, pwm):
        GPIO.setup(id_, GPIO.OUT)

        if (pwm):
            self.pwm = GPIO.PWM(id_, 50)
        else:
            self.pwm = pwm

        self.id_ = id_
        self.state = GPIO.LOW
        self.update()

    def setPwm(self, state):
        if (state):
            if (self.pwm):
                return self.get()
            self.pwm = GPIO.PWM(self.id_, 50)
            if (self.state == GPIO.HIGH):
                self.pwm.start(100)
            else:
                self.pwm.start(0)
        else:
            if (not self.pwm):
                return self.get()
            self.pwm.stop()
            self.pwm = False
        return self.get()

    def on(self):
        if self.state == GPIO.HIGH:
            return self.get()

        self.state = GPIO.HIGH
        return self.update()

    def off(self):
        if self.state == GPIO.LOW:
            return self.get()
      
        self.state = GPIO.LOW
        return self.update()

    def toggle(self):
        if self.state == GPIO.LOW:
            self.state = GPIO.HIGH
        else:
            self.state = GPIO.LOW
        return self.update()

    def blink(self, duration = .5):
        self.toggle()
        time.sleep(duration)
        return self.toggle()

    def pwmOn(self):
        self.pwm.start(0)
        for dc in range(0, 101, 5):
            self.pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)

    def pwmOff(self):
        for dc in range(100, -1, -5):
            self.pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)

    def get(self):
        if (not self.pwm):
            pwm = self.pwm
        else:
            pwm = True

        return {
            'id': self.id_,
            'state': self.state,
            'pwm': pwm
        }

    def update(self):
        if (self.pwm):
            if (self.state == GPIO.HIGH):
                self.pwmOn()
            elif (self.state == GPIO.LOW):
                self.pwmOff
        else:
            GPIO.output(self.id_, self.state)

        return self.get()
