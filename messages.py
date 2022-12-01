import os
import pyautogui
import time
import sys
import pyperclip
# width = 1920   #height = 1080

contact = -1
msg = ""
occurence = -1
app = ""

while (app != "sms" and app != "whatsapp" and app != "instagram"):
    app = pyautogui.prompt("sms, whatsapp or instagram ?")

if (app == "whatsapp"):
    contact = pyautogui.prompt("What is your contact name?")
elif (app == "sms"):
    while (contact < 600000000 or contact > 799999999 or not isinstance(contact, int)):
        contact = int(pyautogui.prompt("What is your contact name?"))
elif (app == "instagram"):
    contact = pyautogui.prompt("What is your contact name?")

msg = pyautogui.prompt("What is your message ?")
occurence = int(pyautogui.prompt("and how many times do you want to send this message ?"))
answer = pyautogui.confirm("Alright so you want to send \"" + str(msg) + "\" " +
      str(occurence) + " times to " + str(contact) + "\n")
      
if (answer != "OK"):
    print("bye")
    exit()

# open chrome via terminal
os.system("gnome-terminal -e 'google-chrome'")
time.sleep(1)
if (app == "whatsapp"):
    pyperclip.copy("https://web.whatsapp.com")
    pyautogui.hotkey("ctrl", "v")  # copy what'sapp url in google chrome
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.leftClick(325, 230)
    pyperclip.copy(contact)
    pyautogui.hotkey("ctrl", "v")  # copy name in the serch bar
    pyautogui.press('enter')
    time.sleep(1)
    pyperclip.copy(msg)
    for _ in range(occurence):
        print("%d/%d" % (_, occurence))
        pyautogui.hotkey("ctrl", "v")  # copy message
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
elif (app == "sms"):
    pyperclip.copy("https://messages.google.com")
    pyautogui.hotkey("ctrl", "v")  # copy message url in google chrome
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.leftClick(210, 230)
    pyperclip.copy(contact)
    pyautogui.hotkey("ctrl", "v")  # copy name in the serch bar
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    pyperclip.copy(msg)
    for _ in range(occurence):
        print("%d/%d" % (_, occurence))
        pyautogui.hotkey("ctrl", "v")#copy message 
        time.sleep(0.1) 
        pyautogui.press('enter')
        time.sleep(0.1)
elif(app == 'instagram'):
    pyperclip.copy("https://www.instagram.com")
    pyautogui.hotkey("ctrl", "v")       #copy message url in google chrome
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.leftClick(190, 450)
    time.sleep(2)
    pyautogui.leftClick(1275, 700)
    pyperclip.copy(contact)
    pyautogui.hotkey("ctrl", "v")#copy name in the serch bar
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.leftClick(1140, 425)
    time.sleep(1.5)
    pyautogui.leftClick(1140, 320)
    time.sleep(5)
    pyperclip.copy(msg)
    for _ in range(occurence):
        print("%d/%d" % (_, occurence))
        pyautogui.hotkey("ctrl", "v")#copy message 
        time.sleep(0.1) 
        pyautogui.press('enter')
        time.sleep(0.1)


time.sleep(5)#wait for messages to be sent before closing window
pyautogui.hotkey("ctrl", "w")