# **************************************************
# ✥ Title  :- Function Parameters
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 31 December 2020
# **************************************************
# ✥ Check whether a number is prime or not.
# **************************************************


n = int(input("Enter a number:- "))

def prime_checker(number):
   is_prime = True
   for num in range(2,number):
      if number % num == 0:
         is_prime = False
   if is_prime:
      print("It's a prime number")
   else:
      print("It's not a prime number")

prime_checker(number=n)

