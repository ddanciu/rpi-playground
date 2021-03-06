from l298n_shield import Tank
from l298n_shield import Motors
from l298n_shield import L298NShield

from time import sleep

delay = 2

shield = L298NShield()
shield.wireMotor(Motors.MotorA, enable=13, inF=16, inB=19)
shield.wireMotor(Motors.MotorB, enable=26, inF=20, inB=21)
shield.setSpeed(1, Motors.MotorA, Motors.MotorB)

while True:
    print("Forward full speed")
    shield.forward(Motors.MotorA, Motors.MotorB)
    sleep(delay)

    print("Backward full speed")
    shield.backward(Motors.MotorA, Motors.MotorB)
    sleep(delay)
