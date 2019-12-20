#SnowPi Test Code

import random

import time

from gpiozero import LED

#Setup all the LEDs

 

led7 = LED(7)

led8 = LED(8)

led9 = LED(9)

led17 = LED(17)

led18 = LED(18)

led22 = LED(22)

led23 = LED(23)

led24 = LED(24)

led25 = LED(25)

 

led7.off()

 

led8.off()

 

led9.off()

 

led17.off()

 

led18.off()

 

led22.off()

 

led23.off()

 

led24.off()

 

led25.off()

 

while True:

    led7.toggle()

    time.sleep(1)

    led8.toggle()

    time.sleep(1)

    led9.toggle()

    time.sleep(1)

    led17.toggle()

    time.sleep(1)

    led18.toggle()

    time.sleep(1)

    led22.toggle()

    time.sleep(1)

    led23.toggle()

    time.sleep(1)

    led24.toggle()

    time.sleep(1)

    led25.toggle()

    time.sleep(1)