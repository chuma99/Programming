import random

#Generate  a  list  of  10  random  numbers  between  0  and  100.  
randoms=[]
for i in range (10):
    randoms.append(random.randrange(1,101,1))
print(randoms)
#Get  them  in order  from  largest  to  smallest,
randoms.sort()
print(randoms)
#removing  numbers  divisible  by  3.
for i in randoms:
	if i % 3 == 0:
		randoms.remove(i)
print(randoms)


#generate a list of random prime numbers from 1 through 100
randoms=[]
for i in range (10):
    randoms.append(random.randrange(1,101,1))
print(randoms)
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


#Create  a  list  of  100  randomly  generated  3-digit  numbers.
numbers = []
first = []
for i in range(10):
	numbers.append(random.randrange(100,1000,1))
#Find  a  way  to  extract  only  the  first  digit  from  each  number,
for i in numbers:
	first[i] = int(str(numbers[i])[:1])
#and  then  arrange  the  resulting  list  in  ascending  order
first.sort()