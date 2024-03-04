import turtle as trtl 
from PIL import Image, ImageOps

cookie_img = "cookie.gif"

# init screen
wn = trtl.Screen()
wn.addshape(cookie_img)

cookie = trtl.Turtle()
cookie.shape(cookie_img)

def resize_cookie(resize:int):
  with Image.open("cookie.gif") as im:
    size = im.size
    new_size_arr = []

    for coord in size:
      coord += resize
      new_size_arr.append(coord)

    new_size = tuple(new_size_arr)
    ImageOps.contain(im, new_size).save("new.gif")

  new_img = "new.gif"
  wn.addshape(new_img)
  cookie.shape(new_img)

print("resizing?")
resize_cookie(-40)

wn.mainloop()