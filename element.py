#11-13-18
#In this assignment, I was able to import a csv file of the elements on the periodic table, and import them into my code. From there, 
#I was able to access the elements of the file and complete tasks using them, all through user input. 
#Sources: 	https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
		#	https://introcs.cs.princeton.edu/python/32class/elements.csv
		#	https://docs.python.org/2/library/csv.html
		#	https://www.pythonforbeginners.com/csv/using-the-csv-module-in-python
#On my honor, I have neither given or received unauthorized aid. 

import csv #importing libraries that allow us to access csv files
import pandas as pd

class Element:
	def __init__(self, name, number, symbol, weight): #constructor
		self.name = name
		self.number = number
		self.symbol = symbol
		self.weight = weight

	def __str__(self): #print statement
		return self.name +" "+ str(self.number) +" "+ self.symbol +" "+ str(self.weight)

	def getName(self): #getter to access name
		return self.name

	def getNumber(self): #getter to access number
		return self.number

	def getSymbol(self): #getter to access symbol
		return self.symbol

	def getWeight(self): #getter to access weight
		return self.weight

class PeriodicTable:
	def __init__(self, table): #constructor
		self.names = []
		self.numbers = []
		self.symbols = []
		self.weights = []
		self.table = list(csv.reader(open('elements.csv', 'r')))#this imports the csv file as table
		self.elementList = []
		i = 1
		#this next part of the code is a loop that goes through elementlist and adds elements based on the dataset
		while i < len(self.table):
			self.elementList.append(Element(self.table[i][0], self.table[i][1], self.table[i][2], self.table[i][3]))
			if i == 103:
				break
			i+=1

	def __str__(self): #print statement
		result = ''
		for i in self.elementList:
			result += str(i)+'\n'
		return result

	def findElementNameByWeight(self, weight): #Enter a weight to find an element
		for t in self.elementList:
			if t.getWeight() == str(weight):
				return t.getName()

	def findElementNameBySymbol(self, symbol): #Enter a symbol to find an element
		for t in self.elementList:
			if t.getSymbol() == str(symbol):
				return t.getName()

	def findElementNameByNumber(self, number): #Enter a number to find an element
		for t in self.elementList:
			if t.getNumber() == str(number):
				return t.getName()

	def displayElement(self, name): #Enter element name to display element details.
		for t in self.elementList:
			if t.getName() == str(name):
				return t

	def atomicWeightCalculator(self, name1, name2): #Enter two element names and add their atomic weights
		weight = 0
		for t in self.elementList:
			if t.getName() == str(name1):
				weight+= float(t.getWeight())
			if t.getName() == str(name2):
				weight+= float(t.getWeight()) 
		return weight

	def getElementList(self): #Returns the element list
		return self.elementList

	def getTable(self):#Returns the csv file
		return self.table
#data = pd.read_csv("elements.csv")

#print(data)

pt = PeriodicTable("elements.csv")
#the following code is the menu that is looped through to complete the tasks mentioned above
print("Hello user, welcome to the periodic table of elements!")
print("What would you like to do here?\n")
x = 1
while x == 1:
	print("1. See all elements in the table")
	print("2. Find a specific element")
	print("3. Display an element's details")
	print("4. Calculate the weight of two elements")
	print("5. Exit\n")
	selection = input("Enter the number of the task you'd like to complete: ")
	if selection == "1":
		print("Here is the list of elements in order of atomic number.")
		print("\n"+pt)
	elif selection == "2":
		print("How would you like to find this element?\n")
		print("1. Using the atomic weight")
		print("2. Using its symbol")
		print("3. Using the atomic number\n")
		choice = input("Enter the number of your choice: ")
		if choice == "1":
			weight = float(input("Enter the atomic weight of the element you wish to find: "))
			print("\n"+pt.findElementNameByWeight(weight))
		elif choice == "2":
			symbol = str(input("Enter the symbol of the element you wish to find: "))
			print("\n"+pt.findElementNameBySymbol(symbol))
		elif choice == "3":
			number = int(input("Enter the atomic number of the element you wish to find."))
			print("\n"+pt.findElementNameByNumber(number))
	elif selection == "3":
		element = str(input("What is the name of the element who's details you would like to display? "))
		print("\n"+pt.displayElement(element))
	elif selection == "4":
		element1 = str(input("Please enter the first element you would like to add: "))
		element2 = str(input("Please enter the second element you would like to add: "))
		print("Adding elements atomic weights...")
		print("\nThe atomic weights of these elements add up to "+ str(pt.atomicWeightCalculator(element1, element2)) + "!\n")
	elif selection == "5":
		print("You have exited the periodic table of elements!")
		x=2
	else: 
		print("Your input was invalid. Please try again.")

