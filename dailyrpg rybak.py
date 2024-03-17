import interception
import time
import dxcam
import pyautogui
import cv2
import numpy as np
from termcolor import colored
import os
interception.auto_capture_devices(keyboard=True, mouse=True)
os.system('title discord hypeer_7')

camera = dxcam.create()
print(colored("bocik zrobiony przez discord: hypeer_7", 'magenta'))
while True:

   if pyautogui.locateOnScreen('rybalewo.png', confidence=0.80):
        interception.click(button="left", delay=1)
        print("jest rybka uu sigma rel")
        time.sleep(2)
        interception.click(button="left", delay=1)
        os.system('cls')
        print(colored("bocik zrobiony przez discord: hypeer_7", 'magenta'))
   if pyautogui.locateOnScreen('rybaprawo.png', confidence=0.80):
        interception.click(button="left", delay=1)
        print("jest rybka uu sigma rel")
        time.sleep(2)
        interception.click(button="left", delay=1)
        os.system('cls')
        print(colored("bocik zrobiony przez discord: hypeer_7", 'magenta'))
