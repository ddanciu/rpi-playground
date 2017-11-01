from gpiozero import PWMLED
from gpiozero import LED
from time import sleep

w16 = PWMLED(16)
w20 = LED(20)
w21 = LED(21)

while True:
    print("C")
    w16.value = 1
    w20.on()
    w21.off()
    sleep(1)

    print("off")
    w16.value = 0
    sleep(1)

    print("CC")
    w16.value = 1
    w20.off()
    w21.on()
    sleep(1)

    print("off")
    w16.value = 0
    sleep(1)
