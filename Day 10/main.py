# **************************************************
# ✥ Title  :- Functions with outputs
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 2 January 2021
# **************************************************
# ✥ Python Calculator
# **************************************************


from art import logo
print(logo)

# Calculator functions
def add(n1,n2):
   return n1 + n2

def subtract(n1,n2):
   return n1 - n2

def multiply(n1,n2):
   return n1 * n2

def divide(n1,n2):
   return n1 / n2

operations = {
   "+" : add,
   "-" : subtract,
   "*" : multiply,
   "/" : divide
}

def calculator():
   num1 = float(input("What's the first number? "))
   for operator in operations:
      print(operator)

   should_continue = True

   while should_continue: 
      operation_symbol = input("Pick an operation from line above:- ")
      num2 = float(input("What's the next number? "))
      function = operations[operation_symbol]
      answer = function(num1,num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")

      if input(f"Do you wanna continue with the {answer}. Type 'yes' or 'no'") == "yes":
         num1 = answer
      else:
         should_continue = False
         calculator()

calculator()

