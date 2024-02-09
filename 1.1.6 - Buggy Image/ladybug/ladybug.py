#   a116_ladybug.py
import turtle as trtl

ladybug = trtl.Turtle()
ladybug.speed(0)

def moveUp(x, y):
  ladybug.penup()
  ladybug.goto(x,y)
  ladybug.pendown()

legs = 6
angle = 180/legs
ladybug.pencolor("black")
ladybug.pensize(4)


for i in range(legs):
  moveUp(0,-55/2)
  newangle = angle * (i)
  if i < 3:
    print("i =", i)
    print(newangle - 45)
    ladybug.setheading(newangle - 30)
  else:
    print(newangle + 45)
    ladybug.setheading(newangle + 60)
  ladybug.forward(55)


# create head
moveUp(0,0)
ladybug.setheading(0)
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()