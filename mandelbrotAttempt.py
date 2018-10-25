#print a series of color coded boxes on a grid 
#based on the number of iterations of the mandelbrot equations 
#it takes for the imaginary number given by the coordinate values to be greater than 2

def createBoard (rows, cols):
	board = [[0 for r in range(rows+2)] for r in range(cols+2)]

createBoard(6,6)

for i in board:
        print(*i)

