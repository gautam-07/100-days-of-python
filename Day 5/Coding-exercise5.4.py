# ******************************************************
# ✥ Title  :- Python loops
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 28 December 2020
# ******************************************************
# ✥ FizzBuzz Game
# ******************************************************

# The fizz buzz game is a simple game in which if a multiple of 3 occurs we say "fizz" and if a multiple of 5 occurs we day "buzz" and if there is a number whose multiple is both 3 and 5 we say "fizzbuzz".

for number in range(1,101):
   if number%3==0 and number%5==0:
      print("FizzBuzz")
   elif number%3==0:
      print("Fizz")
   elif number%5==0:
      print("Buzz")
   else:
      print(number)    