import sys

a = float(sys.argv[1])

if a.replace('.','',1).isdigit():
	if 5>=a>=0:
		if 1.0>a>=0:
			print("F")
		elif 1.5>a>=1.0:
			print("D-")
		elif 2.0>a>=1.5:
			print("D")
		elif 2.5>a>=2.0:
			print("D+")
		elif 2.85>a>=2.5:
			print("C-")
		elif 3.2>a>=2.85:
			print("C")
		elif 3.5>a>=3.2:
			print("C+")
		elif 3.85>a>=3.5:
			print("B-")
		elif 4.2>a>=3.85:
			print("B")
		elif 4.5>a>=4.2:
			print("B+")
		elif 4.7>a>=4.5:
			print("A-")
		elif 4.85>a>=4.7:
			print("A")
		elif 5.0>=a>=4.85:
			print("A+")
	else:
		print("Expecting a number between 0 and 5")
else:
	print("Expecting a number between 0 and 5")