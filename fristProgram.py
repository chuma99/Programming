# comment
# homework is to write a program that has a conversation with you
# python3 vs python

hometown = input("Hello, " +username+ "! Where are you from?\n")
grade = input("Awesome, what grade are you in?\n")
returner = input(grade+ " graders are the coolest! Were you a student at Choate last year?\n")
if returner == "yes":
 print("That's cool, " +username+ ". Congratulations on making it this far, and good luck for the rest of this year!")
elif returner == "no":
 print("Glad that you've come to join us, " +username+ ". It was fun speaking with you, and I'm sure you'll meet many other " +grade+ " graders soon!")
else:
 print("Okay cool!")