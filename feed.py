#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def feed():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)

    try:
        servo = GPIO.PWM(18,50)
        servo.start(12.5)

        time.sleep(0.8)
    
    finally:
        if servo:
            servo.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    feed()
    