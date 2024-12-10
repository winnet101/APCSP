import turtle as trtl
import random as rand

# --- variables ---
number_of_walls = 6
path_width = 10
wall_color = "black"

# --- init ---
trtl.tracer(False)

maze = trtl.Turtle()
wn = maze.screen
maze.pencolor(wall_color)
maze.pensize(3)
maze.setheading(180)
maze.hideturtle()

wall_length = 15
for i in range(number_of_walls):
  for j in range(4):
    door_length = path_width * 2
    true_length = wall_length

    # randomize locations
    def get_locations():
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
          draw_barrier(barrier)
        else:
          draw_barrier(barrier)
          draw_door(door)

    maze.forward(true_length)

    wall_length += path_width
    maze.left(90)
        
    def draw_door(dist: int | float):
      maze.forward(dist)
      maze.penup()
      maze.forward(door_length)
      maze.pendown()
     

    def draw_barrier(dist: int | float):
      maze.forward(dist)
      maze.left(90)
      maze.forward(door_length)
      maze.backward(door_length)
      maze.right(90)
    
wn.update() 
wn.mainloop()
