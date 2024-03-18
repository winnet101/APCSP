from turtle import Turtle
from utils import abs_resize, quickmove, rotate

def draw_cursor(cookiex: int, cookiey: int):
  cursor = Turtle()
  cursor.seth(90)
  resized_cursor_img = abs_resize(cursor, "assets/cursor.gif", 40, "icon_cache")
  quickmove(cursor, cookiex, cookiey)
  cursor.stamp()
  cursor.penup()

  def turn_cursor():
    cursor.right(1)
    cursor.forward(3)
    cursor.clear()
    cursor.stamp()
    rotate(cursor, resized_cursor_img, int(cursor.heading() - 180), "icon_cache")
    cursor.screen.ontimer(turn_cursor, 10)

  cursor.screen.ontimer(turn_cursor, 0)