import RPi.GPIO as IO
import time


class ShiftRegister:

    _t = 0.01

    def __init__(self, t=0.01):
        IO.setmode (IO.BCM)
        self._t = t

    def wire(self, data, clock, latch, reset):
        self._data = data
        self._clock = clock
        self._latch = latch
        self._reset = reset
        IO.setup(self._data,IO.OUT)            # initialize GPIO Pins as an output.
        IO.setup(self._clock,IO.OUT)
        IO.setup(self._latch,IO.OUT)
        IO.setup(self._reset,IO.OUT)


    def clear(self):
        IO.output(self._reset, 0)    
        time.sleep(self._t)          
        IO.output(self._reset, 1)         
        time.sleep(self._t)

    def shift(self, bit=0):
        IO.output(self._data, bit)            # pull up the data pin for every bit.
        time.sleep(self._t)            # wait for 100ms
        IO.output(self._clock,1)            # pull CLOCK pin high
        time.sleep(self._t)
        IO.output(self._clock,0)            # pull CLOCK pin down, to send a rising edge

    def store(self):
        time.sleep(self._t)
        IO.output(self._data,0)            # clear the DATA pin
        IO.output(self._latch,1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(self._t)
        IO.output(self._latch,0)            # pull down the SHIFT pin
        

    def out(self, no):

        self.clear()
        
        for y in [int(x) for x in bin(no)[2:]]:            # loop for counting up 8 times
            self.shift(y)

        self.store()

