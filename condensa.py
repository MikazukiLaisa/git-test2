import wiringpi
import RPi.GPIO as GPIO

import time

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(23, 1)

t1 = time.time()
wiringpi.digitalWrite(23, 1)
#while wiringpi.digitalRead(25)!= 1:
    #pass

while wiringpi.digitalRead(24)!= 1:
    pass

t2 = time.time()

print(t2 - t1)

wiringpi.digitalWrite(23, 0)
time.sleep(1)


