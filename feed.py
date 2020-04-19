#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def feed():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)

    try:
	freq = 100.0
        servo = GPIO.PWM(18, freq)
	sleep_time = 0.85

        servo.start(20)
        time.sleep(sleep_time)

    finally:
        if servo:
            servo.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    feed()

