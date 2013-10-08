import RPi.GPIO as GPIO, time, os, random

import vhsled_spi,vhsled_text



GPIO.setmode(GPIO.BCM)

width = 26
height = 10

ledpixels = []
for i in range(0,width):
	ledpixels.append([0]*height)

spidev = file("/dev/spidev0.0", "w")


def colorwipe_vertical(pixels, c, delay,direction):
	for i in range(width)[::direction]:
		for j in range(height)[::direction]:
			setpixelcolor(pixels, i,j, c)
			writestrip(pixels,spidev)
			time.sleep(delay)

def colorwipe_horiz(pixels, c, delay,direction):
	for i in range(0,height)[::direction]:
		for j in range(0,width)[::direction]:
			setpixelcolor(pixels, j,i, c)
			writestrip(pixels,writestrip)
			time.sleep(delay)

def simpleGol(pixels, initial_points, live_c, dead_c, step_time, iterations):
	#not actually working yet.
	return
	setFullColour(pixels,dead_c)
	for i in range(initial_points):
		pixels[random.randint(0,width)][random.randint(0,height)] = live_c
		
	for i in range(iterations):
		new_pixels = pixels
	#	for x in range(width):
	#		for y in range(height):
	#		        
				
def countdown_timer(pixels, c, time_s):
	setFullColour(pixels,c)
	for i in range (0,height):
		for j in range(0,width):
			setpixelcolor(pixels,j,i,Color(0,0,0))
			writestrip(pixels,spidev)
			time.sleep(time_s/(width*height))

def Wheel(WheelPos):
	if (WheelPos < 85):
   		return Color(WheelPos * 3, 255 - WheelPos * 3, 0)
	elif (WheelPos < 170):
   		WheelPos -= 85;
   		return Color(255 - WheelPos * 3, 0, WheelPos * 3)
	else:
		WheelPos -= 170;
		return Color(0, WheelPos * 3, 255 - WheelPos * 3)

def rainbowBoard(pixels, wait):
	for j in range(256): # one cycle of all 256 colors in the wheel
    	   for i in range(width):
		   for k in range(height):
# tricky math! we use each pixel as a fraction of the full 96-color wheel
# (thats the i / strip.numPixels() part)
# Then add in j which makes the colors go around per pixel
# the % 96 is to make the wheel cycle around
			   setpixelcolor(pixels, i,k, Wheel( ((i * 256 / (width*height)) + j) % 256) )
	   writestrip(pixels,spidev)
	   time.sleep(wait)

def colourFlashMode(pixels,iterations, delay):
	for i in range(0,iterations):
		c = randomColor()
		for i in range(width):
			for j in range(height):
				setpixelcolor(ledpixels, i,j, c)
		writestrip(pixels)
		time.sleep(delay)

def rainbowCycle(pixels, wait):
        for j in range(256): # one cycle of all 256 colors in the wheel                                   
           for i in range(width):
                   for k in range(height):
# tricky math! we use each pixel as a fraction of the full 96-color wheel                                 
# (thats the i / strip.numPixels() part)                                                                  
# Then add in j which makes the colors go around per pixel                                                
# the % 96 is to make the wheel cycle around                                                              
                           setpixelcolor(pixels, i,k, Wheel( (((i*width+k) * 256 / ((width*height)) + j)) % 256) )
           writestrip(pixels)
           time.sleep(wait)

def setFullColour(pixels, c):
	for i in range(width):
		for j in range(height):
			setpixelcolor(pixels, i,j, c)
	writestrip(pixels)


c = randomColor()
setFullColour(ledpixels,c)

bright_colours = [Color(255,0,0),Color(0,255,0),Color(0,0,255),Color(255,255,255),Color(255,255,0),Color(255,0,255),Color(0,255,255)]

random.seed()


a="""
while True:
	text = raw_input("say string (or empty to start countdown):")
	if len(text) > 0:
		if text == "flash":
			while True:
				colourFlashMode(ledpixels,10,0.1)
		else:	
			scrollText(ledpixels,characters, text, random.choice(bright_colours),Color(0,0,0),0.05)
	else:
		countdown_timer(ledpixels, random.choice(bright_colours),90.0)
	setFullColour(ledpixels,Color(0,0,0))
"""

while True:
	action = random.randint(0,7)
	if action == 0:
		colourFlashMode(ledpixels,random.randint(0,20),0.1)
	elif action == 1:
		wipe = random.choice([0,1])
		if wipe == 0:
			colorwipe_vertical(ledpixels,randomColor(), 0.0005,random.choice([-1,1]))
		elif wipe == 1:
			colorwipe_horiz(ledpixels,randomColor(),0.0005,random.choice([-1,1]))
	elif action == 2:
		rainbowCycle(ledpixels, 0.00)
	elif action == 3:
		rainbowBoard(ledpixels,0.0)
	elif action >=4 and action < 7:
		strings= ["VHS! VHS!", "Welcome to the Bunker","drink beer", "sorry, We Lied about the cake","hack the planet", "42", "feed donatio"]
		scrollText(ledpixels,characters, random.choice(strings),randomColor(),Color(0,0,0),0.05)
	elif action ==7:
		oddityroll = random.randint(0,100)
		oddstrings = ["fnord", "subliminal message"]
		bright_colours = [Color(255,0,0),Color(0,255,0),Color(0,0,255),Color(255,255,255)]
		if oddityroll > 95:
			scrollText(ledpixels,characters,random.choice(oddstrings),random.choice(bright_colours),random.choice(bright_colours),0.001)



spidev.close()
