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

letter_list:list[str] = []
turtle_list:list[trtl.Turtle] = []

#-----functions-----
def draw_apple(active: trtl.Turtle):
  active.shape(apple_image)
  write_letter(active, curr_letter.capitalize())
  wn.update()

def reset_apple(active_apple):
  trtl.tracer(False)
  active_apple.goto(rand.randint(-180, 180), 0)

def apple_fall():
  trtl.tracer(True)
  apple.clear()
  apple.sety(-200)
  apple.hideturtle()
  reset_apple(apple)

def write_letter(active_apple:trtl.Turtle, letter: str):
  ''' 
  Writes a given letter using a given turtle.

  Arguments: 
  active_apple -- a turtle | letter -- a string
  '''
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
curr_letter = letters.pop(rand.randint(0, len(letters) - 1))

draw_apple(apple)
wn.onkeypress(apple_fall, curr_letter)

wn.listen()
wn.mainloop()