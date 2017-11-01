from gpiozero import Motor
from gpiozero import PWMLED


class Motors:
    MotorA = 1
    MotorB = 2


class L298NShield:

    _enable = {}
    _motors = {}

    def wireMotor(self, which = None, enable = None, inF = None, inB = None):
        self._enable[which] = PWMLED(enable)
        self._motors[which] = Motor(forward=inF, backward=inB)

    def setSpeed(self, speed, *motors):
        for motor in motors:
            self._enable[motor].value = speed
    
    def forward(self, *motors):
        for motor in motors:
            self._motors[motor].forward()

    def backward(self, *motors):
        for motor in motors:
            self._motors[motor].backward()

    def stop(self, *motors):
        for motor in motors:
            self._motors[motor].stop()


class Tank:

    _l298n = L298NShield() 

    def __init__(self, enA, in1, in2, enB, in3, in4):
        self._l298n.wireMotor(Motors.MotorA, enA, in1, in2)
        self._l298n.wireMotor(Motors.MotorB, enB, in3, in4)

    def forward(self, speed):
        self._l298n.setSpeed(speed, Motors.MotorA, Motors.MotorB)
        self._l298n.forward(Motors.MotorA, Motors.MotorB)
        
    def backward(self, speed):
        self._l298n.setSpeed(speed, Motors.MotorA, Motors.MotorB)
        self._l298n.backward(Motors.MotorA, Motors.MotorB)

    def left(self, speed):
        self._l298n.setSpeed(speed, Motors.MotorA, Motors.MotorB)
        self._l298n.forward(Motors.MotorA)
        self._l298n.stop(Motors.MotorB)

    def right(self, speed):
        self._l298n.setSpeed(speed, Motors.MotorA, Motors.MotorB)
        self._l298n.forward(Motors.MotorB)
        self._l298n.stop(Motors.MotorA)

    def spinRight(self, speed):
        self._l298n.setSpeed(speed, Motors.MotorA, Motors.MotorB)
        self._l298n.forward(Motors.MotorB)
        self._l298n.backward(Motors.MotorA)

    def spinLeft(self, speed):
        self._l298n.setSpeed(speed, Motors.MotorA, Motors.MotorB)
        self._l298n.forward(Motors.MotorB)
        self._l298n.backward(Motors.MotorA)

