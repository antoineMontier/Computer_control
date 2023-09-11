import os
import pyautogui as py
import time
import sys
import pyperclip
import keyboard

def click_on(picture_name, x_off=0, y_off=0):
	image_location = py.locateOnScreen(picture_name)
	if( not image_location ): 
		print("no image, no click")
		return
	center_x = image_location.left + image_location.width  // 2 + x_off
	center_y = image_location.top  + image_location.height // 2 + y_off
	print("click on ", center_x, center_y)
	py.leftClick(center_x, center_y)


def need_intervention():
	x, y = py.position()
	py.sleep(.1)
	py.hotkey('ctrl', 'a')
	py.sleep(.1)
	py.hotkey('ctrl', 'c')
	py.sleep(.1)
	page_str = pyperclip.paste()
	py.sleep(.1)

	res = False
	if 'gateway.gostudent.org' in page_str:
		res = True
		py.leftClick(1500, 1000)
		return res


	py.leftClick(1500, 1000)
	py.sleep(.1)
	py.press('escape')
	py.sleep(.1)
	py.moveTo(x, y)
	return res

def modify_title():
	py.hotkey('ctrl', 'a')
	py.sleep(.1)
	py.hotkey('ctrl', 'c')

	str = pyperclip.paste()

	str = str.split('\n')[1]

	print("l1:", str)

	str = str.split('/')[1]

	names = str.split(',')

	name = names[0].strip()#[:-1]
	surname = names[1].strip()

	print(name, surname)

	updated_name = ''
	if name.capitalize() == surname.capitalize():
		updated_name = name
	
	else:
		updated_name = name + ' ' + surname
	
	for i in range(3): py.leftClick(170, 170) # triple click

	pyperclip.copy(updated_name)

	py.hotkey('ctrl', 'v')

	
def modify_calendar():
	click_on("cal.png", 60)	
	py.sleep(.2)
	click_on("Gs.png")



# py.mouseInfo()
# exit()



while True:
	py.sleep(4)
	if not need_intervention():
		continue
	py.sleep(.1)
	modify_title()
	py.sleep(.2)
	modify_calendar()
	py.sleep(.2)
	click_on("save.png")




