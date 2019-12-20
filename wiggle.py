from snowman import Snowman
from time import sleep
import random

man = Snowman()

try:
    man.face.nose.on()
    count = 0
    while True:
        man.face.leftEye.value = (count & 1)
        man.face.rightEye.value = not (count & 1)
        for led in man.body.left:
            led.value = (count & 2)
        for led in man.body.right:
            led.value = not (count & 2)
        count += 1
        sleep(.1)
except:
    man.close()
