#On my honor, I have neither given or received unauthorized aid.
#1-16-19
#For this assignment, I graphed the number of shots I would take in a week on average,
# based on the amount of practices, time spent practicing, and shots per minute I have to take them,
# and the amount of minutes it takees to make these shots.

import random
from collections import Counter
import matplotlib.pyplot as plt

#THE ARRAY IN WHICH EACH INDIVIDUAL WEEKLY TOTAL IS STORED
shotResults = []

#THE LOOP THAT GOES THROUGH EACH POSSIBILITY, ESSENTIALLY MULTIPLYING POSSIBILITIES
for j in range(10000):
	numPractices = random.randint(4,7)
	totalShots = 0
	for j in range(numPractices):
		minutesPerPractice = random.randint(30,60)
		for i in range(minutesPerPractice):
			shotsPerMinute = random.randint(6,12)
			totalShots += shotsPerMinute
	shotResults.append(totalShots)

#CREATES AN ARRAY WHICH ADDS DIMENSION TO GRAPH, MAKING THE X AXIS THE NUMBER OF SHOTS,
# AND THE Y AXIS THE NUMBER OF TRIALS WITH THIS MANY SHOTS
display = [0 for i in range(5041)]
for i in range(len(shotResults)):
	display[shotResults[i]] += 1

r = [x for x in range(5041)]
#PRINT STATEMENTS, LABELS, AND GRAPH DESIGNS
plt.bar(r,  display, color=(.5, 0.0, 0.5, 1.0))
plt.ylabel("Number of Trials")
plt.xlabel("Number of Shots")
plt.title("Shot Attempts in a Week")
plt.show()