import random

randoms=[]
for i in range (10):
    randoms.append(random.randrange(1,101,1))
print(randoms)

randoms.sort()
print(randoms)

for i in randoms:
	if i % 3 == 0:
		randoms.remove(i)
print(randoms)



#generate a list of prime numbers from 1 through 100
#should print 1,2,3,5,7

for i in randoms:
	if i % 2 == 0:
		randoms.remove(i)
	elif i % 3 == 0:
		randoms.remove(i)
	elif i % 5 == 0:
		randoms.remove(i)
	elif i % 7 == 0:
		randoms.remove(i)
print(randoms)