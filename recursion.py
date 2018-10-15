def fact(n):
	if n == 0 or n == 1:
		return 1
	return n * fact(n-1)

#print(fact(5))

x = fact(1)

	#recursion and how it works
	#learned 

def fibonacci(n):
	if n == 0 or n == 1:
		return n
	return fibonacci(n-2) + fibonacci(n-1)

##print(fibonacci(5))

	#Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

def countX(n):
	n = n.lower()
	count = 0
	if len(n) != 0:
		if n[0][0] == "x":
			count+1

	else:
		return count
	return 

def moves(n,  left):
	if n ==0:
		return
	moves(n-1,not  left)
	if  left:  
		print(str(n)+'  left')
	else:    
		print(str(n)+'  right')
	moves(n-1,not  left) 

moves(4,True)

