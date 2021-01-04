#The Start of the programm
import time
print(" > |!Welcome to the Even or odd Calculator !| < ")
X = input(" > What is your Name ? ")
How_Many_Time = int(input(" > How many times do you want to Check weather it is even or odd ? "))
for i in range(0,How_Many_Time) :
	enterAone  = int(input(" > What is the Number ? \n > "))
	E = enterAone  %  2
	if E == 0 :
		print(f" > {enterAone} is a even Number ")
		time.sleep(0.30)
	elif E == 1 :
		print(f" > {enterAone} is a odd Number " )
		time.sleep(0.30)
	else :
		print(" > An error occured...")
		print(" > Try again later...")
print(f"Have Nice Day {X}")
print("See you later")
#The end of the programm