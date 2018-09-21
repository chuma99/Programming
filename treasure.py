def start():
	response = input("Do you 1) Trust your Friend, or 2) Trust the Map?\n")
	if response == "1":
		friend()
	elif response == "2":
		map()
	else:
		print("You must type 1 or 2. Please try again.")
		start()

def map():
	response = input("The treasure is north of Mt. Everest! Would you like to 1) follow the map, or 2) teleport within 2 miles and search yourself?")
	if response == "1":
		guide()
	elif response == "2":
		teleport()
	else:
		print("You must type 1 or 2. Please try again.")
		map()

def friend():
	response = input("I heard the treasure is south of Mt. Everest. Do you 1) want me to guide you, or 2) want me to purchase you plane ticket to Mt. Everest?")
	if response == "1":
		follow()
	elif response == "2":
		fly()
	else:
		print("You must type 1 or 2. Please try again.")
		friend()

def guide():
	print("Here is a map that will lead you straight to the treasure. ")
	response = input("Would you like to 1) spend time interpretting the map, or 2) begin along the path?")
	if response == "1":
		print("You have been able to accurately interpret the map, and after walking towards it you've located the treasure")
		answer = input("Would you like to 1) open the chest or 2) pick up the chest and carry it home?")
	elif response == "2":
		print("You have overwalked the treasure and are now disoriented. You rip up your map in frustration, and return home.")
		restart()
	else:
		print("You must type 1 or 2. Please try again.")
		guide()

def teleport():
	print("You were teleported to the top of mount Everest, and due to your unprepared state, you have now frozen to death. ")
	restart()

def follow():
	print("You have chosen to follow your friend, and at a crossroad, he is unsure which direction to take, so he asks you to help.")
	response = input("Would you like to 1) go down the rocky road, or 2) scale a hill in the opposite direction?")
	if response == "1":
		print("By chosing to travel down the rocky road, you have committed to a path of which the end is unforseeable.")
		answer = input("Would you like to 1) turn back or 2) continue down the rocky road?")
	elif response == "2":
		print("By partially scaling the hill, you have gained an advantageous view of the area. You can now see a clear path to the treasure.")
		answer = input("Would you like to 1) follow this path or 2) continue scaling the hill?")
	else:
		print("You must type 1 or 2. Please try again.")
		follow()

def fly():
	print("Your plane has landed at the airport closest to mount Everest. You get out of the plane and exit the airport. ")
	response = input("Would you like to 1) call an uber to mount Everest, or 2) take a taxi?")
	if response == "1":
		print("By chosing to travel via uber, you get to the destination much later than planned.")
		answer = input("Would you like to 1) tip your driver, or 2) exit and give him a bad rating?")
	elif response == "2":
		print("By chosing to travel via taxi, you are now being asked to fork over all of the cash you have, because you could not cover the fare.")
		answer = input("Would you like to 1) run away and try to evade the taxi driver or 2) give up all of your money?")
	else:
		print("You must type 1 or 2. Please try again.")
		fly()
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


print("Greetings! You are looking for treasure.\n Your map says that the treasure can be found northerly.\n However, your friend says he heard someone talking about treasure in the south.\n")
start()
#create functions for follow, fly, teleport, and guide.