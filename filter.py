from PIL import Image
import math

def open_image(path):
  	newImage = Image.open(path)
 	return newImage

def save_image(image, path):
  	image.save(path, 'png')

def create_image(i, j):
 	image = Image.new("RGB", (i, j), "white")
  	return image

def get_pixel(image, i, j):
    width, height = image.size
    if i > width or j > height:
      	return None

def convert_grayscale(image):
  # Get size
	width, height = image.size
	new = create_image(width, height)
	pixels = new.load()

  # Transform to grayscale
	for i in range(width):
		for j in range(height):
			pixel = get_pixel(image, i, j)

			red =   pixels[0]
			green = pixel[1]
			blue =  pixel[2]

			gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)      
			pixels[i, j] = (int(gray), int(gray), int(gray))
	return new

#imgx = 512
#imgy = 512 

#image = Image.new("RGB", (imgx, imgy))
image = Image.open('demo_image.png')
print(convert_grayscale(image))
image.show()