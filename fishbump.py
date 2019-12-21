from fishdish import FishDish
from time import sleep

fish = FishDish()

pattern = 1
def bump_pattern():
    global pattern
    pattern += 1
    fish.buzzer.beep(.05,0,1)

try:
    fish.button.when_pressed = bump_pattern
    while True:
        bit = 1
        for led in fish.leds:
            if pattern & bit:
                led.toggle()
            bit = bit << 1
        sleep(.5)
except Exception as e:
    fish.close()
    raise e
