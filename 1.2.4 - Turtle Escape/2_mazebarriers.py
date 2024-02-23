import turtle as trtl

# --- variables ---
number_of_walls = 6
path_width = 10
wall_color = "black"

# --- init ---
maze = trtl.Turtle()
trtl.tracer(False)
maze.pencolor(wall_color)
maze.pensize(3)
maze.setheading(180)
maze.hideturtle()

wn = maze.screen

wall_length = 10
for i in range(number_of_walls):
  for j in range(4):
    true_length = wall_length

    # draw door
    if i >= 1:
      door_length = path_width * 2
      maze.forward(10)
      maze.penup()
      maze.forward(door_length)
      maze.pendown()
      true_length -= (10 + door_length)

    # draw barrier
    if i >= 2:
      maze.forward(40)
      maze.left(90)
      maze.forward(path_width * 2)
      maze.backward(path_width * 2)
      maze.right(90)
      true_length -= 40

    maze.forward(true_length)

    wall_length += path_width
    maze.left(90)
    
wn.update() 
wn.mainloop()