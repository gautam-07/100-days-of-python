# Make a rock, paper, scissors game.
import random

rock = '''
     (_____)
      (_____)
      (____)
---.   _______
---'   ____)
  __(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
RPS = [rock,paper,scissors]

user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))

if user_choice >= 3 or user_choice < 0:
   print("You type an invalid number")

else:
   print(RPS[user_choice])

   computer_choice = random.randint(0,2)
   print("Computer choose: ")
   print(RPS[computer_choice])

   if user_choice == 0 and computer_choice == 2:
      print("You won")
   elif computer_choice == 0 and user_choice == 2:
      print("You lose")
   elif computer_choice > user_choice:
      print("You lose")
   elif user_choice > computer_choice:
      print("You won")
   elif computer_choice == user_choice:
      print("Its a draw")






