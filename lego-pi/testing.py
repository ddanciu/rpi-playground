from l298n_shield import Tank

from time import sleep

delay = 2

tank = Tank(13, 19, 26, 16, 20, 21)

while True:
    tank.forward(1)
    sleep(delay)
    led.backward(1)
    sleep(delay)
