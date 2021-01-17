import turtle as T

# Task 1: Drawing dashed line
timmy = T.Turtle()
for _ in range(15):
   timmy.forward(10)
   timmy.penup()
   timmy.forward(10)
   timmy.pendown()

screen = T.Screen()
screen.exitonclick()

