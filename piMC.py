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

width = 42
height = 10

ledpixels = []
for i in range(0,width):
	ledpixels.append([0]*height)

spidev = file("/dev/spidev0.0", "w")

random.seed()

c = randomColor()
setFullColor(ledpixels,spidev,c)

# a few nice and bright colours with at least one channel at full. 
bright_colors = [Color(255,0,0),Color(0,255,0),Color(0,0,255),Color(255,255,255),Color(255,255,0),Color(255,0,255),Color(0,255,255)]


while True:
	text = raw_input("display string (blank to start countdown, 'exit' to quit):")
	if len(text) > 0:
		if text == "flash": #undocumented mode to strobe the display
			while True:
				colorFlashMode(ledpixels,spidev,10,0.1)
		elif text =="exit":
				break
		else:	
			scrollText(ledpixels,spidev,characters, text, random.choice(bright_colors),Color(0,0,0),0.05)
	else:
		countdown_timer(ledpixels, random.choice(bright_colors),90.0)
	setFullColor(ledpixels,spidev,Color(0,0,0))

spidev.close