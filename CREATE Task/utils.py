from turtle import Turtle
from PIL import Image, ImageOps
import os

def quickmove(t:Turtle, x:int, y:int):
  '''Moves the turtle to a given location without pen.
 
  Shorthand for `t.penup()` `t.goto(x, y)` `t.pendown()`.'''
  t.penup()
  t.goto(x, y)
  t.pendown()

def draw_rect(t:Turtle, x:int, y:int, width:int, height: int | None = None):
  '''Draws a rectangle. Height defaults to width.
  :returns - An array containing its boundaries (`[left, up, right, down]`).'''
  if height == None:
    height = width
  
  t.hideturtle()
  t.penup()
  t.seth(0)
  t.goto(x, y)
  t.backward(width/2)
  t.left(90)
  t.backward(height/2)
  t.pendown()

  t.begin_fill()

  walls:list[float] = []

  for i in range(2):
    walls.append(t.xcor())
    t.forward(height)
    t.right(90)

    walls.append(t.ycor())
    t.forward(width)
    t.right(90)
  
  t.end_fill()

  return walls

def isolate_img_name(img_path: str):
      name = ""
      true_path = img_path
      if "/" in img_path:
        true_path_arr:list[str] = img_path.split("/")
        true_path = true_path_arr[len(true_path_arr) - 1]
      for char in true_path:
        if char == ".":
          return name
        else:
          name += char

def abs_resize(t:Turtle, img_path:str, new_size:int, NEW_IMG_FOLDER:str = "assets"):
  '''Given an image path, resizes it and sets the given turtle to that image.
  :returns - The new image path.'''
  with Image.open(img_path) as im:
    new_size_tuple = (new_size, new_size)

    new_img = f"{NEW_IMG_FOLDER}/{isolate_img_name(img_path)}{new_size}.gif"
    ImageOps.contain(im, new_size_tuple).save(new_img)

  t.screen.addshape(new_img)
  t.shape(new_img)
  t.screen.update()
  return new_img

def rotate(t:Turtle, img_path: str, angle:int, NEW_IMG_FOLDER:str = "assets"):
  '''Given an image path, rotates it and sets the given turtle to that image.
  :returns - The new image path.'''
  with Image.open(img_path) as im:
    while angle >= 360:
      angle //= 360 
    print(angle)

    new_img = f"{NEW_IMG_FOLDER}/{isolate_img_name(img_path)}:{angle}deg.gif"
    if new_img not in os.listdir(NEW_IMG_FOLDER):
      im.rotate(angle, expand=True).convert("RGBA").save(new_img)
  
  t.screen.addshape(new_img)
  t.shape(new_img)
  t.screen.update()  
  return new_img  

def clear_folder(path:str):
  '''Clears all files within a folder.
  A simplified version of 
  https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder.'''
  for file in os.listdir(path):
    file_path = os.path.join(path, file)
    os.unlink(file_path)