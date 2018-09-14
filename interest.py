import math as m
i = float(input("Input your investment: "))
r = float(input("Input your interest rate: "))
y = float(input("How many years would you like to invest for?: "))

A = i*m.e(r)(y)
print("In the next", y + "years, your investment will be worth", A + "dollars.")