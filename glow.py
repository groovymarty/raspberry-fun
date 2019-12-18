from christmastree import ChristmasTree
from time import sleep
import random

tree = ChristmasTree(pwm=True)

try:
    leds = tree.leds
    for led in leds:
        led.pulse()
        sleep(random.uniform(0, 3))
    while True:
        sleep(.2)
except:
    tree.close()
