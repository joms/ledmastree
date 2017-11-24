from signal import pause
from gpiozero import LEDBoard
from gpiozero.tools import random_values

TREE = LEDBoard(*range(2, 28), pwm=True)
for led in TREE:
    led.source_delay = 1
    led.source = random_values()
pause()
