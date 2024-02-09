import turtle as trtl

spider = trtl.Turtle()

# draw spider body
spider.pensize(40)
spider.circle(20)
spider.speed(0)

# configure spider legs
legs = 8
leglength = 70
legangle = 360 / legs 
spider.pensize(5)
legcounter = 0

# draw legs
while (legcounter < legs):
  spider.goto(0,20)
  spider.setheading(legangle*legcounter)
  spider.forward(leglength)
  legcounter = legcounter + 1
spider.hideturtle()


wn = trtl.Screen()
wn.mainloop()