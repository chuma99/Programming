from PIL import Image, ImageFilter

xa, xb = -0.63788, -0.44463
ya, yb = 0.51314, 0.70640

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

		r = (i*40)%128#i
		g = (i*100)%256#int(256-(i%(i+2)%2))
		b = (i*50)%256

		image.putpixel((x,y), (r,g,b))

km = (
     -2, -1,  0,
     -1,  1,  1,
      0,  1,  2
      )

im1 = ImageFilter.Kernel(
    size=(3, 3),
    kernel=km,
    scale=sum(km),
    offset=0 
    )
#im1 = image.filter(ImageFilter.Kernel((3,3), 3, 1, 0))


image.filter(im1).show()
