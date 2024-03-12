import turtle as trtl 
from PIL import Image, ImageOps
import os
from utils import draw_rect, quickmove, abs_resize, clear_folder

cookie_img = "assets/cookie.gif"
COOKIE_IMG_PATH = "cookie_cache"
ICON_IMG_PATH = "icon_cache"

cookies = 0

# init screen
trtl.tracer(0)
wn = trtl.Screen()
# wn.setup(0.5, 1.0, 630)
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

buildings = {
  "cursor": 0,
  "grandma": 0,
  "infiniplex": 0
}

building_turtles:list[trtl.Turtle] = []
for building in buildings:
  building_turtles.append(trtl.Turtle())

building_costs:list[int] = []
for building in buildings:
  match building:
    case "cursor":
      building_costs.append(10)
    case "grandma":
      building_costs.append(100)
    case "infiniplex":
      building_costs.append(10000)
    case _:
      print(f"[BUILDING_COSTS]: Building {building} is not defined.")

building_effects:list[float] = []
for building in buildings:
  match building:
    case "cursor":
      building_effects.append(0.1)
    case "grandma":
      building_effects.append(1)
    case "infiniplex":
      building_effects.append(100)
    case _:
      print(f"[BUILDING_EFFECTS]: Building {building} is not defined.")

clear_folder(COOKIE_IMG_PATH)
clear_folder(ICON_IMG_PATH)

prev_size:tuple[int, int] = (cookie_size, cookie_size)
is_animating = False

def abs_resize_cookie(resize:int):
  global prev_size
  abs_resize(cookie, cookie_img, resize, COOKIE_IMG_PATH)
  new_size_arr:list = [resize, resize]
  new_size = tuple(new_size_arr)
  prev_size = new_size

# randomize size/time
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

def update_cookies(new_score: int):
  global cookies
  cookies_writer.clear()
  cookies += new_score
  cookies_writer.write(cookies, font=("Verdana", 20, "normal"))
  wn.update()

def handle_cookie_click(x, y):
  global cookies
  update_cookies(1)
  bounce_cookie(cookie_size)

def get_building_cost(building: str):
  return building_costs[[building for building, _number in buildings.items()].index(building)]

def get_building_effect(building: str):
  return building_effects[[building for building, _number in buildings.items()].index(building)]

def draw_button(t:trtl.Turtle, x:int, y:int, building:str): 
  
  t.color("#87481e") 
  new_button = tuple(draw_rect(t, x, y, 400, 100))
  
  # image
  t.color("white")
  quickmove(t, int(t.xcor()) + 50, y)
  abs_resize(t, f"assets/{building}.gif", 90, ICON_IMG_PATH)
  t.stamp()

  # name
  quickmove(t, int(t.xcor()) + 70, y - 25)
  t.write(building.capitalize(), font=("Verdana", 30, "bold"))

  # cost
  quickmove(t, int(t.xcor()), int(t.ycor()) - 15)
  t.write(f"Cost: {get_building_cost(building)}", font=("Verdana", 10, "normal"))

  quickmove(t, x + 100, y - 30)
  t.write(buildings.get(building), font=("Verdana", 20, "normal"))

  def handle_button_click(xclick, yclick):
    if (new_button[0] < xclick < new_button[2]) and (new_button[3] < yclick < new_button[1]):
      if cookies >= get_building_cost(building):
        update_cookies(-get_building_cost(building))
        buildings[building] += 1
        draw_button(t, x, y, building)

  wn.onscreenclick(handle_button_click, add=True)

for i, building in enumerate(buildings):
  draw_button(building_turtles[i], 400, (i * -120) + 120, building)

abs_resize_cookie(cookie_size)
update_cookies(0)
cookie.onclick(handle_cookie_click)

wn.listen()
wn.mainloop()