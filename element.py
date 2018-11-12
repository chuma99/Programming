import csv
import pandas as pd

class Element:
	def __init__(self, name, number, symbol, weight):
		self.name = name
		self.number = number
		self.symbol = symbol
		self.weight = weight

	def __str__(self):
		return str()


	def getName(self):
		return self.name

	def getNumber(self):
		return self.number

	def getSymbol(self):
		return self.symbol

	def getWeight(self):
		return self.weight

class PeriodicTable:
	def __init__(self, table):
		self.names = []
		self.numbers = []
		self.symbols = []
		self.weights = []
		self.table = pd.read_csv(table)
		i = 1;
		self.elementList = []
		#holdonwhile (i < 103):
			#self.elementList.append(Element("Hydrogen", 1, "H", 1.01))
			#self.elementList.append(Element("Helium", 2, "He", 1.07))
			#holdonself.elementList.append(Element(table[i][0], table[i][1], table[i][2], table[i][3]))
			#holdoni+=1

		for row in self.table:
			name = row[0]
			number = row[1]
			symbol = row[2]
			weight = row[3]
			self.names.append(name)
       		self.numbers.append(number)
       		self.symbols.append(symbol)
       		self.weights.append(weight)

	def __str__(self):
		return str()


	def getElementList(self):
		return self.elementList

	def getTable(self):
		return self.table
#data = pd.read_csv("elements.csv")

#print(data)

pt = PeriodicTable("elements.csv")
#pt.printTable()
print(pt.getElementList())
print(pt.getTable())
# periodicTable.append(Element("Hydrogen", 1, "H", 1.01))
