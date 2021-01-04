# **************************************************
# ✥ Title  :- Black-Jack Game
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 4 January 2021
# **************************************************
# ✥ Black-Jack Game
# **************************************************


from art import logo
from os import system
import random

def deal_card():
   """Returns a random card from the deck"""
   cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
   card = random.choice(cards)
   return card

def calculate_score(cards):
   """Calculates the score of the drawn cards"""
   if sum(cards) == 21 and len(cards) == 2:
      return 0
   if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
   return sum(cards)


def compare(user_score, computer_score):
   if user_score == computer_score:
      return "It's a draw"
   elif computer_score == 0:
      return "Lose, opponent has black-jack"
   elif user_score  == 0:
      return "You win with black-jack"
   elif user_score > 21:
      return "You went over. You lose"
   elif computer_score > 21:
      return "Opponent went over you win"
   elif user_score > computer_score:
      return "You win"
   else:
      return "You lose"

def play_game():
   print(logo)
   user_cards = []
   computer_cards = []
   is_game_over = False

   for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())

   while not is_game_over:
      user_score =  calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
      print(f"  Your cards :- {user_cards}, current score :- {user_score}")
      print(f"  Computer's first card :- {computer_cards[0]}")

      if user_score == 0 or computer_score == 0 or user_score > 21:
         is_game_over = True
      else:
         user_should_deal = input("Type 'y' to get another card or 'n' to pass :- ")
         if user_should_deal == "y":
            user_cards.append(deal_card())
         else:
            is_game_over = True

   while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = computer_score(computer_cards)

   print(f"  Your final hand :- {user_cards} , final score was :- {user_score}")
   print(f"  Computer's final hand :- {computer_cards} , final score was :- {computer_score}")
   print(compare(user_score,computer_score))

while input("Do you wanna play a game of Black-Jack. Type 'y' or 'n'"):
   play_game()
   system("cls")


