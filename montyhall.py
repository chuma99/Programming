#Chuma Azinge
#Honor Code: I have neither given nor received unauthorized aid
#Within this code I have created a class in which I run the 
#Monty Hall simulation and print out the results 


import random

class MontyHall:
	def __init__(self):
		self.prizeDoor = self.pickDoor()
		self.selectedDoor = None
		self.removedDoor = None
	#This funtion was created in order to start the simulation
	def pickDoor(self):
		return random.randint(1,3)
	#This sets the door as what picked in the two simulations
	def selectDoor(self):
		self.selectedDoor = self.pickDoor()
	#This step of the simulation takes one of the three doors out of play 
	def removeDoor(self):
		d = self.pickDoor()
		while d == self.selectedDoor or d == self.prizeDoor:
			d = self.pickDoor()
		self.removedDoor = d
	#This step happens in the simulation where the user switches doors.
	#Should theoretically change odds
	def switchChoice(self):
		self.selectedDoor = 6-self.selectedDoor-self.removedDoor
	#The simulation should win out regardless
	def userWins(self):
		if self.selectedDoor == self.prizeDoor:
			return True
		else:
			return False
	#This starts the simulation and calls the functions created above
	def runGame(self, switch=True):
		self.selectDoor()
		self.removeDoor()
		if switch:
			self.switchChoice()
		return self.userWins()

wins = 0
losses = 0

for i in range(1000):
	#make an instance of the game, "m"
	m = MontyHall()
	#run the game and switch choice of door.
	if m.runGame(switch=True):
		#run the game and switch choice of door.
		wins += 1
	else:
		#a return value of False means we've lost
		losses+=1

percentWin = 100.0*wins / (wins+losses)

print("\nOne thousand Monty Hall games (with switching):")
print(" won:", wins, "games")
print(" lost:", losses, "games")
print(" odds: %.2f%% winning percentage" % percentWin)

wins = 0
losses = 0

for i in range(1000):
	#make an instance of the game, "m"
	m = MontyHall()
	#run the game and switch choice of door.
	if m.runGame(switch=False):
		#run the game and switch choice of door.
		wins += 1
	else:
		#a return value of False means we've lost
		losses+=1

percentWin = 100.0*wins / (wins+losses)

print("\nOne thousand Monty Hall games (staying with the original choice):")
print(" won:", wins, "games")
print(" lost:", losses, "games")
print(" odds: %.2f%% winning percentage" % percentWin)
