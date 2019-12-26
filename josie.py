from snowman import Snowman
from time import sleep
import random

man = Snowman()

try:
    leds = man.body.left.leds + man.body.right.leds
    count = 0
    while True:
        man.face.nose.value = count & 2
        man.face.leftEye.value = count & 4
        man.face.rightEye.value = count & 8
        n = len(leds)
        i = random.randint(0, n-1)
        leds[i].toggle()
        count += 1
        sleep(.1)
except Exception as e:
    man.close()
    raise e
