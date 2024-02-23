import turtle as trtl
import random as rand

# --- variables ---
number_of_walls = 6
path_width = 10
wall_color = "black"

# --- init ---
maze = trtl.Turtle()
maze.pencolor(wall_color)
maze.pensize(3)
maze.setheading(180)
maze.hideturtle()

wn = maze.screen

wall_length = 10
for i in range(number_of_walls):
  for j in range(4):
    door_length = path_width * 2
    true_length = wall_length

    # randomize locations
    def get_locations():
      if (wall_length - door_length) > door_length:
        door = rand.randint(door_length, wall_length - door_length)
        barrier = rand.randint(door_length, wall_length - door_length)
        return (door, barrier)
      else:
        return False
      
    lengths = get_locations()
    if lengths:
      door = lengths[0]
      barrier = lengths[1]

    # draw door
    if lengths:
      maze.forward(door)
      maze.penup()
      maze.forward(door_length)
      maze.pendown()
      true_length -= (door + door_length)

    # draw barrier
    if lengths:
      maze.forward(barrier)
      maze.left(90)
      maze.forward(door_length)
      maze.backward(door_length)
      maze.right(90)
      true_length -= barrier

    maze.forward(true_length)

    wall_length += path_width
    maze.left(90)
    
wn.update() 
wn.mainloop()