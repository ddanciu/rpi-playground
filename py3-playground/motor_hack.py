import RPi.GPIO as IO         # calling for header file which helps us use GPIO’s of PI
import time                             # calling for time to provide delays in program
from shift_register import ShiftRegister 
import itertools

IO.setwarnings(False)

IO.setmode(IO.BCM)
IO.setup(13, IO.OUT)

data=16
clock=20
latch=21
reset=12

hc595 = ShiftRegister()
hc595.wire(data, clock, latch, reset)

dc=0
p = IO.PWM(13, 50)
p.start(0)
while 1:                               # execute loop forever

    dc += 33
    dc = dc % 100
    p.ChangeDutyCycle(dc)
    print("Speed " + str(dc))
    
    for no in [8]:
        
        hc595.out(no)

        print("Done: " + str(no))
        time.sleep(5)

    
    
