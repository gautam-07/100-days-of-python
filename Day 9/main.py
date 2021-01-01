# **************************************************
# ✥ Title  :- Dictionaries and Nesting
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 1 January 2021
# **************************************************
# ✥ Secret Auction Program
# **************************************************

from art import logo
from os import system
print(logo)
print("Welcome to Secret Auction")

total_biddings = {}
bidding_finished = False

# Finding highest bidder
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]

    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder

  print(f"The highest bidder is {winner} with a bid of {highest_bid}")

# Biddings 
while not bidding_finished:
  name = input("What is your name:- ")
  bid_price = int(input("What is your bid price:- $ "))

  total_biddings[name] = bid_price
  user_input = input("Are there any other bidders? Type 'yes' or 'no' :- ")

  if user_input == "no":
    bidding_finished = True
    find_highest_bidder(total_biddings)

  elif user_input == "yes":
    system('cls')
  
