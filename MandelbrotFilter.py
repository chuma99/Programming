from PIL import Image, ImageFilter

image = Image.open('mandelbrot1.png')

im1 = image.filter(ImageFilter.Kernel((3,3), 3, 1, 0))
#im1 = image.filter(ImageFilter.GaussianBlur(5))

im1.show()
