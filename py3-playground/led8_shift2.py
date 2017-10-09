import RPi.GPIO as IO         # calling for header file which helps us use GPIO’s of PI
import time                             # calling for time to provide delays in program
from shift_register import ShiftRegister 
import itertools

IO.setwarnings(False)


data=16
clock=20
latch=21
reset=12

hc595 = ShiftRegister()
hc595.wire(data, clock, latch, reset)

while 1:                               # execute loop forever

    for p in itertools.chain(range(1, 7), range(7, 1, -1)):
        no=2**p + 2**(p-1)
        hc595.out(no)

        print("Done: " + str(no))
        time.sleep(0.05)

        
