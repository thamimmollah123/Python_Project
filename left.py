import keyboard as key
import pyautogui as py

while True:
     if key.is_pressed('left'):
          py.moveTo(100,200)
