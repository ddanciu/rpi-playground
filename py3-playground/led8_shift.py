import RPi.GPIO as IO         # calling for header file which helps us use GPIO’s of PI
import time                             # calling for time to provide delays in program

IO.setwarnings(False)

IO.setmode (IO.BCM)        # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)

data=16
clock=20
latch=21
reset=12

t=0.05

IO.setup(data,IO.OUT)            # initialize GPIO Pins as an output.
IO.setup(clock,IO.OUT)
IO.setup(latch,IO.OUT)
IO.setup(reset,IO.OUT)



while 1:                               # execute loop forever

    for no in [1, 2, 4, 8, 16, 32, 64, 128]:
        IO.output(reset, 0)    
        time.sleep(t)          
        IO.output(reset, 1)         
        time.sleep(t)        
        
        for y in [int(x) for x in bin(no)[2:]]:            # loop for counting up 8 times
            IO.output(data, y)            # pull up the data pin for every bit.
            time.sleep(t)            # wait for 100ms
            IO.output(clock,1)            # pull CLOCK pin high
            time.sleep(t)
            IO.output(clock,0)            # pull CLOCK pin down, to send a rising edge

        time.sleep(t)
        #IO.output(data,0)            # clear the DATA pin
        IO.output(latch,1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(t)
        IO.output(latch,0)            # pull down the SHIFT pin

        print("Done: " + str(no))
        time.sleep(1.5)
        
        
        
