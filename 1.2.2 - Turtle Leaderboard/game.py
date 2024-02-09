import turtle as t
import random as r
import leaderboard as lb

# game config
colors = ["black", "sky blue", "salmon", "orchid", "pale green"]
font = ("Arial", 20, "normal")
spotSize = 2
spotColor = 'pink'
spotShape = 'turtle'
timer = 5
counterInterval = 1000 # 1 second
timerUp = False
score = 0

leaderboardFileName = "leaderboard.txt"
playerName = input("What's your name?")

# initialization
spot = t.Turtle()
spot.shape(spotShape)
spot.shapesize(spotSize)
spot.fillcolor(spotColor)

scoreWriter = t.Turtle();
scoreWriter.hideturtle()
scoreWriter.penup()
scoreWriter.goto(160, 160)
scoreWriter.pendown()

counter = t.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-160, 160)
counter.pendown()

def manageLeaderboard():
  global score
  global spot
  leaderNamesList = lb.get_names(leaderboardFileName)
  leaderScoresList = lb.get_scores(leaderboardFileName)

  # show the leaderboard with or without the current player
  if (len(leaderScoresList) < 5 or score >= leaderScoresList[4]):
    lb.update_leaderboard(leaderboardFileName, leaderNamesList, leaderScoresList, playerName, score)
    lb.draw_leaderboard(True, leaderNamesList, leaderScoresList, spot, score)
  else:
    lb.draw_leaderboard(False, leaderNamesList, leaderScoresList, spot, score)


def countdown():
  global timer
  global timerUp
  counter.clear()
  if timer <= 0:
    counter.write(
      "Time's Up!", 
      font=font)
    timerUp = True;
    manageLeaderboard()
  else:
    counter.write(
      "Timer: " + str(timer), 
      font=font)
    timer -= 1
    counter.getscreen().ontimer(countdown, counterInterval)

def updateScore():
  global score
  score += 1
  scoreWriter.clear()
  scoreWriter.write(
    score,
    font=font
  )

def handleClick(x, y):
  if not timerUp:
    updateScore()
    changePosition()
  else:
    spot.hideturtle()
  
def resize():
  sizes = [0.5, 1, 1.5, 2]
  spot.shapesize(r.choice(sizes))

def stamp():
  spot.fillcolor(r.choice(colors))
  spot.stamp()

def changePosition():
  stamp()
  resize()
  spot.penup()
  spot.hideturtle()
  spot.goto(
    r.randint(-150, 150),
    r.randint(-150, 150)
  )
  spot.pendown()
  spot.showturtle()

def startGame():
  spot.onclick(handleClick)
  counter.getscreen().ontimer(
    countdown, 
    counterInterval
  )

# events
startGame()
wn = t.Screen()
wn.bgcolor("white smoke")
wn.mainloop()