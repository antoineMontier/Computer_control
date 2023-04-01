import pyautogui, time, os, subprocess, cv2, pyperclip, pytesseract


while True:
    subprocess.run(["adb", "shell", "input", "tap", '530', '1440'])


"""
for i in range(100):
    subprocess.run(["adb", "shell", "input", "tap", '530', '1440'])
    time.sleep(.5)
    subprocess.run(["adb", "shell", "input", "tap", '630', '1340'])
    time.sleep(.5)
    subprocess.run(["adb", "shell", "input", "tap", '730', '1140'])
    time.sleep(.5)
    subprocess.run(["adb", "shell", "input", "tap", '530', '1540'])
    time.sleep(.5)
    subprocess.run(["adb", "shell", "input", "tap", '430', '1600'])
    time.sleep(.5)
    subprocess.run(["adb", "shell", "input", "tap", '550', '1440'])
    time.sleep(.5)
    subprocess.run(["adb", "shell", "input", "tap", '570', '1440'])
    time.sleep(.5)
    subprocess.run(["adb", "shell", "input", "tap", '580', '1440'])
    time.sleep(.5)
    subprocess.run(["adb", "shell", "input", "tap", '600', '1440'])
    time.sleep(.5)
"""