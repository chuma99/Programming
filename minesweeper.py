import random

def createBoard (rows, cols, mines):
    board = []
    for r in range (0,rows+1):
        board.append([])
        for c in range (0,cols+1):
           board[r].append("C ")

    num_mines=0

    while num_mines < mines :
        x = random.choice(board)
        y = random.choice(x)
        ypos = x.index(y)
        if y == "C ":
            x[ypos]= "C*"

        num_mines = num_mines+1

    print(board)

createBoard(3, 3, 2)

#set the range to the number of rows and columns provided +1
    #for every row, create a row and a column
     #set # of mines to 0