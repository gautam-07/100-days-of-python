# ******************************************************
# ✥ Title  :- Python loops
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 28 December 2020
# ******************************************************
# ✥ Program to calculate average heights
# ******************************************************

student_height = input("Enter a list of student heights: ").split()

for n in range(0, len(student_height)):
   student_height[n] = int(student_height[n])
print(student_height)

total_item = 0
total_height = 0

for student in student_height:
   total_item += 1

for height in student_height:
   total_height += height

average_height = round(total_height / total_item)

print(f"The average height of students is : {average_height}")