#print a series of color coded boxes on a grid 
#based on the number of iterations of the mandelbrot equations 
#it takes for the imaginary number given by the coordinate values to be greater than 2

def createBoard (rows, cols):
	board = [[0 for r in range(rows+2)] for r in range(cols+2)]

createBoard(512,512)

MaxValue = 4
MaxIterations = 50
planeWidth = 4

for x in range(0, size):
    for y in range(0, size): # for each pixel do:
        cReal = (x * planeWidth / size) - 2
        cImg =  (y * planeWidth / size) - 2
        zReal = 0
        zImg = 0
        count = 0
        while (zReal*zReal + zImg*zImg) <= MaxValue and count < MaxIterations:
            temp = (zReal * zReal) - (zImg * zImg) + cReal
            zImg = 2 * zReal * zImg * cImg
            zReal = temp
            count += 1

        if count == MaxIterations:
            img.put((x,y))


