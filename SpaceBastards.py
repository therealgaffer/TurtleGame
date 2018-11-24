import turtle

# Create a window
main_window = turtle.Screen()
main_window.bgcolor("Black")
main_window.title("Space Bastards")

# Create border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.penup()
border_pen.goto(-300, -300)
border_pen.color("white")
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the player
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.speed(0)
player.goto(0, -250)
player.lt(90)

# Create a baddie
enemy = turtle.Turtle()
enemy.penup()
enemy.shape("circle")
enemy.color("red")
enemy.speed(0)
enemy.goto(0, 200)

# Move player left and right
playerspeed = 15

def player_move_left():
    x = player.xcor()
    x -= playerspeed
    player.setx(x)

def player_move_right():
    y = player.ycor()
    y += playerspeed
    player.sety(y)

# Keybinds
turtle.listen()
turtle.onkey(player_move_left, "Left")








input("Press enter to finish")
