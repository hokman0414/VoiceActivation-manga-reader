import time
import pyautogui
import keyboard

def scroll():
    #korean manhwa scroll rate
    scroll=1950
    #manga
    #scroll = 610
    for i in range(scroll):
        if keyboard.is_pressed('b'):
            break
        else:
            pyautogui.press('down')
            time.sleep(0.10)