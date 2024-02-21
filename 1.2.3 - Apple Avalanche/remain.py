#   a123_apple_1.py
import random as rand
import turtle as trtl

#-----setup-----
apple_image = "apple.gif"

# screen init
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) 
wn.bgpic("background.gif")

letters = ["q", "w", "e", "r", "t", "y", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
apple_number = 5

letter_list:list[str] = []
for i in range(apple_number):
  new_letter = letters.pop(rand.randint(0, len(letters) - 1))
  letter_list.append(new_letter)

turtle_list:list[trtl.Turtle] = []
for i in range(apple_number):
  new_turtle = trtl.Turtle()
  turtle_list.append(new_turtle)

#-----functions-----
def draw_apple(active: trtl.Turtle):
  trtl.tracer(False)
  active.penup()
  active.shape(apple_image)
  active.goto(rand.randint(-180, 180), rand.randint(-20, 30))
  wn.update()

def reset_apple(active):
  trtl.tracer(False)
  active.goto(rand.randint(-180, 180), 0)

def apple_fall():
  trtl.tracer(True)
  apple.clear()
  apple.sety(-200)
  apple.hideturtle()
  reset_apple(apple)

def write_letter(active:trtl.Turtle, letter: str):
  ''' 
  Writes a given letter using a given turtle.

  Arguments: 
  active -- a turtle | letter -- a string
  '''
  trtl.tracer(False)
  x = active.xcor()
  y = active.ycor()
  active.goto(x - 18, y + 40)
  active.write(letter.upper(), font
  =("Arial", 55, "normal"))
  active.goto(x, y)
  active.showturtle()
  wn.update()

#-----function calls-----
for i in range(apple_number):
  curr_turtle = turtle_list[i]
  curr_letter = letter_list[i]
  draw_apple(curr_turtle)
  write_letter(curr_turtle, curr_letter.capitalize())
  # wn.onkeypress(apple_fall, curr_letter)
  print(i)

wn.listen()
wn.mainloop()