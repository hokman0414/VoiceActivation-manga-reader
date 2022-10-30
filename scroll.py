import pyautogui
import time
from pynput import keyboard
from scrollfunction import scroll
pyautogui.FAILSAFE = False


#keys to be detected
COMBINATION =[
    {keyboard.KeyCode(char='p')},

]
#current chapter
#Chapter_number = 92
#check keys being pressed
current =set()


def execution():
    #change outside variable
    #global Chapter_number
    print("activate scroll")
    #request this link with chapter
    scroll()
    #Chapter_number += 1


#pare any of the keys pressesd
def on_press(key):
    #if any of the keys in the eteration is pressed.
    if any([key in i for i in COMBINATION]):
        #add this to the current key list
        current.add(key)
        if any(all(k in current for k in i) for i in COMBINATION):
            execution()
#releasepppppppppppppp
def on_release(key):
    #if any of the key is released we need to remove it from the current set
    if any([key in i for i in COMBINATION]):
        current.remove(key)


#listener put together
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

