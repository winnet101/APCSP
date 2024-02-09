#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

startx = 0
starty = 0
startdir = 90
forward = 5
i = 0

for s in range(100):
  tshape = turtle_shapes[s%6]
  print(tshape)
  t = trtl.Turtle(shape=tshape)
  my_turtles.append(t)
  t.speed=(0)
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  color = turtle_colors[i%6]
  print(color)
  t.pencolor(color)
  t.fillcolor(color)
  t.setheading(startdir)
  t.right(45)     
  t.forward(forward)
  i += 1
  startx = t.xcor()
  starty = t.ycor()
  startdir = t.heading()
  forward += 5

# set start position


# code run in each turtle
  

#	each successive turtle offsets the next by 50
  

wn = trtl.Screen()
wn.mainloop()