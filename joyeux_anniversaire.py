import pyautogui, time, os, subprocess, cv2, pyperclip, pytesseract

def generate_substrings(input_string):
    n = len(input_string)
    substrings = []
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(input_string[0:j])
    return substrings
"""
def generate_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings
"""

def envoyer():
    subprocess.run(["adb", "shell", "input", "tap", "1000", "2300"])

def ecrire(input_string):
    for i in input_string.split():
        subprocess.run(["adb", "shell", "input", "text", i])
        subprocess.run(["adb", "shell", "input", "keyevent", "62"]) # Space key
    # subprocess.run(["adb", "shell", "input", "text", "songs"])

# adj = list()
# adj = ['fabuleuse', 'mirifique', 'Romane', 'geniale', 'la meilleure', 'mon idole', 'idole de jimmin', 'parfaite', 'legendaire', 'prodigieuse', 'fantastique', 'chimerique', 'irreelle', 'pharamineuse', 'magnifique', 'fictive', 'impressionnante', 'invraisemblable', 'rocambolesque', 'inouie', 'fantasmmagorique', 'abracadabrante', 'stupefiante']


for i in generate_substrings("joyeux anniversaire Romane tu es parfaite"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es legendaire"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es prodigieuse"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es fantastique"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es chimerique"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es irreelle"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es pharamineuse"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es magnifique"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es fictive"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es impressionnante"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es invraisemblable"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es rocambolesque"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es inouie"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es abracadabrante"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es fantasmmagorique"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()

for i in generate_substrings("joyeux anniversaire Romane tu es stupefiante"):
    time.sleep(1)
    ecrire(i)
    time.sleep(1)
    envoyer()