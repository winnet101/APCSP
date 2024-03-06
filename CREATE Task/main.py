import turtle as trtl 
from PIL import Image, ImageOps
import os

cookie_img = "cookie.gif"

cookies = 0

# init screen
trtl.tracer(0)
wn = trtl.Screen()
wn.setup(1.0, 1.0)
wn.addshape(cookie_img)

cookie = trtl.Turtle()
cookie_size = 300
cookie.shape(cookie_img)
wn.update()

cookies_writer = trtl.Turtle()
cookies_writer.penup()
cookies_writer.goto(-300, 300)
cookies_writer.hideturtle()
cookies_writer.pendown()

for file in os.listdir("assets"):
  file_path = os.path.join("assets/", file)
  os.unlink(file_path)

prev_size:tuple[int, int] = (cookie_size, cookie_size)
is_animating = 0

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
    is_animating += 1
    abs_resize_cookie(init_size)
    for i in range(5):
      abs_resize_cookie(init_size + (i * 10))
      wn.update()

    for i in range(5):
      abs_resize_cookie((init_size + (5 * 10)) + (-i * 10))
      wn.update()
    abs_resize_cookie(init_size)
    wn.update()
  is_animating = 0

def handle_cookie_click(x, y):
  global cookies
  update_score(1)
  bounce_cookie(cookie_size)

def update_score(new: int):
  global cookies
  cookies_writer.clear()
  cookies += new
  cookies_writer.write(cookies, font=("Times New Roman", 20, "normal"))
  wn.update()

abs_resize_cookie(cookie_size)
cookie.onclick(handle_cookie_click)

wn.listen()
wn.mainloop()