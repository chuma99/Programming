#On my honor, I have neither given or received unauthorized aid.
#3-1-19
#Monte Carlo simulations are used to model the probability of different outcomes 
#in a process that cannot easily be predicted because of random variables. 
#It helps create graphs that forecast possible future events 
#using an array of occurence combinations. 

#For this assignment, I graphed the number of shots I would take in a week on average,
# 
# 

import random
from collections import Counter
import matplotlib.pyplot as plt

#THE ARRAY IN WHICH EACH INDIVIDUAL WEEKLY TOTAL IS STORED
dartResults = []

#THE LOOP THAT GOES THROUGH EACH POSSIBILITY, ESSENTIALLY MULTIPLYING POSSIBILITIES
for j in range(100):
	hitsBox = random.uniform(1.0,4.0)
	totalHits = 0
	#if it hits the circle
	if hitsBox < 3.14 and hitsBox > 1:
		totalHits+=1
	if totalHits==0:
		hit = "No"
	else:
		hit = "Yes"
	dartResults.append(totalHits)

#CREATES AN ARRAY WHICH ADDS DIMENSION TO GRAPH, MAKING THE X AXIS THE NUMBER OF SHOTS,
# AND THE Y AXIS THE NUMBER OF TRIALS WITH THIS MANY SHOTS
display = [0 for i in range(100)]
for i in range(len(dartResults)):
	display[dartResults[i]] += 1

r = [x for x in range(100)]
#PRINT STATEMENTS, LABELS, AND GRAPH DESIGNS
plt.bar(r,  display, color=(0.5, 0.0, 0.5, 1.0))
plt.ylabel("Number of Trials")
plt.xlabel("Thrown Within Circle?")
plt.title("Chart of Darts that Hit Box")
plt.show()