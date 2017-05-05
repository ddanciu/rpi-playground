from gpiozero import Button
from time import sleep
button1 = Button(23)
button2 = Button(24)
button3 = Button(5)
button4 = Button(6)

while True:
    print("inputs #23: {} #24 {}".format(button1.is_pressed, button2.is_pressed) )
    print("inputs # 5: {} # 6 {}".format(button3.is_pressed, button4.is_pressed) )
    print("")
    sleep(0.5)
