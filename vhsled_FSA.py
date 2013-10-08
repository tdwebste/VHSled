def simpleGol(pixels, initial_points, live_c, dead_c, step_time, iterations):
	#not finished yet.
	return
	setFullColor(pixels,dead_c)
	for i in range(initial_points):
		pixels[random.randint(0,width)][random.randint(0,height)] = live_c
		
	for i in range(iterations):
		new_pixels = pixels
	#	for x in range(width):
	#		for y in range(height):
	#		