import random as m

def start():
	num = int(m.random() * 100)
	print(num)
	guess(num)

def guess(num):
		response = int(input("Guess an integer from 0 to 99:"))
		if response == num:
			print("Correct! You win!")
			restart()
		else:
			answer = input("Incorrect. Guess again!")
			guess(num)

def restart():
			answer = input("Would you like to play again? Y/N \n")
			answer.lower()
			if answer == "y":
				start()
			elif answer == "n":
				print("Thanks for playing the game!")
			else:
				print("Incorrect input. Try again")
				restart()

start()
