# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random as rand

#-----game configuration----
size = 3
shape = "circle"
spotColor = "pink"
score = 0
font = ("Arial", 20, "normal")
timer = 5
counterInterval = 1000  # 1 second
timerUp = False
sizes = (0.5, 1, 2, 4)

#-----initialize turtle-----
t = turtle.Turtle()
t.shape(shape)
t.shapesize(size)
t.fillcolor(spotColor)
t.penup()
t.speed(0)
wn = turtle.Screen()
wn.bgcolor("bisque")

screenWriter = turtle.Turtle()
screenWriter.penup()
screenWriter.speed(0)
screenWriter.goto(-300, 225)
screenWriter.hideturtle()

counter = turtle.Turtle()
counter.penup()
counter.speed(0)
counter.goto(180, 225)
counter.hideturtle()


#-----game functions--------

def spotClicked(x, y):
  global timerUp
  if timerUp is False:
    updateScore()
    changePosition()
    changeSize()
  else:
    t.hideturtle()

def changeSize():
  t.shapesize(rand.choice(sizes))

def changePosition():
  xcor = rand.randint(-200, 200)
  ycor = rand.randint(-150, 150)
  t.hideturtle()
  t.goto(xcor, ycor)
  t.showturtle()

def updateScore():
  global score 
  score += 1
  screenWriter.clear()
  screenWriter.write(score, font = font)

def countdown():
  global timer, timerUp
  counter.clear()
  if timer <= 0:
    counter.write("Time's up!", font = font)
    timerUp = True
  else:
    counter.write("Timer: " + str(timer),  font = font)
    timer -= 1
    # append new timer to screen
    counter.getscreen().ontimer(countdown, counterInterval) 

#-----events----------------
t.onclick(spotClicked)
wn.ontimer(countdown, counterInterval)
wn.mainloop()