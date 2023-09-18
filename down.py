import pyautogui as py
import keyboard as key

while True:
     if key.is_pressed('down'):
          py.position(x=315,y=45)
          py.mouseDown(345,45)
