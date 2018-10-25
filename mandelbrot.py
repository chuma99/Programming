from PIL import Image, ImageFilter

#https://www.atopon.org/mandel/#

xa, xb = -0.232397, -0.205298
ya, yb = 0.6888428, 0.7159424

imgx, imgy = 512,512

maxIt = 256 #colors out of 255, so iterations never cuts a color!


image = Image.new("RGB", (imgx, imgy))

for y in range(imgy):
	cy = y*(yb-ya)/(imgy-1)+ya
	for x in range(imgx):
		cx = x*(xb-xa)/(imgx-1)+xa
		c = complex(cx,cy)
		z = 0
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**2 + c

		r = (i*40)%128#adjusts code color on more than incremental
		g = (i*5)%128
		b = (i*50)%256

		image.putpixel((x,y), (r,g,b))

im1 = image.filter(ImageFilter.GaussianBlur(2))#blurs image to scale of 2

im1.show()