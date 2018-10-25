from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB", (imgx, imgy))
m = 0
n = 64
while n < 512 and m < 512:
	for x in range(m,n):
		for y in range(m,n):
			image.putpixel((x,y), (255,0,0))
	m+=64
	if n == 448:
		n+=63
	else:
		n+=64

m=128
n=192
o=0
p=64
while n < 512 and m < 512 and o < 512 and p < 512:
	for x in range(m,n):
		for y in range(o,p):
			image.putpixel((x,y), (255,0,0))
	m+=64
	if n == 448:
		n+=63
	else:
		n+=64
	o+=64
	if p== 448:
		p+=63
	else:
		p+=64

m=0
n=64
o=128
p=192
while n < 512 and m < 512 and o < 512 and p < 512:
	for x in range(m,n):
		for y in range(o,p):
			image.putpixel((x,y), (255,0,0))
	
	m+=64
	if n == 448:
		n+=63
	else:
		n+=64
	o+=64
	if p== 448:
		p+=63
	else:
		p+=64

m=0
n=64
o=192+64
p=192+128
while n < 512 and m < 512 and o < 512 and p < 512:
	for x in range(m,n):
		for y in range(o,p):
			image.putpixel((x,y), (255,0,0))
	m+=64
	if n == 448:
		n+=63
	else:
		n+=64
	o+=64
	if p== 448:
		p+=63
	else:
		p+=64

m=192+64
n=192+128
o=0
p=64
while n < 512 and m < 512 and o < 512 and p < 512:
	for x in range(m,n):
		for y in range(o,p):
			image.putpixel((x,y), (255,0,0))
	
	m+=64
	if n == 448:
		n+=63
	else:
		n+=64
	o+=64
	if p== 448:
		p+=63
	else:
		p+=64

m=0
n=64
o=192+192
p=192+192+64
while n < 512 and m < 512 and o < 512 and p < 512:
	for x in range(m,n):
		for y in range(o,p):
			image.putpixel((x,y), (255,0,0))
	m+=64
	if n == 448:
		n+=63
	else:
		n+=64
	o+=64
	if p== 448:
		p+=63
	else:
		p+=64

m=192+192
n=192+192+64
o=0
p=64
while n < 512 and m < 512 and o < 512 and p < 512:
	for x in range(m,n):
		for y in range(o,p):
			image.putpixel((x,y), (255,0,0))
	
	m+=64
	if n == 448:
		n+=63
	else:
		n+=64
	o+=64
	if p== 448:
		p+=63
	else:
		p+=64

#image.putpixel((0,0),(255,0,0))
image.save("demo_image.png", "PNG")