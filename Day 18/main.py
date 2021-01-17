# ✥ Title  :- The Graphical User Interface
# ✥ Author :- Gautam Khatter 🧐
# ✥ Date   :- 17 January 2021
# **************************************************
# ✥ Turtle Module
# **************************************************



import turtle as T
import random

timmy = T.Turtle()
T.colormode(255)

def random_color():
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0, 255)
   color = (r, g, b)
   return color


# Task 1: Drawing dashed line
# for _ in range(15):
#    timmy.forward(10)
#    timmy.penup()
#    timmy.forward(10)
#    timmy.pendown()




# Task 2: Draw Different shapes
# timmy.pensize(3)
# timmy.speed("slowest")
# def draw(sides):
#    angle = 360 / sides
#    for _ in range(sides):
#       timmy.forward(100)
#       timmy.right(angle)

# for n in range(3, 11):
#    timmy.color(random_color())
#    draw(n)




# Task 3: Draw a random walk
# directions = [0, 90, 180, 270]
# timmy.pensize(14)

# for _ in range(200):
#    timmy.color(random_color())
#    timmy.forward(30)
#    timmy.setheading(random.choice(directions))



# Task 4: Draw a Spirograph
# def draw(gap):
#    for _ in range(int(360/gap)):
#       timmy.color(random_color())
#       timmy.circle(100)
#       timmy.setheading(timmy.heading() + gap)

# timmy.speed("fastest")
# draw(5)


screen = T.Screen()
screen.exitonclick()
