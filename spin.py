from snowman import Snowman
from time import sleep
import random

man = Snowman()

try:
    man.face.nose.on()
    ring = (man.body.right.top,
            man.body.right.middle,
            man.body.right.bottom,
            man.body.left.bottom,
            man.body.left.middle,
            man.body.left.top)
    count = 0
    while True:
        if count == 0:
            for led in man.face:
                led.toggle()
        ring[count].toggle()
        count = (count + 1) % 6
        sleep(.1)
except:
    man.close()
