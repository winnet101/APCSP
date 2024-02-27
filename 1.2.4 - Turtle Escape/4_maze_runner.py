import turtle as trtl
import random as rand
from functools import partial

# --- variables ---
number_of_walls = 6
path_width = 10
wall_color = "black"
wall_length = 15
true_length = wall_length

# --- init ---
trtl.tracer(False)

maze = trtl.Turtle()
wn = maze.screen
maze.pencolor(wall_color)
maze.pensize(3)
maze.setheading(180)
maze.hideturtle()

runner = trtl.Turtle()
runner.showturtle()
runner.goto(0, 0)
runner_speed = 10
runner_keys = ["Up", "Down", "Left", "Right"]

def key_move(key:str):
  match key:
    case "Up":
      runner.seth(90)
    case "Down":
      runner.seth(270)
    case "Left":
      runner.seth(180)
    case "Right":
      runner.seth(0)
  wn.update()

def draw_maze():
  for i in range(number_of_walls):
    for j in range(4):
      door_length = path_width * 2
      global true_length
      global wall_length
      true_length = wall_length

      # randomize locations
      def get_locations():
        if i < 2:
          if (wall_length - (door_length )) > door_length:
            door = rand.randint(door_length , wall_length - (door_length))
            barrier = rand.randint(door_length , wall_length - (door_length))
            return (door, barrier)
        else:
          if (wall_length - (door_length * 2)) > door_length * 2:
            door = rand.randint(door_length * 2, wall_length - (door_length * 2))
            barrier = rand.randint(door_length * 2, wall_length - (door_length * 2))
            return (door, barrier)
          else:
            return False
          
      lengths = get_locations()
      if lengths:
        door = lengths[0]
        barrier = lengths[1]
        if i < 2:
          draw_door(door)
        else:
          if door < barrier:
            draw_door(door)
            barrier -= door
            draw_barrier(barrier)
          else:
            draw_barrier(barrier)
            door -= barrier
            draw_door(door)

      maze.forward(true_length)

      wall_length += path_width
      maze.left(90)
          
      def draw_door(dist: int):
        maze.forward(dist)
        maze.penup()
        maze.forward(door_length)
        maze.pendown()
        global true_length 
        true_length -= (dist + door_length)

      def draw_barrier(dist: int):
        maze.forward(dist)
        maze.left(90)
        maze.forward(door_length)
        maze.backward(door_length)
        maze.right(90)
        global true_length 
        true_length -= (dist)
  wn.update()

draw_maze()
for key in runner_keys:
  key_press = partial(key_move, key)
  wn.onkeypress(key_press, key)

wn.listen()
wn.mainloop()