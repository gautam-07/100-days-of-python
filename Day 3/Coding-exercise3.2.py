# Write a program that calculates BMI based on user's inputed weight and height

height = float(input("Enter you height: "))
weight = float(input("Enter your height"))

bmi = round(weight / height**2)

if bmi < 18.5:
   print(f"Your bmi is {bmi}.\nYou are underweight")
elif bmi < 25:
   print(f"Your bmi is {bmi}.\nYou are normal weight")
elif bmi < 30:
   print(f"Your bmi is {bmi}.\nYou are overweight")
elif bmi < 35:
   print(f"Your bmi is {bmi}.\nYou are obese")
else:
   print(f"Your bmi is {bmi}.\nYou are clinically underweight")

