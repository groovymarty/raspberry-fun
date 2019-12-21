from christmastree import ChristmasTree
from time import sleep
import random

tree = ChristmasTree()

try:
    leds = tree.leds
    while True:
        n = len(leds)
        i = random.randint(0, n-1)
        leds[i].toggle()
        sleep(.2)
except Exception as e:
    tree.close()
    raise e
