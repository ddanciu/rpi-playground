from gpiozero import PWMLED
from gpiozero import LED
from time import sleep

w = LED(16)

while True:
    print("off")
    w.off()
    sleep(1)

    print("on")
    w.on()
    sleep(10)