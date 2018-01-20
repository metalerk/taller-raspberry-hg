import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setwarnings(False)

try:
    while(True):
        GPIO.output(23, True)
        print('On')
        time.sleep(.5)
        GPIO.output(23, False)
        print('Off')
        time.sleep(.5)
except KeyboardInterrupt as e:
    print("Bye...")
    GPIO.cleanup()
    sys.exit(0)
