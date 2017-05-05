from gpiozero import Motor, LED
import time

MotorPin1 = 27 # pin11
MotorPin2 = 22 # pin12
MotorEnable = 17 # pin13

enable = LED(MotorEnable)
enable.on()

motor = Motor(MotorPin1, MotorPin2)

print("Forward")
motor.forward(0.2)
time.sleep(1)
motor.forward(0.4)
time.sleep(1)
motor.forward(0.6)
time.sleep(1)
motor.forward(0.8)
time.sleep(1)
motor.forward(1)
time.sleep(1)

print("Backward")
motor.backward()
time.sleep(5)


print("Stop")
motor.stop()
enable.off()
