import turtle as trtl 
import random as rand
from typing import TypedDict
from utils import draw_rect, quickmove, abs_resize, clear_folder

# --- init vars ---
cookie_img = "assets/cookie.gif"
COOKIE_CACHE_PATH = "cookie_cache"
ICON_CACHE_PATH = "icon_cache"

cookies = 0

trtl.tracer(0)
wn = trtl.Screen()
# wn.setup(0.5, 1.0, 630)
wn.setup(1.0, 1.0)
wn.addshape(cookie_img)

def draw_backgrounds():
  bg_writer = trtl.Turtle()
  bg_writer.hideturtle()
  bg_writer.color("sky blue")
  draw_rect(bg_writer, -300, 0, 500, 850)
draw_backgrounds()

cookie = trtl.Turtle()
cookie_size = 300
quickmove(cookie, -300, 0)
cookie.shape(cookie_img)

prev_size:tuple[int, int] = (cookie_size, cookie_size)
is_animating = False

cookies_writer = trtl.Turtle()
cookies_writer.hideturtle()
quickmove(cookies_writer, -300, 300)

cps_writer = trtl.Turtle()
cps_writer.hideturtle()
quickmove(cps_writer, -300, 270)

class Buildings(TypedDict):
  owned: int
  cost: int
  effect: float
  cache: float

buildings:dict[str, Buildings] = {
  "cursor": {
    "owned": 0,
    "cost": 10,
    "effect": 0.1,
    "cache": 0.0 
  },
  "grandma": {
    "owned": 0,
    "cost": 100,
    "effect": 1,
    "cache": 0.0 
  },
  "infiniplex": {
    "owned": 0,
    "cost": 1000,
    "effect": 10,
    "cache": 0.0 
  }
}

building_turtles:list[trtl.Turtle] = []
for building in buildings:
  building_turtles.append(trtl.Turtle())

clear_folder(COOKIE_CACHE_PATH)
clear_folder(ICON_CACHE_PATH)

# --- functions ---
def draw_mini_cookie():
  mini = trtl.Turtle()
  mini.hideturtle()
  mini.penup()
  abs_resize(mini, cookie_img, 50, COOKIE_CACHE_PATH)
  mini.goto(rand.randint(-700, -300), 850)
  mini.stamp()

def abs_resize_cookie(resize:int):
  global prev_size
  abs_resize(cookie, cookie_img, resize, COOKIE_CACHE_PATH)
  new_size_arr:list = [resize, resize]
  new_size = tuple(new_size_arr)
  prev_size = new_size

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

def update_cps():
  global buildings
  cps_writer.clear()
  curr_cps = 0.0
  for v in buildings.values():
    curr_cps += v["effect"] * float(v["owned"])
    curr_cps = round(curr_cps, 1)
  cps_writer.write(f"Cookies per second: {curr_cps}", font=("Verdana", 10, "normal"), align="center")

def handle_cookie_click(x: float, y: float):
  global cookies
  update_cookies(1)
  bounce_cookie(cookie_size)

def draw_button(t:trtl.Turtle, x:int, y:int, building:str): 
  t.color("#87481e") 
  new_button = tuple(draw_rect(t, x, y, 450, 100))
  
  # image
  t.color("white")
  quickmove(t, int(t.xcor()) + 50, y)
  abs_resize(t, f"assets/{building}.gif", 90, ICON_CACHE_PATH)
  t.stamp()

  # name
  quickmove(t, int(t.xcor()) + 70, y - 25)
  t.write(building.capitalize(), font=("Verdana", 30, "bold"))

  # cost
  quickmove(t, int(t.xcor()), int(t.ycor()) - 15)
  t.write(f"Cost: {buildings[building]['cost']}", font=("Verdana", 10, "normal"), align="center")

  # owned
  quickmove(t, int(new_button[2]) - 50, y-30)
  t.write(buildings[building]["owned"], font=("Verdana", 40, "normal"), align="right")

  def handle_button_click(xclick: float, yclick: float):
    if (new_button[0] < xclick < new_button[2]) and (new_button[3] < yclick < new_button[1]):
      if cookies >= buildings[building]["cost"]:
        update_cookies(-buildings[building]["cost"])
        buildings[building]["cost"] = int(buildings[building]["cost"] * 1.3)
        buildings[building]["owned"] += 1
        update_cps()
        draw_button(t, x, y, building)

  wn.onscreenclick(handle_button_click, add=True)

# might call more often 
def handle_buildings():
  for v in buildings.values():
    v["cache"] += (v["effect"] * v["owned"])
    v["cache"] = round(v["cache"], 1)
    add = 0
    while v["cache"] >= 1:
      v["cache"] -= 1
      add += 1
    update_cookies(add)
  wn.ontimer(handle_buildings, 1000)

# --- call funcs ---
abs_resize_cookie(cookie_size)

for i, building in enumerate(buildings):
  draw_button(building_turtles[i], 300, (i * -120) + 120, building)

handle_buildings()
update_cps()
update_cookies(0)
cookie.onclick(handle_cookie_click)

wn.listen()
wn.mainloop()