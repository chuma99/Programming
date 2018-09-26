a = []

#add 2 to our list
#first element in a list is psition 0.
a+= [2]
a.append(4)
a.append(7)
a.append(1)
a.append(3)
a = [2,1,2,3,4,5] + 2


#to remove from a list
#del [:a]
#del [a:]
a.pop()
a.remove() # remove takes exactly one argument
#Removs first matching opioh
#update a value
a[4] = 7
#print the list
print(a)

print(a[3])
print(a[len(a)-1])
#or
print(a{[-1]})

#swap
a.replace(a[3], a[5])

c= 1
b = 5

temp = c
c= b
b = temp

c,b = 1,5
c,b = b,c


a[3],a[5] = a[5], a[3]
print(a)
my_list = range(0,100,7)
for i in my_list:
	print i;                                                                                                                                                                                                                                                 