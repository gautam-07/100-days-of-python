# Nested Lists are 2d arrays of python

# fruits = ["Strawberries","Apples","Grapes","Cherries"]
# vegetables = ["Spinach","Kale","Tomatoes","Potatoes"]
# dirty_dozen = [fruits , vegetables]


#Treasure Map Exercise
# Write a program that will mark a spot with an 'X'.

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you wanna put the treasure? ")

vertical = int(position[0])
horizontal = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}\nYour Treasure was stored successfully")