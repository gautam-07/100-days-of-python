# **************************************************
# ✥ Title  :- Function Parameters
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 31 December 2020
# **************************************************
# ✥ Paint Area Calculator
# **************************************************

import math
test_h = int(input("Enter the height of the wall:- "))
test_w = int(input("Enter the width of the wall:- "))

coverage = 5

def paint_calc(height,width,cover):
   # Ceil function rounds UP the number and is imported from math module.
   cans = math.ceil((height*width)/cover)
   print(f"The total number of cans to buy are {cans}")

paint_calc(height=test_h, width=test_w, cover=coverage)

