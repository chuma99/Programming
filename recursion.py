def fact(n):
	if n == 0 or n == 1:
		return 1
	return n * fact(n-1)

print(fact(5))

x = fact(1)

	#recursion and how it works
	#learned 

def fibonacci(n):
	if n == 0 or n == 1:
		return n
	return fibonacci(n-2) + fibonacci(n-1)

print(fact(5))
print(fibonacci(5))