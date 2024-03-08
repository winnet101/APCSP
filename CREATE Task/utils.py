from turtle import Turtle

def quickmove(t:Turtle, x:int, y:int):
  '''Moves the turtle to a given location without pen.
  Shorthand for `t.penup()` `t.pendown()`.'''
  t.penup()
  t.goto(x, y)
  t.pendown()

def draw_rect(t:Turtle, x:int, y:int, width:int, height: int | None = None):
  '''Draws a rectangle.
  :returns: An array containing its boundaries (`[left, up, right, down]`).'''
  if height == None:
    height = width
  
  t.hideturtle()
  t.penup()
  t.seth(0)
  t.goto(x, y)
  t.backward(width/2)
  t.left(90)
  t.backward(height/2)
  t.pendown()

  t.begin_fill()

  walls:list[float] = []

  for i in range(2):
    walls.append(t.xcor())
    t.forward(height)
    t.right(90)

    walls.append(t.ycor())
    t.forward(width)
    t.right(90)
  
  t.end_fill()

  return walls
