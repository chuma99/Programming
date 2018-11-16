#11-16-18
#For this assignment, I have created a grayscale filter that accepts images and returns them with only neutral colors!
#Sources: 	https://www.oreilly.com/library/view/programming-computer-vision/9781449341916/ch01.html
#			https://dsp.stackexchange.com/questions/43701/convert-rgb-image-to-grayscale-and-display-it-python-matplotlib
#			https://docs.python-guide.org/scenarios/imaging/
#			https://www.youtube.com/watch?v=6Qs3wObeWwc
#			https://www.youtube.com/watch?v=XPrXttsX1wY
#On my honor, I have neither given or received unauthorized aid.

from PIL import Image
import math

def open_image(path): #creates method that incorporates PIL library
	newImage = Image.open(path)
	return newImage

def save_image(image, path): #a way to save the image from input
	image.save(path, 'png')

def create_image(i, j): #expresses the new image so that it can be transformed
	image = Image.new("RGB", (i, j), "white")
	return image

def get_pixel(image, i, j): #essential in changing individual pixels of the image
	width, height = image.size
	if i > width or j > height:
		return None

	pixel = image.getpixel((i, j))
	return pixel

def convert_grayscale(image):
	# Getting the size of the image
	width, height = image.size
	new = create_image(width, height)
	pixels = new.load()

	# This is the loop that transforms the image to grayscale
	for i in range(width):
		for j in range(height):
			pixel = get_pixel(image, i, j)
			red =   pixel[0]
			green = pixel[1]
			blue =  pixel[2]
			#This changes each pixel to a shade of gray
			gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)      
			pixels[i, j] = (int(gray), int(gray), int(gray))

	return new

image = Image.open('fieldtower.jpg')
image.show()
convert_grayscale(image).show()