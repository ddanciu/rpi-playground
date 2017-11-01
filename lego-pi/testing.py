from l298n_shield import Tank

from time import sleep

delay = 2

tank = Tank(enA=13, in1=19, in2=26, enB=16, in3=20, in4=21)

while True:
    print("Forward full speed")
    tank.forward(1)
    sleep(delay)

    print("Left full speed")
    tank.left(1)
    sleep(delay)
    
    print("Right full speed")
    tank.right(1)
    sleep(delay)

    print("Backward full speed")
    tank.backward(1)
    sleep(delay)
