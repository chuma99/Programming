import math as m

def start():
	num = int(m.rand() * 100)
	def guess():
	response = int(input("Guess an integer from 0 to 99:"))
		if response == num:
			answer = lower(input("Correct! You win! Would you like to play again? Y/N \n"))
			if answer == "y":
				start()
			elif answer == "n":
				print("Thanks for playing the game!")
		else:
			answer = input("Incorrect. Guess again!")
			guess()
start()