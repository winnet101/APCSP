import turtle as trtl

# --- variables ---
number_of_walls = 6
path_width = 10
wall_color = "black"

# --- init ---
maze = trtl.Turtle()
trtl.tracer(False)
maze.pencolor(wall_color)
maze.pensize(2)
maze.setheading(90)
maze.hideturtle()

wn = maze.screen

wall_length = 10
for i in range(number_of_walls):
  for i in range(4):
    maze.forward(10)

    # draw door
    maze.penup()
    maze.forward(path_width * 2)
    maze.pendown()

    maze.forward(wall_length)
    wall_length = wall_length + path_width
    maze.left(90)
    
wn.update() 
wn.mainloop()