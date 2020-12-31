# ******************************************************
# ✥ Title  :- Control flow and logical operators
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 26 December 2020
# ******************************************************
# ✥ Program to check whether a number is leap or not.
# ******************************************************

year = int(input("Enter a year: "))

if year % 4 == 0:
   if year % 100 == 0:
      if year % 400 == 0:
         print("It is a leap year")
      else:
         print("Not a leap year")
   else:
      print("It is a leap year")
else:
   print("Not a leap year")