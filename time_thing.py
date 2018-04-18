import ctypes
from time import sleep
import random


MessageBox = ctypes.windll.user32.MessageBoxW

while (True):
	sleep(1500) #25 minutes
	messages = ["Mindfullness break: breath and chill out for a sec","Take a walk around the building","Grab some water"]
	MessageBox(None, messages[random.randint(0,len(messages)-1)], 'Breaktime',0)
	sleep(300) #5 minutes
	MessageBox(None, "Time is up, get back to work", 'Worktime',0)


