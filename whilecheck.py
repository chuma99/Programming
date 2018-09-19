while True:
	try:
		num = int(input("Pick a number between 1 and 5: "))
		between()
		break

	except ValueError:
		print("That's not right. Pick an integer between 1 and 5 with your number keys.")

def between():
	if num>5 and num<1:
		num = int(input("That's not right. Pick a number BETWEEN 1 and 5: "))
	else:
		print("Good Job")
