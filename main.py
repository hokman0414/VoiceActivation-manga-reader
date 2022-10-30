import time
from pynput import keyboard
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pynput import mouse
import subprocess
from scrollfunction import scroll
import speech_recognition
import pyaudio
#open seperate scroll script
cmd = 'python scroll.py'
subprocess.Popen(cmd,shell=True)



#make the browser stay open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#add extension
extension = r'C:\Users\pigge\5.3.0_0'
chrome_options.add_argument('load-extension=' + extension)
#selenium driver sstart no longer need chrome.exe
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()),options=chrome_options)
driver.create_options()
#maximum screen size
driver.maximize_window()
#time for it to let adblock be installed
time.sleep(5)
link_to_manga=f"https://chapmanganato.com/manga-mr990074/chapter-8"


driver.get(link_to_manga)


#keys to be detected
COMBINATION =[
    {keyboard.KeyCode(char='m')},
    {keyboard.Key.shift_r},
    {keyboard.Key.tab},

]
#current chapter
#Chapter_number = 92
#check keys being pressed
current =set()

#request page
def request_manga():
    #manga link
#kissmanga
    #driver.find_element(By.ID,'btnNext').click()
#mangakalot #find . which is class
    driver.find_element(By.CSS_SELECTOR,value=".navi-change-chapter-btn-next").click()

#cssselector usage   results = browser.find_elements(By.CSS_SELECTOR,'div[class="g"]')


def execute():
    #change outside variable
    #global Chapter_number
    print("Activated key")
    #request this link with chapter
    request_manga()
    time.sleep(5)
    #Chapter_number += 1


#pare any of the keys pressesd
def on_press(key):
    #if any of the keys in the eteration is pressed.
    if any([key in i for i in COMBINATION]):
        #add this to the current key list
        current.add(key)
        print(current)
        if any(all(k in current for k in i) for i in COMBINATION):
            execute()
#releasepppppppppppppp
def on_release(key):
    #if any of the key is released we need to remove it from the current set
    if any([key in i for i in COMBINATION]):
        current.remove(key)

#voice activation
voice_list =[]
r= speech_recognition.Recognizer()
while True:
    with speech_recognition.Microphone() as source:
        print("***********Awaiting Input**********")
        audio = r.listen(source,10,5)
        try:
            text = r.recognize_google(audio)
            print(f"you said:{text}")
            voice_list.append(text)
        except:
            print("***********ON STANDBY**********")


    if 'down' in voice_list:
        voice_list.clear()
        scroll()
    if 'next' in voice_list:
        execute()
        voice_list.clear()




#listener put together
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()


'''
with mouse.Listener(
    on_click=execute()
) as pressing:
    pressing.join()
'''