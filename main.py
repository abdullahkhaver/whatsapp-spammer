import pyautogui
import time

msg = "Your Message Here"

x = int(input("How many times: "))

time.sleep(5)  

for _ in range(x):
    pyautogui.write(msg)
    pyautogui.press("enter")
    time.sleep(0.2)
