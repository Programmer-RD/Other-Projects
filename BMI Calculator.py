#BMI calculator
Password = "Ranuga"
password = input(" > Enter the Password.... \n > ")
while password != Password:
	Password = input(" > Enter the password....")
Email = int,str(input(" > Enter your email please...."))
print("Please enter the information that the questions ask down below Thank you")
print(" Welcome to BMI calculator. ")
Name = input(" What is your name : ")
Height = int(float(input(" What is your Height : ")))
Weight = int(float(input(" What is your weight : ")))
Unit = input(" Lbs or Kg : ")
unit = input(" ft or m :")
if len(Name) < 2:
  print("Name must be more than 2 Letters")
elif len(Name) > 25 :
  print("Name must be less than 25 letters.")
else :
   print("Name is looking perfect.")

#Kg turned into Lbs
if Unit.upper() == "Lbs" :
  converted = Weight * 0.45
  print( f" You are {converted} pounds. ")
#Lbs turned into kg
  if Unit.upper() == "Kg" :
    convert = Weight / 0.45
    print( f" You are {convert} kg ")
#Meeters into foot
if unit.upper() == "ft" :
  conver = Height * 3.28
  print( f" You are {conver} Meeters ")
#foot into meeters
  if unit.upper() == 'm' :
    conve = Height / 3.28
    print( f" You are {conve} foot ")
#BMI calculations
BMI = Weight / (Height ** 2)

if BMI > 25 :
  print( Name )
  print(" You are not over weight or under weight. ")
  print(" Congratulations ! ")

elif BMI > 25 :
  print( Name )
  print(" You are under weight. ")

elif BMI == 25 :
  print( Name )
  print(" Your BMI is in the middle of under weight and over Weight ")

else :
  print( Name )
  print(" You are over Weight ")
print("BMI : ")
print( BMI )
print(""" Thank you for using this website,
 Hope that you enjoyed it
 Thank you !. """)
print(" <> programm Finished <> ")
#
