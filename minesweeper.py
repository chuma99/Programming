import random as r

def createBoard (rows, cols, mines):
    board = [[0 for r in range(rows+2)] for r in range(cols+2)]
    solution = [["X" for r in range(rows+2)] for r in range(cols+2)]
    
    for n in range(mines):
        # num_mines=0
        # while num_mines < mines :
        x = r.randint(1,rows)
        y = r.randint(1,cols)
        if board[y][x] != "B":
            board[y][x] = "B"
            if board[y][x-1] != "B": 
                board[y][x-1]+=1
            if board[y][x+1] != "B": 
                board[y][x+1]+=1
            if board[y-1][x] != "B": 
                board[y-1][x]+=1
            if board[y+1][x] != "B": 
                board[y+1][x]+=1
            if board[y-1][x-1] != "B": 
                board[y-1][x-1]+=1
            if board[y-1][x+1] != "B": 
                board[y-1][x+1]+=1
            if board[y+1][x+1] != "B": 
                board[y+1][x+1]+=1
            if board[y+1][x-1] != "B": 
                board[y+1][x-1]+=1

            # num_mines+=1

        #x = board.randrange(1,rows+1,1)
       # y = random.choice(x)
        #ypos = x.index(y)
        #if y == "0":
         #   x[ypos]= "B*"
          #  x[ypos+1] 
    for i in board:
        print(*i)
    for i in solution:
        print(*i)

    print("The objective of the game is to reveal all of the bombless positions without selecting a bomb.")
    print("Enter coordinates in order to select positions, and use the information given positions to determine where the bombs are not.")
    while True:
        xpos = int(input("Input the x coordinate of a bombless position (1-"+str(rows)+"): "))
        ypos = int(input("Input the y coordinate of a bombless position (1-"+str(cols)+"): "))
        if board[ypos][xpos] == "B":
            for i in board:
                print(*i)
            print("You've clicked on a bomb. Game over.")
            break
        else:
            #reveal solution[ypos][xpos]
            solution[ypos][xpos] = str(board[ypos][xpos])
            if board[ypos][xpos] == 0:
                solution[ypos][xpos-1] = str(board[ypos][xpos-1])
                if board[ypos][xpos-1] == 0:
                    solution[ypos][xpos-2] = str(board[ypos][xpos-2])
                    solution[ypos-1][xpos-1] = str(board[ypos-1][xpos-1])
                    solution[ypos+1][xpos-1] = str(board[ypos+1][xpos-1])
                    solution[ypos-1][xpos-2] = str(board[ypos-1][xpos-2])
                    solution[ypos+1][xpos] = str(board[ypos+1][xpos])
                    solution[ypos-1][xpos] = str(board[ypos-1][xpos])
                    solution[ypos+1][xpos-2] = str(board[ypos+1][xpos-2]) 
                solution[ypos][xpos+1] = str(board[ypos][xpos+1])
                if board[ypos][xpos+1] == 0:
                    solution[ypos][xpos+2] = str(board[ypos][xpos+2])
                    solution[ypos-1][xpos] = str(board[ypos-1][xpos])
                    solution[ypos+1][xpos] = str(board[ypos+1][xpos])
                    solution[ypos-1][xpos+2] = str(board[ypos-1][xpos+2])
                    solution[ypos+1][xpos+1] = str(board[ypos+1][xpos+1])
                    solution[ypos-1][xpos+1] = str(board[ypos-1][xpos+1])
                    solution[ypos+1][xpos+2] = str(board[ypos+1][xpos+2]) 
                solution[ypos-1][xpos] = str(board[ypos-1][xpos])
                if board[ypos-1][xpos] == 0:
                    solution[ypos][xpos-1] = str(board[ypos][xpos-1])
                    solution[ypos][xpos+1] = str(board[ypos][xpos+1])
                    solution[ypos-2][xpos] = str(board[ypos+1][xpos])
                    solution[ypos-1][xpos-1] = str(board[ypos-1][xpos-1])
                    solution[ypos-2][xpos+1] = str(board[ypos+1][xpos+1])
                    solution[ypos-1][xpos+1] = str(board[ypos-1][xpos+1])
                    solution[ypos-2][xpos-1] = str(board[ypos+1][xpos-1]) 
                solution[ypos+1][xpos] = str(board[ypos+1][xpos])
                if board[ypos+1][xpos] == 0:
                    solution[ypos][xpos-1] = str(board[ypos][xpos-1])
                    solution[ypos][xpos+1] = str(board[ypos][xpos+1])
                    solution[ypos+2][xpos] = str(board[ypos-1][xpos])
                    solution[ypos][xpos-1] = str(board[ypos-1][xpos-1])
                    solution[ypos+1][xpos+1] = str(board[ypos+1][xpos+1])
                    solution[ypos][xpos+1] = str(board[ypos-1][xpos+1])
                    solution[ypos+1][xpos-1] = str(board[ypos+1][xpos-1]) 
                solution[ypos-1][xpos-1] = str(board[ypos-1][xpos-1])
                if board[ypos-1][xpos-1] == 0:
                    solution[ypos][xpos-1] = str(board[ypos][xpos-1])####here
                    solution[ypos][xpos-2] = str(board[ypos][xpos-2])
                    solution[ypos-1][xpos-2] = str(board[ypos-1][xpos-2])
                    solution[ypos-1][xpos] = str(board[ypos-1][xpos])
                    solution[ypos-2][xpos] = str(board[ypos-2][xpos])
                    solution[ypos-2][xpos-1] = str(board[ypos-2][xpos-1])
                    solution[ypos-2][xpos-2] = str(board[ypos-2][xpos-2])
                solution[ypos+1][xpos+1] = str(board[ypos+1][xpos+1])
                if board[ypos+1][xpos+1] == 0:
                    solution[ypos][xpos+1] = str(board[ypos][xpos+1])
                    solution[ypos+1][xpos] = str(board[ypos+1][xpos])
                    solution[ypos][xpos+2] = str(board[ypos][xpos+2])
                    solution[ypos+1][xpos+2] = str(board[ypos+1][xpos+2])
                    solution[ypos+2][xpos] = str(board[ypos+2][xpos])
                    solution[ypos+2][xpos+1] = str(board[ypos+2][xpos+1])
                    solution[ypos+2][xpos+2] = str(board[ypos+2][xpos+2])
                solution[ypos-1][xpos+1] = str(board[ypos-1][xpos+1])
                if board[ypos-1][xpos+1] == 0:
                    solution[ypos-2][xpos] = str(board[ypos-2][xpos])
                    solution[ypos][xpos+1] = str(board[ypos][xpos+1])
                    solution[ypos-1][xpos] = str(board[ypos-1][xpos])
                    solution[ypos][xpos+2] = str(board[ypos][xpos+2])
                    solution[ypos-1][xpos-1] = str(board[ypos-1][xpos-1])
                    solution[ypos-2][xpos+2] = str(board[ypos-2][xpos+2])
                    solution[ypos-2][xpos+1] = str(board[ypos-2][xpos+1]) 
                solution[ypos+1][xpos-1] = str(board[ypos+1][xpos-1])  
                if board[ypos+1][xpos-1] == 0:
                    solution[ypos+1][xpos] = str(board[ypos+1][xpos])
                    solution[ypos][xpos-2] = str(board[ypos][xpos-2])
                    solution[ypos+2][xpos] = str(board[ypos+2][xpos])
                    solution[ypos][xpos-1] = str(board[ypos][xpos-1])
                    solution[ypos+1][xpos-2] = str(board[ypos+1][xpos-2])
                    solution[ypos+2][xpos-1] = str(board[ypos+2][xpos-1])
                    solution[ypos+2][xpos-2] = str(board[ypos+2][xpos-2])
                
            for i in board:
                print(*i)
            for i in solution:
                print(*i)



def difficulty():
    difficultylevel = input("Choose your preferred difficulty (E/M/H):")
    difficultylevel = difficultylevel.lower()
    if difficultylevel == "e":
        createBoard(9, 9, 10)
    elif difficultylevel == "m":
        createBoard(15, 15, 30)
    elif difficultylevel == "h":
        createBoard(20, 20, 80)
    else:
        print("You must choose from the 3 options!")
        difficulty()

print("WELCOME TO MINESWEEPER!")
difficulty()


#set the range to the number of rows and columns provided +2 for a border
    #for every row, create a row and a column
     #set # of mines to 0