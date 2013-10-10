# a more accurate name for this would be timer.py, however the "spec"
#  calls for the pi based timer to be called piMC.py. Who am I to argue.
import RPi.GPIO as GPIO, time, os, random
from vhsled_spi import *
from vhsled_text import *
from vhsled_colour import *


def countdown_timer(pixels, c, time_s):
	setFullColor(pixels,spidev,c)
	for i in range (0,height):
		for j in range(0,width):
			setpixelcolor(pixels,j,i,Color(0,0,0))
			writestrip(pixels,spidev)
			time.sleep(time_s/(width*height))

GPIO.setmode(GPIO.BCM)

width = 26
height = 10

ledpixels = []
for i in range(0,width):
	ledpixels.append([0]*height)

spidev = file("/dev/spidev0.0", "w")

random.seed()

c = randomColor()
setFullColor(ledpixels,spidev,c)

# a few nice and bright colours with at least one channel at full. 
bright_colors = [Color(0,255,0),Color(0,0,255),Color(255,255,0),Color(255,0,255),Color(0,255,255)]


while True:
	text = raw_input("display string (insert dev code or press enter to run countdown):")
	if len(text) > 0:
		if text == "flash": #undocumented mode to strobe the display
			while True:
				colorFlashMode(ledpixels,spidev,10,0.1)
		if text == "snake": #undocumented mode to strobe the display
			while True:
				colorwipe_snake(ledpixels,spidev,randomColor(),0.05)
		if text == "wipe": #undocumented mode to strobe the display
			while True:
				colorwipe_horiz(ledpixels,spidev,randomColor(),0.0005,1)
		if text == "fades": #undocumented mode to strobe the display
			while True:
				rainbowBoard(ledpixels,spidev,0.0)
		if text == "rainbows": #undocumented mode to strobe the display
			while True:
				rainbowCycle(ledpixels,spidev, 0.00)
		elif text =="exit":
				break
	else:
		seconds = int(raw_input("How many seconds?"))
		countdownText(ledpixels,spidev,characters,seconds, random.choice(bright_colors),Color(0,0,0),1)
	setFullColor(ledpixels,spidev,Color(0,0,0))


spidev.close