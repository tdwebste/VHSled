import RPi.GPIO as GPIO, time, os

def writestrip(pixels,spidev):
	for i in range(0,len(pixels),1):
		start = 0
		end = len(pixels[0])
		step = 1
		if (i % 2 == 1):
			start = len(pixels[0])-1
			end = -1
			step = -1
		for j in range(start,end,step):
			spidev.write(chr((pixels[i][j]>>16) & 0xFF))
			spidev.write(chr((pixels[i][j]>>8) & 0xFF))
			spidev.write(chr(pixels[i][j] & 0xFF))
	spidev.flush()

