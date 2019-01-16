from random import randint

board = [[randint(0,5) for r in range(5)] for r in range(5)]
for i in board:
        print(*i)

print(board[0])
low = board[0][0]
for i in board:
    if i < low:
    	low = i
	return int(low)
print(low)