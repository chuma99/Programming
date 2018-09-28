import random

randoms=[]
for i in range (10):
    randoms.append(random.randrange(1,101,1))
print(randoms)

randoms.sort()
print(randoms)

for i in range(10):
	
	three = randoms[i]/3
	if isinstance(three, int):
		del randoms(i)



#generate a list of prime numbers from 1 through 100
#should print 1,2,3,5,7

for i in range (10):
	two = randoms[i]/2
	three = randoms[i]/3
	five = randoms[i]/5
	seven = randoms[i]/7

	if isinstance(two, int):
		randoms.remove(i)
	elif isinstance(three, int):
		randoms.remove(i)
	elif isinstance(five, int):
		randoms.remove(i)
	elif isinstance(seven, int):
		randoms.remove(i)
print(randoms)