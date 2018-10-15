from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB", (imgx, imgy))

for x in range(512):
	for y in range(512):
		image.putpixel((x,y), (255,0,0))

image.putpixel((0,0),(255,0,0))
image.save("demo_image.png", "PNG")