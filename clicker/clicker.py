import mouse
import keyboard
from time import sleep

isClicking = False


def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("Clicker was turned off")
    else:
        isClicking = True
        print("Clicker was enabled")


keyboard.add_hotkey("Alt + Z", set_clicker)

while True:
    if isClicking:
        mouse.double_click(button="left")
        sleep(0.01)
