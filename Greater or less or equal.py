import time
print(" > |!Welcome to Greater or equal or less Calculator!| < ")
time.sleep(0.30)
Name = input(" > What is your Name ? ")
How_Much = int(input(" > How many times do you want to see which it is greater or less or equal"))
for i in range(0,How_Much) :
	entersone = int(input(" > Enter First Number... \n > "))
	enterstwo = int(input(" > Enter Second Number... \n > "))
	if entersone > entersone :
		print(f" > {entersone} is greater than {enterstwo}... ")
	elif entersone < enterstwo :
		print(f" > {enterstwo} is greater than {entersone}... ")
	elif entersone == enterstwo :
		print(f" > {entersone} and {enterstwo} are equal... ")
	else :
		print(" > An error occured...")
		print(" > Try again later...")
print(f"Bye {Name}")
print("See you later..")