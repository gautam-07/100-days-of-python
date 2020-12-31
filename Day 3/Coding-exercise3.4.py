# ******************************************************
# ✥ Title  :- Control flow and logical operators
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 26 December 2020
# ******************************************************
# ✥ Python Pizza Calculator.
# ******************************************************
# Small Pizza - $15
# Medium Pizza - $20
# Large Pizza - $25
# Pepperoni for small pizza - +$2
# Pepperoni for medium or large - +$3
# Extra cheese for any size pizza - +$1
# ******************************************************


print("Welcome to the Python Pizza Deliveries")
size = input("What size pizza do you want: S, M, L -> ")
pepperoni = input("Do you want pepperoni: Y or N -> ")
cheese = input("Do you want extra cheese : Y or N -> ")

if size == "S" or size == "s":
   bill = 15
   if pepperoni == "Y" or pepperoni == "y":
      bill+=2
   if cheese == "Y" or cheese == "y":
      bill+=1

elif size == "M" or size == "m":
   bill = 20
   if pepperoni == "Y" or pepperoni == "y":
      bill+=3
   if cheese == "Y" or cheese == "y":
      bill+=1

elif size == "L" or size == "l":
   bill = 25
   if pepperoni == "Y" or pepperoni == "y":
      bill+=3
   if cheese == "Y" or cheese == "y":
      bill+=1

print(f"Your total bill is ${bill}. Enjoy your pizza")
   

   
