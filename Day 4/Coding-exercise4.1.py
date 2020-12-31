# ******************************************************
# ✥ Title  :- Randomisation and Python Lists
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 27 December 2020
# ******************************************************
# ✥ Introduction to random module
# ******************************************************

import random

# random_integer = random.randint(1,10)
# print(random_integer)

# # Increasing the limit of random from [0,1).
# random_float = random.random() * 5
# print(random_float)


#  Write a program that tells users if its heads or tails randomly.

toss = random.randint(0,1)
if toss == 0:
   print("Heads")
elif toss == 1:
   print("Tails")




