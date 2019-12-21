#!/usr/bin/python
import RPi.GPIO as GPIO
import time

LEDGPIOPin_Gruen = 4
LEDGPIOPin_Rot = 9
LEDGPIOPin_Gelb = 22
LEDGPIOPin_BUZZ = 8
LEDGPIOPin_BUTTON = 7

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LEDGPIOPin_Gruen, GPIO.OUT)
GPIO.setup(LEDGPIOPin_Gelb, GPIO.OUT)
GPIO.setup(LEDGPIOPin_Rot, GPIO.OUT)

GPIO.setup(LEDGPIOPin_BUZZ, GPIO.OUT)

GPIO.setup(LEDGPIOPin_BUTTON, GPIO.IN)

GPIO.output(LEDGPIOPin_Rot, GPIO.LOW)
GPIO.output(LEDGPIOPin_Gruen, GPIO.LOW)
GPIO.output(LEDGPIOPin_Gelb, GPIO.LOW)

DELAYON = 1.0 
DELAYBUZZ = 0.1

while True:
    if (GPIO.input(LEDGPIOPin_BUTTON) == True):
        GPIO.output(LEDGPIOPin_Rot, GPIO.HIGH)
        i = 1
        while i < 30:
            GPIO.output(LEDGPIOPin_BUZZ, GPIO.HIGH)
            time.sleep(DELAYBUZZ)
            GPIO.output(LEDGPIOPin_BUZZ, GPIO.LOW)
            time.sleep(DELAYBUZZ)

            if (i == 10):
                GPIO.output(LEDGPIOPin_Gelb, GPIO.HIGH)
            if (i == 20):
                                GPIO.output(LEDGPIOPin_Gruen, GPIO.HIGH)
            i += 1
    else:
        GPIO.output(LEDGPIOPin_Rot, GPIO.LOW)
        GPIO.output(LEDGPIOPin_Gruen, GPIO.LOW)
        GPIO.output(LEDGPIOPin_Gelb, GPIO.LOW)