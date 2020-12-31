# *********************************************************************
# ✥ Title  :- Understanding Data Types and how to manipulate strings.
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 25 December 2020
# *********************************************************************
# ✥ Program to tell remaining of life left if age is given 90.
# *********************************************************************


# In python we se round() function to round numbers.
# print(round(8 / 3,2))

# If we divide any number then he result is always floating point number
# If we want the result as integer only we can also use floor division.
# print(8 // 3)

# f-Strings
# eg - f"Your age is {age}"



age = int(input("What is your age: "))
age_left = 90 - age
days_remaining = age_left * 365
months_remaining = age_left * 12
weeks_remaining = age_left * 52

message = f"You have left {days_remaining} days, {months_remaining} months, {weeks_remaining} weeks."

print(message)

