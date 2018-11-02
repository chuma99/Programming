class BankAccount:
	def __init__(self, balance, password, number, accountType):
		self.balance = balance
		self.log = 0
		self.password = password
		self.interestRate = 0.15
		self.number = number
		self.accountType = accountType

		#methods - functions
		#Check Balance, Deposit, Withdraw, transfer, log in/log out
	def login(self):
		#if(self.log == 0):
		response = str(input("What is your bank account password? "))
		if(self.password == response):
			print("You have logged in to an account! Log out and try again.")
			self.log+=1
		else:
			print("You were unable to log into your account.")	
		#else:
		#	print("You are already logged in!")
	
	def logout(self):
		#if(self.log == 1):
		print("You have logged out of your account.")
		self.log-=1
		#else:
			#print("You not currently logged into any accounts.")

	def deposit(self, response):
		status = ""
		#if (self.log == 1):
		self.balance += response
		#else:
		#	status ="You aren't logged in!"


	def withdraw(self, response):
		status = ""
		#if (self.log == 1):
		if (self.accountType == "Checking"):
			if(self.balance >= response):
				self.balance -= response
			else:
				status = "Insufficient Funds"
		else:
			status = "You may not withdraw from this account."
		#else:
		#	status ="You aren't logged in!"
		return status

	def transfer(self, response, BankAccount):
		status = ""#self.balance += response
		#if(self.log == 1):
		if(self.balance >= response):
			self.balance -= response
			BankAccount.balance += response
		else:
			status = "Insufficient Funds."
		#else:
			status = "You aren't logged in!"
		return status
		
	def checkBalance(self):
		#if(self.log == 1):
		return self.accountType +" Balance: $" + str(self.balance)
		#else:
		#	return "You aren't logged in!"

	def getAccountType(self):
		#if(self.log == 1):
		return "Account Type: " + self.accountType
		#else:
			#return "You aren't logged in!"

	def getInterestRate(self):
		#if(self.log == 1):
		return "Interest Rate: " + self.interestRate + "%"
		#else:
		#	return "You aren't logged in!"

	def getAccountNumber(self):
		#if(self.log == 1):
		return "Account Number:" + str(self.accountNumber)
		#else:
			#return "You aren't logged in!"

	def recoverPassword(self):
		#if(self.log == 1):
		return "Password:" + str(self.password)
		#else:
			#return "You aren't logged in!"

myCheckingAccount = BankAccount(1000, "SpendMore", "123456789", "Checking")
mySavingsAccount = BankAccount(10000, "SaveMore", "987654321", "Savings")
print(myCheckingAccount.getAccountType())
print(myCheckingAccount.checkBalance())
myCheckingAccount.deposit(2000)
print(myCheckingAccount.checkBalance())
myCheckingAccount.withdraw(1500)
print(myCheckingAccount.checkBalance())
myCheckingAccount.transfer(1000, mySavingsAccount)
print(myCheckingAccount.checkBalance())
print(mySavingsAccount.checkBalance())


#for assignment, make a class, create a constructor, and implement!