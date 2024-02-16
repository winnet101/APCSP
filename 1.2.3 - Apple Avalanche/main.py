#   a123_apple_1.py
import random as rand
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

letters = ["q", "w", "e", "r", "t", "y", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def reset_apple(active_apple):
  trtl.tracer(False)
  active_apple.goto(rand.randint(-180, 180), 0)

def apple_fall(active_apple):
  trtl.tracer(True)
  active_apple.clear()
  active_apple.sety(-200)
  active_apple.hideturtle()
  reset_apple(active_apple)

def write_letter(active_apple:trtl.Turtle, letter: str):
  ''' Doc comments '''
  trtl.tracer(False)
  x = active_apple.xcor()
  y = active_apple.ycor()
  active_apple.goto(x - 18, y + 40)
  active_apple.write(letter.upper(), font
  =("Arial", 55, "normal"))
  active_apple.goto(x, y)
  active_apple.showturtle()
  wn.update()

#-----function calls-----
draw_apple(apple)

curr_letter = letters[rand.randint(0, len(letters) - 1)]

write_letter(apple, curr_letter.capitalize())
wn.onkeypress(apple_fall, curr_letter)

wn.listen()
wn.mainloop()