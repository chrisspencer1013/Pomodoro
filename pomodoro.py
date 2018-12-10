import ctypes
from time import sleep
import random
import sys
import os
from threading import Timer
from playsound import playsound

MessageBox = ctypes.windll.user32.MessageBoxW
clear = lambda: os.system('cls')
messages = ["Mindfullness break: breath and chill out for a sec",
				"Take a walk around the building",
				"Grab some water"]


#Not quite what we want for this purpose
def foo():
	timer = Timer(10.0, lambda: MessageBox(None, messages[random.randint(0,len(messages)-1)], 'Breaktime',0)).start()
	MessageBox(None, "Alright, let's get back to it!", 'Worktime',0)


#Old method
while (True):

	for i in range(60*25,0,-1):
		sleep(1)
		clear()
		#print(str(int(i/60))+':'+str(i%60)+' left in this work cycle')
		print('%i:%02i left in this work cycle' % (int(i/60), i%60))
	playsound('R2D2a.mp3')
	for i in range(60*5,0,-1): 
		sleep(1)
		clear()
		print('%i:%02i left to your break' % (int(i/60), i%60))
	playsound('R2D2a.mp3')
	MessageBox(None, messages[random.randint(0,len(messages)-1)]
	MessageBox(None, "Alright, let's get back to it!", 'Worktime',0)
