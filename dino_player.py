import  pyautogui, time
from PIL import ImageGrab



def resetZoomWindow():
    pyautogui.keyDown('ctrl')
    for i in range(2):
        pyautogui.scroll(1)
    for i in range(2):
        pyautogui.scroll(-1)
    pyautogui.keyUp('ctrl')

    reset = pyautogui.locateOnScreen('resetButton.png')
    if reset != None:
        pyautogui.leftClick(reset[0] + reset[2]/2, reset[1] + reset[3])
        time.sleep(1)
        pyautogui.press('esc')#start game

def obstacleInFrontOfDino(array_of_px, start_x, start_y, length, color_of_background):
    i = start_x
    while(i < start_x + length):
        if(array_of_px[i, start_y] != color_of_background):
            #print(array_of_px[i, start_y], " != ", color_of_background)
            return True
        i+=2
    return False



"""
answer = pyautogui.confirm("ready to start ?\n")
if (answer != "OK"):
    print("bye")
    exit()


os.system("gnome-terminal -e  'nmcli radio wifi off'")#turn wifi off
time.sleep(1)
os.system("gnome-terminal -e 'google-chrome'")#open google-chrome
time.sleep(1)
#==========enter a random website
pyperclip.copy("dino")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
#==============================
resetZoomWindow()#set window zoom to default
"""
#==================locate dino on x and y axis
dino = pyautogui.locateOnScreen('dino.png', confidence=0.8 )
if dino != None:
    x_axis = dino[0] + dino[2]/2
    y_axis = dino[1] + dino[3]/2
    dino_height = dino[3]
    dino_width = dino[2]
else:
    print("cannot locate dino on screen")
    exit()
#======================
region_x = x_axis
region_y = y_axis
region_w = dino_width
region_h = dino_height



pyautogui.press('space')#start game

iterations = 0
last_jump = iterations
playing = True
while playing:
    #do things....
    # print("iterations = %d" % iterations)
    iterations += 1
    px = ImageGrab.grab().load()
    bg_color = px[region_x - region_w*2 , region_y]
    #mouse = pyautogui.position() 
    #print(mouse)
    #print(region_x - region_w*2 , region_y)

    if obstacleInFrontOfDino(px, region_x + region_w*0.5, region_y, region_w*1.4, bg_color): 
        print("cactus or bottom raven")
        last_jump = iterations
        pyautogui.press('space') 
    elif obstacleInFrontOfDino(px, region_x + region_w*0.9     , region_y - region_h*0.3, region_w, bg_color)  and not obstacleInFrontOfDino(px, region_x + region_w*0.9     , region_y + region_h*0.3, region_w/2, bg_color):
        print("raven")
        last_jump = iterations
        #pydirectinput.press('down')
    #cactus = pyautogui.locateOnScreen('cactus_stick.png', region=(region_x ,region_y, region_w, region_h), confidence=0.9)
    #if(cactus != None):
    #    pyautogui.press('space')

"""
    restart = pyautogui.locateOnScreen('restart.png')
    if(restart != None):
        print("lost")
        playing = False
"""


#pyautogui.click(pyautogui.locateAllOnScreen('magnifier.png'))
