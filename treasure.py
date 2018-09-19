def start():
	response = input("Greetings! You are looking for treasure.\n Your map says that the treasure can be found northerly.\n However, your friend says he heard someone talking about treasure in the south.\n Do you 1) Trust your Friend, or 2) Trust the Map?\n")
	if response == "1":
		friend()
	elif response == "2":
		map()
	else:
		print("You must type 1 or 2. Please try again.")
		start()
start()
def map():
	response = input("The treasure is north of Mt. Everest! Would you like to 1) follow the map, or 2) teleport within 2 miles and search yourself?")
	if response == "1":
		teleport()
	elif response == "2":
		guide()
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
#create functions for follow, fly, teleport, and guide.