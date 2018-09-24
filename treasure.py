#start begins the game
def start():
	response = input("Do you 1) Trust your Friend, or 2) Trust the Map?\n")
	if response == "1":
		friend()
	elif response == "2":
		map()
	else:
		print("You must type 1 or 2. Please try again.")
		start()

#map can show a map or teleport the player
#in future, should print a map
def map():
	response = input("The treasure is north of Mt. Everest! Would you like to 1) follow the map, or 2) teleport within 2 miles and search yourself?")
	if response == "1":
		guide()
	elif response == "2":
		teleport()
	else:
		print("You must type 1 or 2. Please try again.")
		map()

#friend can guide or purchase plane ticket for the player
def friend():
	response = input("I heard the treasure is south of Mt. Everest. Do you 1) want me to guide you, or 2) want me to purchase you a plane ticket to Mt. Everest?")
	if response == "1":
		follow()
	elif response == "2":
		fly()
	else:
		print("You must type 1 or 2. Please try again.")
		friend()

#guide can be followed or interpretted
def guide():
	print("Here is a map that will lead you straight to the treasure. ")
	response = input("Would you like to 1) spend time interpretting the map, or 2) begin along the path?")
	if response == "1":
		print("You have been able to accurately interpret the map, and after walking towards it you've located the treasure")
		chest()
	elif response == "2":
		print("You have overwalked the treasure and are now disoriented. You rip up your map in frustration, and return home.")
		restart()
	else:
		print("You must type 1 or 2. Please try again.")
		guide()

#final option
def chest():
	response = input("Would you like to 1) open the chest or 2) pick up the chest and carry it home?")
	if response == "1":
		print("You have opened the chest and found out that the treasure was the journey all along!")
		print("Congratulations on finishing the game!")
		restart()
	elif response == "2":
		print("After trying to carry it over your head, the chest falls from your hands and is destroyed. Game over.")
		restart()
	else:
		chest()
#teleport can only lead to death
#in future, should have randomizer determining outcome of landing
def teleport():
	print("You were teleported to the top of mount Everest, and due to your unprepared state, you have now frozen to death. ")
	restart()

#follow can take you down the rocky road or up the hill
def follow():
	print("You have chosen to follow your friend, and at a crossroad, he is unsure which direction to take, so he asks you to help.")
	response = input("Would you like to 1) go down the rocky road, or 2) scale a hill in the opposite direction?")
	if response == "1":
		print("By chosing to travel down the rocky road, you have committed to a path of which the end is unforseeable.")
		road()
	elif response == "2":
		print("By partially scaling the hill, you have gained an advantageous view of the area. You can now see a clear path to the treasure.")
		clearview()
	else:
		print("You must type 1 or 2. Please try again.")
		follow()


#Road
def road():
	response = input("Would you like to 1) turn back or 2) continue down the rocky road?")
	if response == "1":
		print("You chose to turn back and when you turn around, you notice that you're trail has dissapeared. You are lost. Game Over.")
		restart()
	elif response == "2":
		print("By continuing down rocky road, you find yourself walking through a neverending circle. Eventually, you dehydrate. Game over. ")
		restart()
	else:
		print("You must type 1 or 2. Please try again.")
		road()


#clear view
def clearview():
	response = input("Would you like to 1) follow this path or 2) continue scaling the hill?")
	if response == "1":
		print("By following the path, you are able to succesfully locate the chest.")
		chest()
	elif response == "2":
		print("Attempting to climb higher on the hill, you lose grip and plummet to your death. Game Over. ")
		restart()
	else:
		print("You must type 1 or 2. Please try again.")
		clearview()

#fly takes you to the airport
def fly():
	print("Your plane has landed at the airport closest to mount Everest. You get out of the plane and exit the airport. ")
	response = input("Would you like to 1) call an uber to mount Everest, or 2) take a taxi?")
	if response == "1":
		print("By chosing to travel via uber, you get to the destination much later than planned.")
		rate()
	elif response == "2":
		print("By chosing to travel via taxi, you are now being asked to fork over all of the cash you have, because you could not cover the fare.")
		run()
	else:
		print("You must type 1 or 2. Please try again.")
		fly()


#run allows the player to decide whether to abide or not
def run():
	response = input("Would you like to 1) run away and try to evade the taxi driver or 2) give up all of your money?")
	if response == "1":
		print("You chose to run and evade the taxi driver, but he calls the police instead of chasing you. You are caught and arrested. Game over.")
		restart()
	elif response == "2":
		print("By chosing to give up all your money, the driver decides that he would pay you back by awarding you with the chest.")
		chest()
	else:
		print("You must type 1 or 2. Please try again.")
		run()

#rate allows the user to rate its driver
def rate():
	response = input("Would you like to 1) tip your driver, or 2) exit and give him a bad rating?")
	if response == "1":
		print("By chosing to tip your driver, you have been hit with good karma, and you were magically presented with a chest.")
		chest()
	elif response == "2":
		print("By chosing to give your driver a bad rating, you have been hit with bad karma, and you are hit by a bad driver on your way off. Game Over.")
		restart()
	else:
		print("You must type 1 or 2. Please try again.")
		rate()
		
#restart asks the user whether to restart the game
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


print("Greetings! You are looking for treasure.\nYour map says that the treasure can be found northerly.\nHowever, your friend says he heard someone talking about treasure in the south.\n")
start()
#create functions for follow, fly, teleport, and guide.