import pyautogui, time, os, subprocess, cv2, pyperclip, pytesseract
#joyeux anniversaire Romane tu es extraordinaire
def generate_substrings(input_string):
    n = len(input_string)
    substrings = []
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(input_string[i:j])
    return substrings

def envoyer():
    subprocess.run(["adb", "shell", "input", "tap", "1000", "2300"])

def ecrire(input_string):
    for i in input_string.split():
        subprocess.run(["adb", "shell", "input", "text", i])
        subprocess.run(["adb", "shell", "input", "keyevent", "62"]) # Space key
    # subprocess.run(["adb", "shell", "input", "text", "songs"])

adj = list()
adj = ['extraordinaire', 'fabuleuse', 'mirifique', 'Romane', 'geniale', 'la meilleure', 'mon idole', 'idole de jimmin', 'parfaite', 'legendaire', 'prodigieuse', 'fantastique', 'chimerique', 'irreelle', 'pharamineuse', 'magnifique', 'fictive', 'impressionnante', 'invraisemblable', 'rocambolesque', 'inouie', 'fantasmmagorique', 'abracadabrante', 'stupefiante']


for j in adj:
    for i in generate_substrings("joyeux anniversaire Romane tu es "+ j):
        time.sleep(1)
        ecrire(i)
        time.sleep(1)
        envoyer()