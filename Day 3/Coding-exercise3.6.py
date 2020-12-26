# Welcome to the Treasure Island Game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to the treasure island game!")
print("Your mission is to find the treasure")

direction = input("Where do you wanna go : L for left or R for right: ")

if direction == "R" or direction == "r":
   print("You fall into a deep pit.Game Over")

elif direction == "L" or direction == "l":
   decision1 = input("Do you wanna swim or wait")
   if decision1 == "Swim" or decision1 == "swim":
      print("You were eaten by a alligators. Game Over")
   elif decision1 == "Wait" or decision1 == "wait":
      decision2 = input("Which door do you wanna go : Red, Yellow or Blue -> ")
      if decision2 == "Red" or decision2 == "red":
         print("You were attacked by gangsters.Game Over")
      elif decision2 == "Blue" or decision2 == "Blue":
         print("You were eaten by a giant snake.Game Over")
      elif decision2 == "Yellow" or decision2 == "yellow":
         print("You safely got the treasure.You won the game. Congratulations")     
else:
   print("Wrong input. Play again")