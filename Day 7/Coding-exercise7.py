# ******************************************************
# ✥ Title  :- Hangman Game
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 30 December 2020
# ******************************************************
# ✥ Save the man from hanging!
# ******************************************************


from os import system
import random
from hangman_words import word_list
from hangman_art import stages,logo


lives = 6
print(logo)
print("\nGuess the correct letter and complete the word to change the man's fate")
print("You have 6 lives to do this!")

end_of_game = False
chosen_word = random.choice(word_list)  # Making a random choice from word_list
word_length = len(chosen_word)

# Making a list in which there will be blanks "_" as much as there is letters in the chosen_word.
# e.g - If chosen_word == "apple" then display list should be like display = ["_","_","_","_","_"]

display = []
for _ in range(word_length):
   display += "_"
print(display)

# Using loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen word and "display" has no more blanks "_".Then you can tell the user that they have won.

while not end_of_game:
   print(f"\nNo of lives left : {lives}")
   guess = input("Guess a letter").lower()
   system('cls')

   # If the user has entered a letter they have already guessed, print the letter and let them know.
   if guess in display:
      print(f"You have already guessed {guess}")

   # Loop through each position in the chosen_word;
   # If the letter at the position matches "guess" then reveal that letter in the display at that position.
   # e.g- If the user guessed "p" and the chosen word was "apple", then display should be ["_","p","p","_","_"].

   for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
         display[position] = letter
   
   if guess not in chosen_word:
      # If the letter is not in the chosen word print out the letter and let them know its not the letter
      if guess not in display:
         print(f"You guessed {guess}, that's not in the word . You lose a life")
      lives -= 1
      if lives == 0:
         end_of_game = True
         print("You lose")

   # Print "display" and you should see the guessed letter in the correct position and every other letter replace with "_"

   print(display)
   if "_" not in display:
      end_of_game = True
      print("You win")

   print(stages[lives])


