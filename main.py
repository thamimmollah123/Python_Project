import keyboard as key # IMPORT KEYBOARD
import pyautogui as py # IMPORT PYAUTOGUI         

   
while True:  
     # CHEAKING FOR UP BUTTON             
     if key.is_pressed('up'):          
          py.mouseUp(100,200,duration=0.1)                             

          # USE DOWN BY KEYBOARD DOWN ARROW
               
     elif key.is_pressed('down'):            
          py.mouseDown(300,300) 
          # MOVE TO RIGHT USE KEYBOARD          
     elif key.is_pressed('right'): 
          py.moveTo(500,500)
      # MOVE TO RIGHT USE KEYBOARD 
     elif key.is_pressed('left'):                          
          py.moveTo(200,300)
          # SCROLL USING BY KEYBOARD SPACE
     elif key.is_pressed('space'): 
          py.scroll(-20)   
          # MOUSE LEFTCLICK USING BY KEYBOARD h 
            
     elif key.is_pressed('h'):

        
          py.leftClick()
          # MOUSE RIGHTCLICK USING BY KEYBOARD t
     elif key.is_pressed('t'):                     
          py.rightClick()
          # KEBOARD f BUTTON USE FOR DOUBLE CLICK
     elif key.is_pressed('f'):
          py.doubleClick()
       # OPEN POPUP HELLO USING BY KEYBOARD c BUTTON
     elif key.is_pressed('c'):
          py.alert(text='Hello ', title='Welcome to code', button='OK')

          # shift BUTTON FOR UP SCROLLING
     else:
          key.is_pressed('shift')
          py.scroll(20)  