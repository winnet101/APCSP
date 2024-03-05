import turtle as trtl 
from PIL import Image, ImageOps
from threading import Timer
from functools import partial

cookie_img = "cookie.gif"

# init screen
wn = trtl.Screen()
wn.addshape(cookie_img)

cookie = trtl.Turtle()
cookie.shape(cookie_img)

prev_size:tuple[int, int] = (150, 150)

def resize_cookie(resize:int):
  with Image.open(cookie_img) as im:
    global prev_size
    new_size_arr = []

    for coord in prev_size:
      coord += resize
      new_size_arr.append(coord)

    new_size = tuple(new_size_arr)
    prev_size = new_size

    new_img = f"assets/cookie{new_size[0]}.gif"

    ImageOps.contain(im, new_size).save(new_img)

  wn.addshape(new_img)
  cookie.shape(new_img)
  print(f"resized to {new_size}")

def abs_resize_cookie(resize:int):
  with Image.open(cookie_img) as im:
    new_size_arr:list = [resize, resize]
    new_size = tuple(new_size_arr)

    new_img = f"assets/cookie{new_size[0]}.gif"

    ImageOps.contain(im, new_size).save(new_img)

  wn.addshape(new_img)
  cookie.shape(new_img)

def set_timeout(time:float, func, args):
  new_func = partial(func, args)
  t = Timer(time, new_func)
  t.start()

def bounce_cookie(x, y):
  abs_resize_cookie(150)
  for i in range(5):
    resize_cookie(i * 15)

  for i in range(5):
    resize_cookie(-i * 15)


cookie.onclick(bounce_cookie)

wn.listen()
wn.mainloop()