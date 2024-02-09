import turtle as trtl

spider = trtl.Turtle()

# draw spider body
spider.pensize(40)
spider.circle(20)
# spider.speed(0)

# configure legs
number = 8
length = 70
angle = 180 / number 
spider.pensize(5)
leg = 0

halfnumber = (number)/2

# draw legs
while leg < number:
  spider.goto(0,20)
  if leg < halfnumber: 
      heading = (angle * leg) - 45
      spider.setheading(heading)
  else:
     heading = (angle * leg) + 45
     spider.setheading(heading)
  print(heading)
  spider.forward(length)
  leg = leg + 1

# draw eyes
def moveUp(x, y):
  spider.penup()
  spider.goto(x, y)
  spider.pendown()

offset = 20
size = 1

for i in range(2):
  spider.color("white")
  if i == 1:
    moveUp(offset, 20)
  else: 
     moveUp(-offset, 20)
  spider.begin_fill()
  spider.circle(size)
  spider.end_fill()
  if size > 2:
    spider.color("black")
    spider.begin_fill()
    spider.circle(size-2)
    spider.end_fill()


spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()