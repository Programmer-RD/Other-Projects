import time
import random
Com = 0
Hum = 0
print(" <> ! | Welcome to Rock Paper Scissors | ! <> ")
T = input(" > What is your Name ? \n > ")
time.sleep(0.30)
How_many_times = int(input(" > How many times do you want to play |Rock|Paper|Sicssors| \n > "))
print(" > |CPU|Repl| ")
print(" > CPU = Easy ")
print(" > Repl = Hard ")
S = input(" > From What do you want to play ? \n > ")
for X in range(0,How_many_times) :
	if (S == "CPU" or "cpu") :
		print(" > ! Lets play ! ")
		K = input(" > Enter the ( Rock or Scissors or Paper )")
		Z = random.choice(["Rock","Scissors","Paper"])
		print(f" \n > Computer = {Z} vs User = {K} \n ")
		if Z == K :
			print(" > ! Tie ! ")
		else :
			if (Hum - Com) % 3 == 1 :
				Com += 1
				print(f" > Computer score : {Com}")
			elif (Hum - Com) % 3 == 2 or 3 :
				Hum += 1
				print(f" > User score : {Hum}")
			else :
				print("An error occured")
				print("Please try again")
for i in range(0,How_many_times) :
	print(" > ! Lets play ! ")
	N = input(" > Enter the ( Rock or Scissors or Paper ) \n > ")
	M = random.choice(["Rock","Scissors","Paper","rock","paper","rock"])
	print(f" \n > Computer = {M} vs User = {N} \n ")
	if N == M :
		print(" > ! Tie ! ")
	else :
		if (Hum - Com) % 3 == 1 :
			Com += 1
			print(f" > Computer score : {Com}")
		elif (Hum - Com) % 3 == 2 or 3 :
			Hum += 1
			print(f" > User score : {Hum}")
		else :
			print(" > An error occured")
			print(" > Please try again")
print(f" > User : {Hum}")
print(f" > Computer : {Com}")
if Hum < Com :
	print(" > You lose")
elif Hum > Com :
	print(" > You win ! ")
elif Hum == Com :
	print(" > its a tie ! ")
print(" > Thank you for using our programm...")
print(f" > Goodbye {T} See you later...")