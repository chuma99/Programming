import math as m
i = float(input("Input your investment: "))
r = float(input("Input your interest rate: "))
y = float(input("How many years would you like to invest for?: "))

A = float(i*(m.e)**(r*y))
print("Future investment value:", A)