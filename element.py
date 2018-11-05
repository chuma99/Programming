class BankAccount:
	def __init__(self, balance, password, number, accountType):
		self.balance = balance
		self.log = 0
		self.password = password
		self.interestRate = 0.15
		self.number = number
		self.accountType = accountType
