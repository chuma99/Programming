class Dog:
	def __init__(self, energy, name):
		self.energy = energy
		self.hunger = 5
		self.weight = 30
		self.happiness = 5
		self.name = name

		#methods - functions
	def eat(self):
		status = ""
		if (self.hunger > 0):
			self.weight +=1
			self.hunger -=1
			self.energy += 1
			self.happiness +=1
			status = self.name + " just ate."
			if self.weight>40:
				self.happiness -= 3
				status += "Dog is unhappy."
		else:
			status = "Not hungry."
		return status
		
	def stats(self):
		return "Name:" + self.name + "\nHunger:" + str(self.hunger) + "\nEnergy:" + str(self.energy) + "\nHappiness:" + str(self.happiness) + "\nWeight:" + str(self.weight)

myDog = Dog(3, "Tim")
mySecondDog = Dog(8, "Annabelle")
print(myDog.stats())
print(myDog.eat())
print(myDog.eat())
print(myDog.eat())
print(myDog.eat())
print(myDog.eat())
print(myDog.eat())
print(myDog.eat())
print(myDog.stats())
#for assignment, make a class, create a constructor, and implement!