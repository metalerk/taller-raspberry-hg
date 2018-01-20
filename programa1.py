import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False)

c14 = 0
c15 = 0

print("""

#################
Push Counter
#################

""")

while(True):
    if (GPIO.input(14) == GPIO.HIGH):
        c14 += 1
        print('###################')
        print('Pulsando el boton 14')
        print('Presionado {} veces'.format(c14))
        time.sleep(.5)
    if (GPIO.input(15) == GPIO.HIGH):
        c15 += 1
        print('###################')
        print('Pulsando el boton 15')
        print('Presionado {} veces'.format(c15))
        time.sleep(.5)

GPIO.cleanup()
