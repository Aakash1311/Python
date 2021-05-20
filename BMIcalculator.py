#BMI calculator  

height = float(input("Enter you Height in cm:"))
weight = float(input("Enter you Weight in kg:"))
heightinm = height/100;
BMI = weight /(heightinm * heightinm)
print(BMI)
if BMI	<= 18.5:
	print("You are UnderWeight")
elif BMI <= 25:
	print("Congrats you are having Normal weight")

elif BMI <= 30:
	print("Overweight")

elif BMI <= 35:
	print("Class I Obesity")

elif BMI <= 40:
	print("Class II Obesity")

elif BMI > 40:
	print("Class III Obesity")

else:
	print("Something went wrong ! Retry....") 	
		

	

