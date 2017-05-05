from gpiozero import Button
from gpiozero import PWMLED
from signal import pause

led = PWMLED(27)
button = Button(18)

#on: yes > 1, off == 0
on = 0

def pushed():
    global on
    global led
    on = (on + 1) % 2
    #print(on)
    if on > 0:
        led.pulse()
    else:
        led.off()





button.when_released = pushed

pushed()

pause()
