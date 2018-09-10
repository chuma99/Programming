import sys
#https://www.pythonforbeginners.com/system/python-sys-argv where I found the value of position 0.
if len(sys.argv) == 1:
	print("Greetings, " + sys.argv[1] + "!")
elif len(sys.argv) == 2:
 	print("Greetings, " + sys.argv[1] + "and " + sys.argv[2] + "!")
elif len(sys.argv) == 3:
 	print("Greetings, " + sys.argv[1]+ ", " +sys.argv[2]+ ", and " + sys.argv[3] + "!")