import pyautogui
import time
def sendsms(n):
    time.sleep(10)
    for i in range(n):
        pyautogui.write('hay Sasank !!')
        pyautogui.press('Enter')
        time.sleep(5)
sendsms(5)
