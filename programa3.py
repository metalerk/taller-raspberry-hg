import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(24, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setwarnings(False)


while(True):
    if(GPIO.input(14) == GPIO.HIGH):
        GPIO.output(23, True)
    else:
        GPIO.output(23, False)
    if (GPIO.input(15) == GPIO.HIGH):
        GPIO.output(24, True)
    else:
        GPIO.output(24, False)

GPIO.cleanup()
