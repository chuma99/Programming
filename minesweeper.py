def createBoard (rows, cols, mines):

    board = []
    #set the range to the number of rows and columns provided +1
    #for every row, create a row and a column
    for r in range (0,rows+1):
        board.append([])
        for c in range (0,cols+1):
            board[r].append("C ")

    #set # of mines to 0

    num_mines=0

    while num_mines < mines :
        x = random.choice(board)
        y = random.choice(x)
        if y == "C ":
            x[y]= "C*"


            num_mines = num_mines+1