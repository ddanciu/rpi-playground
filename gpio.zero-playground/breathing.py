from gpiozero import PWMLED
import signal



led = PWMLED(17)

led.pulse()

signal.pause()
