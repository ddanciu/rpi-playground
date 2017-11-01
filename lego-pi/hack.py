from gpiozero import PWMLED
from gpiozero import LED
from gpiozero import Motor

from time import sleep

w16 = PWMLED(16)
m = Motor(forward=20, backward=21)

while True:
    print("C")
    w16.value = 1
    m.forward()
    sleep(1)

    print("off")
    w16.value = 0
    sleep(1)

    print("CC")
    w16.value = 1
    m.backward()
    sleep(1)

    print("off")
    w16.value = 0
    sleep(1)
