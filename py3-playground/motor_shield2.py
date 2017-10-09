import RPi.GPIO as IO
import time
from enum import Enum

from shift_register import ShiftRegister 

class Motors(Enum):
    M1 = 1
    M2 = 2
    M3 = 3
    M4 = 4

class Direction(Enum):
    FORWARD = 1
    BACKWARD = 2
    RELEASE = 3


class DCMotor:

    _pwm = None
    _direction = Direction.RELEASE
    _enc = {Direction.RELEASE : 0}

    def __init__(self, wire, forward=0, backword=0):
        self._pwm = IO.PWM(wire, self._PWM_FREQ)
        self._pwm.start(0)

        self._enc[Direction.FORWARD] = forward
        self._enc[Direction.BACKWARD] = backword


    def setSpeed(self, speed):
        self._pwm.ChangeDutyCycle(speed)

    def setDirection(self, direction):
        self._direction = direction

    def getDirectionEncoding(self):
        return self._enc[self._direction]


class MotorShield:
    _t = 0.01
    _PWM_FREQ = 50
    _hc595 = ShiftRegister()
    _motors = {}

    def __init__(self, t=0.01):
        IO.setmode (IO.BCM)
        self._t = t

    def wireDirection(self, data, clock, latch, reset):
        self._hc595.wire(data, clock, latch, reset)

    def wireDCMotors(self, pwm2A=None, pwm2B=None, pwm0A=None, pwm0B=None):    
        if pwm2A:
            self.motors[Motors.M1] = DCMotor(pwm2A, forward=4, reverse=8)

        if pwm2B:
            self.motors[Motors.M2] = DCMotor(pwm2B, forward=2, reverse=16)

        if pwm0A:
            self.motors[Motors.M3] = DCMotor(pwm0A, forward=1, reverse=64)
    
        if pwm0B:
            self.motors[Motors.M4] = DCMotor(pwm0B, forward=32, reverse=128)


    def wireServos(self, pwm1A, pwm1B):
        print("Not implemented")


    def setSpeed(self, speed, *motors):
        for which in motors:
            self._motors[which].setSpeed(speed)


    def run(self, direction=Direction.RELEASE, *motors):

        for which in self._motors:

            if which in motors 
                self._motors[which].setDirection(direction)

            no += self.motors[which].getDirectionEncoding()

        self._hc595.out(no)



