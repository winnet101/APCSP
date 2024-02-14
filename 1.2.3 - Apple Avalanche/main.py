#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple.penup()
apple.color("white")
trtl.tracer(False)

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def apple_fall():
  apple.sety(-200)

def write_letter():
  x = apple.xcor()
  y = apple.ycor()
  apple.goto(x - 18, y + 40)
  apple.write("A", font
  =("Arial", 55, "normal"))
  apple.goto(x, y)
  wn.update()

#-----function calls-----
draw_apple(apple)
write_letter()
wn.onkeypress(apple_fall, "a")

wn.listen()
wn.mainloop()