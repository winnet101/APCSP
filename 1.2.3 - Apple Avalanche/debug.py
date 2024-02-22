#   a123_apple_1.py
from functools import partial
from copy import deepcopy
import random as rand
import turtle as trtl

#-----setup-----
apple_image = "apple.gif"

# init screen
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) 
wn.bgpic("background.gif")

letters = ["q", "w", "e", "r", "t", "y", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
letters_immutable = deepcopy(letters) # for keybind purposes

number_of_apples = 5

letter_list: list[str] = []
apple_list: list[trtl.Turtle] = []

for i in range(number_of_apples):
  new_apple = trtl.Turtle()
  new_apple.penup()
  apple_list.append(new_apple)

  new_letter = letters.pop(rand.randint(0, len(letters) - 1))
  letter_list.append(new_letter)

#-----functions-----
def draw_apple(index: int):
  ''' Inits and draws an apple and its associated letter.'''
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
  ''' Writes a given letter using a given apple.'''
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
  '''Redraws the apple at a random position.'''
  active_apple = apple_list[index]

  trtl.tracer(False)
  active_apple.goto(rand.randint(-180, 180), 0)
  draw_apple(index)

def drop_apple(index: int):
  '''Drops an apple and hides it. 
  If there are still letters to be pressed, resets it. Otherwise, hides it.'''
  active_apple = apple_list[index]

  trtl.tracer(True)
  active_apple.clear()
  active_apple.sety(-200)
  active_apple.hideturtle()
  trtl.tracer(False)
  if letters:
    letter_list[index] = letters.pop(rand.randint(0, len(letters) - 1))
    reset_apple(index)
  else:
    global number_of_apples
    number_of_apples = number_of_apples - 1

def typed(letter:str):
  '''Given a letter, drops the associated apple (if there is one).'''
  for i in range(len(letter_list)):
    if letter_list[i] == letter:
      print(i, letter_list, letter_list[i])
      drop_apple(i)

#-----function calls-----
for i in range(number_of_apples):
  draw_apple(i)

# Since functions passed to wn.onkeypress can't take in parameters, they have to be added beforehand. 
# This code loops through each letter and creates a version of the typed function corresponding to that specific letter (that letter is made the default input, using partial), then assigns it to that keybind.
for l in letters_immutable:
  partial_func = partial(typed, l)
  wn.onkeypress(partial_func, l)

wn.listen()
wn.mainloop()