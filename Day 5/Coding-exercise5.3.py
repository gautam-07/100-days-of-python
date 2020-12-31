# ******************************************************
# ✥ Title  :- Python loops
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 28 December 2020
# ******************************************************
# ✥ Program to calculate the sum of all even numbers 
#   1-100 including 1 and 100
# ******************************************************

# For loops with range()
#eg - for number in range(1, 10, 3):
#        print(number)
# 1 - 10 is the range and 3 is the step size for this range.

sum_even = 0
for even in range(0,101,2):
   sum_even += even

print(f"The sum of even numbers b/w 1 and 100 is {sum_even}")