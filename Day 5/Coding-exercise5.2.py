# ******************************************************
# ✥ Title  :- Python loops
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 28 December 2020
# ******************************************************
# ✥ Program to calculate highest score from a list
# ******************************************************

score_list = input("Enter a list of score: ").split()

for n in range(0,len(score_list)):
   score_list[n] = int(score_list[n])
print(score_list)

highest = 0
for score in score_list:
   if score > highest:
      highest = score

print(f"The highest score among given scores is : {highest}")

