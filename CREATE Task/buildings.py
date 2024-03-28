import turtle as trtl
from utils import abs_resize, rotate

def rotate_cursor(t: trtl.Turtle, start_dir: float, radius: int, increment: int, center: tuple[int, int]):
  '''Turns a turtle object into a rotating cursor.
  :params: increment - number of frames per rotation.'''
  resized_path = abs_resize(t, "assets/cursor.gif", 20, "icon_cache")
  rotate(t, resized_path, start_dir + 60, "icon_cache")
  t.setheading(start_dir)

  def turn_turtle():
    new_heading = int(t.heading()) + (365 // increment)
    t.seth(new_heading)
    rotate(t, resized_path, new_heading + 60, "icon_cache")
    t.penup()
    t.goto(center)
    t.forward(radius)
    # t.screen.update()
    t.screen.ontimer(turn_turtle, 10)
    
  t.screen.ontimer(turn_turtle, 10)
  