# Lists are arrays in python.
# eg- states_in_india = ["Jammu & Kashmir", "Uttrakhand", "Chattisgarh", "Delhi", "Punjab", "Haryana", "Sikkim" "etc"]

# In lists we can also use negative index like -1,-2,-3. It will then start counting from the end of the list.


# Write a program to implement Russian Roulette - Who will pay the bill?

import random

names_string = input("Give me everybody's name, seperated by a comma. ")
names = names_string.split(", ")

# we use split function to seprate string with a parameter here like (, ) and store each component individually

list_length = len(names)

random_index = random.randint(0,list_length-1)

person_pay = names[random_index]

print(f"The person who will pay is {person_pay}.")