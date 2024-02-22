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

letter_list: list[str] = []
apple_list: list[trtl.Turtle] = []

for i in range(apple_number):
  new_apple = trtl.Turtle()
  new_apple.penup()
  apple_list.append(new_apple)

  new_letter = letters.pop(rand.randint(0, len(letters) - 1))
  letter_list.append(new_letter)

#-----functions-----
def draw_apple(index: int):
  ''' Inits a turtle as an apple and writes its associated letter.'''
  curr_apple = apple_list[index]
  curr_letter = letter_list[index]
  trtl.tracer(False)

  curr_apple.penup()
  curr_apple.shape(apple_image)
  curr_apple.goto(rand.randint(-180, 180), rand.randint(-20, 30))
  write_letter(curr_apple, curr_letter)
  curr_apple.showturtle()
  wn.update()

def write_letter(active_apple: trtl.Turtle, letter: str):
  ''' Writes a given letter using a given turtle.'''
  trtl.tracer(False)
  x = active_apple.xcor()
  y = active_apple.ycor()
  active_apple.goto(x - 18, y + 40)
  active_apple.write(letter.upper(), font
  =("Arial", 55, "normal"))
  active_apple.goto(x, y)
  active_apple.showturtle()
  wn.update()

def reset_apple(index: int):
  curr_apple = apple_list[index]

  trtl.tracer(False)
  curr_apple.goto(rand.randint(-180, 180), 0)
  draw_apple(index)

def drop_apple(index: int):
  curr_apple = apple_list[index]

  trtl.tracer(True)
  curr_apple.clear()
  curr_apple.sety(-200)
  curr_apple.hideturtle()
  if letters:
    letter_list[index] = letters.pop(rand.randint(0, len(letters) - 1))
    reset_apple(index)
  else:
    global apple_number
    apple_number = apple_number - 1

def a_typed():
  for i in range(apple_number):
    if letter_list[i] == "a":
      drop_apple(i)

#-----function calls-----
for i in range(apple_number):
  draw_apple(i)

# some weird hack to create functions goes here
wn.onkeypress(a_typed, "a")

wn.listen()
wn.mainloop()