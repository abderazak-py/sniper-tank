import turtle
import os
import math
from tkinter import messagebox
import sys


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


bulletPath = resource_path("bullet.gif")
bullet2path = resource_path("bullet2.gif")
tankPath = resource_path("tank.gif")
tank2path = resource_path("tank2.gif")
gamePath = resource_path("game.png")


turtle.register_shape(bulletPath)
turtle.register_shape(bullet2path)
turtle.register_shape(tankPath)
turtle.register_shape(tank2path)

# create window
wind = turtle.Screen()
wind.title("sniper tank by vokernos")
wind.bgpic(gamePath)
wind.setup(width=800, height=600)
wind.tracer(0)

# Set the score to 0
score = 0
score2 = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.setposition(-340, 270)
scoreString = "Player 1: %s" % score
score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Draw score2
score2_pen = turtle.Turtle()
score2_pen.speed(0)
score2_pen.color("black")
score2_pen.penup()
score2_pen.setposition(260, 270)
score2string = "Player 2: %s" % score2
score2_pen.write(score2string, False, align="left", font=("Arial", 14, "normal"))
score2_pen.hideturtle()

# p player 1
o = turtle.Turtle()
o.speed(0)
o.shape(tankPath)
o.shapesize(3, 3, 3)
o.penup()
o.goto(0, -200)
o.tilt(90)

# i player 2
i = turtle.Turtle()
i.speed(0)
i.shape(tank2path)
i.shapesize(3, 3, 3)
i.penup()
i.goto(0, 200)
i.tilt(-90)

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("red")
bullet.shape(bulletPath)
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.1, 0.1)
bullet.hideturtle()

# SET BULLET SPEED HERE!
bulletSpeed = 4

# Define bullet state
# ready - ready to fire - bullet is firing
bulletState = "ready"

# Create the player's bullet
bullet2 = turtle.Turtle()
bullet2.color("red")
bullet2.shape(bullet2path)
bullet2.penup()
bullet2.speed(0)
bullet2.setheading(90)
bullet2.shapesize(0.1, 0.1)
bullet2.hideturtle()

# SET BULLET2 SPEED HERE!
bullet2speed = 4

# Define bullet state
# ready - ready to fire - bullet is firing
bullet2state = "ready"


def fire_bullet():
    # Declare bullet-state as a global if it needs to be changed
    global bulletState
    if bulletState == "ready":
        bulletState = "fire"
        x = o.xcor()
        y = o.ycor() - 10
        bullet.setposition(x, y)
        bullet.showturtle()


def fire_bullet2():
    # Declare bullet state as a global if it needs to be changed
    global bullet2state
    if bullet2state == "ready":
        bullet2state = "fire"
        x = i.xcor()
        y = i.ycor() + 10
        bullet2.setposition(x, y)
        bullet2.showturtle()


tankSpeed = 70


def o_right():
    x = o.xcor()
    x += tankSpeed
    if x > 350:
        x = 350
    o.setx(x)


def o_left():
    x = o.xcor()
    x -= tankSpeed
    if x < -350:
        x = -350
    o.setx(x)


def i_right():
    x = i.xcor()
    x += tankSpeed
    if x > 350:
        x = 350
    i.setx(x)


def i_left():
    x = i.xcor()
    x -= tankSpeed
    if x < -350:
        x = -350
    i.setx(x)


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


wind.onkeypress(o_left, "q")
wind.onkeypress(o_left, "a")
wind.onkeypress(o_right, "d")
wind.onkeypress(o_left, "Q")
wind.onkeypress(o_left, "A")
wind.onkeypress(o_right, "D")
wind.onkeypress(i_left, "Left")
wind.onkeypress(i_right, "Right")
wind.onkeypress(fire_bullet, "space")
wind.onkeypress(fire_bullet, "s")
wind.onkeypress(fire_bullet, "S")
wind.onkeypress(fire_bullet2, "0")
wind.onkeypress(fire_bullet2, "Down")
wind.listen()

while True:
    wind.update()
    # Move the bullet
    if bulletState == "fire":
        y = bullet.ycor()
        y += bulletSpeed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 500:
        bullet.hideturtle()
        bulletState = "ready"

    # Move the bullet
    if bullet2state == "fire":
        y = bullet2.ycor()
        y -= bullet2speed
        bullet2.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet2.ycor() < -500:
        bullet2.hideturtle()
        bullet2state = "ready"
    if is_collision(bullet, i):
        # Reset the bullet
        bullet.hideturtle()
        bulletState = "ready"
        bullet.setposition(0, -400)

        # Update the score
        score += 10
        scoreString = "Player 1: %s" % score
        score_pen.clear()
        score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
    if is_collision(bullet2, o):
        # Reset the bullet
        bullet2.hideturtle()
        bullet2state = "ready"
        bullet2.setposition(0, -400)

        # Update the score
        score2 += 10
        score2string = "Player 2: %s" % score2
        score2_pen.clear()
        score2_pen.write(score2string, False, align="left", font=("Arial", 14, "normal"))

    if score == 100:
        print("player 1 win")
        messagebox.showinfo(title='vokernos says', message='player 1 win')
        score = 0
        scoreString = "Player 1: %s" % score
        score_pen.clear()
        score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
        score2 = 0
        score2string = "Player 2: %s" % score2
        score2_pen.clear()
        score2_pen.write(score2string, False, align="left", font=("Arial", 14, "normal"))
    if score2 == 100:
        print("player 2 win")
        messagebox.showinfo(title='vokernos says', message='player 2 win')
        score = 0
        scoreString = "Player 1: %s" % score
        score_pen.clear()
        score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
        score2 = 0
        score2string = "Player 2: %s" % score2
        score2_pen.clear()
        score2_pen.write(score2string, False, align="left", font=("Arial", 14, "normal"))
