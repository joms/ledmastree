from RPi import GPIO

class Led:
    def __init__(self, id_):
        GPIO.setup(id_, GPIO.OUT)

        self.id_ = id_
        self.state = GPIO.LOW
        self.update()

    def on(self):
        self.state = GPIO.HIGH
        return self.update()

    def off(self):
        self.state = GPIO.LOW
        return self.update()

    def toggle(self):
        if self.state == GPIO.LOW:
            self.state = GPIO.HIGH
        else:
            self.state = GPIO.LOW
        return self.update()

    def get(self):
        return {
            'id': self.id_,
            'state': self.state
        }

    def update(self):
        GPIO.output(self.id_, self.state)
        return self.get()
