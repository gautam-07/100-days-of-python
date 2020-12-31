# *********************************************************************
# ✥ Title  :- Understanding Data Types and how to manipulate strings.
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 25 December 2020
# *********************************************************************
# ✥ BMI Calculator
# *********************************************************************

height = input("enter your height in m: ")
weight = input("enter your weight in  kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)

print(bmi_as_int)