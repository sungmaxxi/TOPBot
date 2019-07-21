import pyautogui
import time
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
def goToCoordinates(x,y):
    print("going back to" + str(x) +","+ str(y))
    pyautogui.hotkey('alt', 'R')
    pyautogui.typewrite(str(x),0.25)
    pyautogui.press('tab')
    pyautogui.typewrite(str(y),0.25)
    pyautogui.press('enter')
    time.sleep(3)
    return

def pickUpAll():
    pyautogui.hotkey('Ctrl', 'A')
    return

def attackAndLoot(x,y,timer):
    print("Attacking and Looting")
    #pyautogui.moveTo(x, y)
    pyautogui.PAUSE = 0.07
    pyautogui.mouseDown(x,y)
    pyautogui.mouseUp()
    pickUpAll()
    time.sleep(timer)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(2)
    pickUpAll()
    pyautogui.PAUSE = 0.1 #default value
    return

def attackHere(x,y,timer):
    print("Attacking")
    #pyautogui.moveTo(x, y)
    pyautogui.PAUSE = 0.07
    pyautogui.mouseDown(x,y)
    pyautogui.mouseUp()
    pickUpAll()
    pyautogui.PAUSE = 0.1
    time.sleep(timer)
    return

try:
    print("Starting!")
    time.sleep(1)
    resetHereX = input("What's the anchored X?\n")
    resetHereY = input("What's the anchored Y?\n")
    WhatMobToFarm = input("What mob do you want to farm? e.g CuddlyLamb.png\n")
    timer = int(input("How long does it take to kill a mob? \n"))
    resetTime = int(input("Go to anchor at how many seconds?\n"))
    #pyautogui.click(1216, 276)
    click(1216, 276)
    goBackCounter = 0

    #shell = win32com.client.Dispatch("WScript.Shell")
    while (True):
        if(goBackCounter > resetTime):
            click(1216,276)
            goToCoordinates(resetHereX,resetHereY)
            goBackCounter = 0
        else:
            try:
                pyautogui.keyDown('shift')
                x, y = pyautogui.locateCenterOnScreen(str(WhatMobToFarm), confidence=.6)
                pyautogui.keyUp('shift')
                attackAndLoot(x,y,timer)
                goBackCounter = 0
            except:
                goBackCounter+=1
                print("Failed first block")
            try:
                pyautogui.keyDown('shift')
                x, y = pyautogui.locateCenterOnScreen('WackyLamb.png', confidence=.6)
                pyautogui.keyUp('shift')
                attackAndLoot(x, y,timer)
                goBackCounter = 0
            except:
                goBackCounter+=1
                print("Failed second block")

except KeyboardInterrupt:
    print("finished")
    pyautogui.keyUp('shift')


