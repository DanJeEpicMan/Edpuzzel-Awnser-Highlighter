#i know how to append, this is better
import time
awn = ["","","","","","","","","","","","","","","","","","","","","","","","",] 
done = 0
n = 0
while done == 0:
    awn[n] = input("awnser: ")
    if awn[n] == "end":
        done = 1
        awn[n] = "end-------------------+_+_+_+_+_+gujbfggb;fgu"
    n = n+1
n = 0; n = int(n)
next = 0; next = int(n)
back = 0; back = int(n)
print("now in production mode (letters with accsents = normal letters")
#qprint(awn)


import keyboard
import pyautogui

while True:
    if keyboard.is_pressed("]"):
        back = 0
        if next == 1:
            pass
        else:
            next = 1
            n = n + 1
            print(n)
    if keyboard.is_pressed("["):
        next = 0
        if back == 1:
            pass
        else:
            back = 1
            n = n - 1
            print(n)


    if keyboard.is_pressed("'"):
        next = 0
        back = 0
        print(awn[n])
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('f')
        time.sleep(0.1)
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('f')
        time.sleep(0.2)
        pyautogui.write(awn[n])
    
    #time.sleep(0.1)
