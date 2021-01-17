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


# Task 4: Draw a Spirograph
def draw(gap):
   for _ in range(int(360/gap)):
      timmy.color(random_color())
      timmy.circle(100)
      timmy.setheading(timmy.heading() + gap)

timmy.speed("fastest")
draw(5)

screen = T.Screen()
screen.exitonclick()

