import turtle as trtl 
from PIL import Image, ImageOps
import os
from utils import draw_rect, quickmove

cookie_img = "cookie.gif"

cookies = 0

# init screen
trtl.tracer(0)
wn = trtl.Screen()
wn.setup(1.0, 1.0)
wn.addshape(cookie_img)

cookie = trtl.Turtle()
cookie_size = 300
quickmove(cookie, -300, 0)
cookie.shape(cookie_img)
wn.update()

cookies_writer = trtl.Turtle()
cookies_writer.hideturtle()
quickmove(cookies_writer, -300, 300)

buttons = ["cursor"]
button_turtles:list[trtl.Turtle] = []

for button in buttons:
  button_turtles.append(trtl.Turtle())

for file in os.listdir("assets"):
  file_path = os.path.join("assets/", file)
  os.unlink(file_path)

prev_size:tuple[int, int] = (cookie_size, cookie_size)
is_animating = False

def abs_resize_cookie(resize:int):
  with Image.open(cookie_img) as im:
    global prev_size
    new_size_arr:list = [resize, resize]
    new_size = tuple(new_size_arr)
    prev_size = new_size

    new_img = f"assets/cookie{new_size[0]}.gif"

    ImageOps.contain(im, new_size).save(new_img)

  wn.addshape(new_img)
  cookie.shape(new_img)
  wn.update()

def bounce_cookie(init_size: int):
  global is_animating
  if is_animating:
    return
  else:
    is_animating = True
    abs_resize_cookie(init_size)
    for i in range(5):
      abs_resize_cookie(init_size + (i * 10))
      wn.update()

    for i in range(5):
      abs_resize_cookie((init_size + (5 * 10)) + (-i * 10))
      wn.update()
    abs_resize_cookie(init_size)
    wn.update()
  is_animating = False

def update_score(new: int):
  global cookies
  cookies_writer.clear()
  cookies += new
  cookies_writer.write(cookies, font=("Times New Roman", 20, "normal"))
  wn.update()

def handle_cookie_click(x, y):
  global cookies
  update_score(1)
  bounce_cookie(cookie_size)

def draw_button(t:trtl.Turtle, x:int, y:int): 
  t.color("brown") 
  new_button = draw_rect(t, x, y, 200, 100)
  print(new_button)
  
  def handle_button_click(x, y):
    if (new_button[0] < x < new_button[2]) and (new_button[1] < y < new_button[3]):
      print("clicked!")

  wn.onscreenclick(handle_button_click)

for i, button in enumerate(buttons):
  draw_button(button_turtles[i], 0, 0)

abs_resize_cookie(cookie_size)
cookie.onclick(handle_cookie_click)

wn.listen()
wn.mainloop()