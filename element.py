import csv
import pandas as pd

class Element:
	def __init__(self, name, number, symbol, weight):
		self.name = name
		self.number = number
		self.symbol = symbol
		self.weight = weight

	def __str__(self):
		return self.name +" "+ str(self.number) +" "+ self.symbol +" "+ str(self.weight)


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
		#datafile = open('elements.csv', 'r')
		#datareader = csv.reader(datafile, delimiter=';')
		self.table = list(csv.reader(open('elements.csv', 'r')))
		#self.table = pd.read_csv(table)
		self.elementList = []
		i = 1
		while i < len(self.table):
			#self.elementList.append(Element("Hydrogen", 1, "H", 1.01))
			#self.elementList.append(Element("Helium", 2, "He", 1.07))
			self.elementList.append(str(Element(self.table[i][0], self.table[i][1], self.table[i][2], self.table[i][3])))
			if i == 103:
				break
			i+=1
			
			
		'''
		for row in self.table:
			name = row[0]
			number = row[1]
			symbol = row[2]
			weight = row[3]
			self.names.append(name)
       		self.numbers.append(number)
       		self.symbols.append(symbol)
       		self.weights.append(weight)
       		'''

	def __str__(self):
		return str()

	def findElementName(self, weight):
		for t in self.elementList:
			if t.getWeight() == weight:
				return t.getName()
	def findElementName(self, symbol):
		for t in self.elementList:
			if t.getSymbol() == symbol:
				return t.getName()

	def findElementName(self, number):
		for t in self.elementList:
			if t.getNumber() == number:
				return t.getName()

	def getElementList(self):
		return self.elementList

	def getTable(self):
		return self.table
#data = pd.read_csv("elements.csv")

#print(data)

pt = PeriodicTable("elements.csv")
#pt.printTable()
#print(pt.getElementList())
for i in pt.getTable():
	print(*i)
print(pt.getElementList())
print(pt.findElementName(1.01))
print(pt.findElementName('H'))
print(pt.findElementName(1))

# periodicTable.append(Element("Hydrogen", 1, "H", 1.01))
