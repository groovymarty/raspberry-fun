from christmastree import ChristmasTree
from time import sleep
import random

tree = ChristmasTree(pwm=True)

try:
    leds = tree.leds
    while True:
        for led in leds:
            led.off()
            sleep(random.uniform(0, 3))
            led.pulse()
except:
    tree.close()
