import math as m
num = int(m.rand() * 100)
def start():

	response = int(input("Guess an integer from 0 to 99:"))
		if response == num:
			answer = input("Correct! You win! Would you like to play again? Y/N \n")
		else:
			answer = input("Incorrect. Guess again!")
	elif response == "2":
		map()
	else:
		print("You must type 1 or 2. Please try again.")
		start()
start()