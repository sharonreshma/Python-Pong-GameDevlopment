import turtle
import winsound

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 5
PADDLE_LENGTH = 1
BALL_SPEED = 2
BALL_INITIAL_SPEED = 40
SCORE_FONT = ("Courier", 24, "normal")
MAX_Y = 250
MIN_Y = -240
MAX_X = 390
MIN_X = -390

# Set up the screen
win = turtle.Screen()
win.title("Pong Game by Sharon")
win.bgcolor("black")
win.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
win.tracer(0)

# Initial scores
score_a = 0
score_b = 0

def create_paddle(x, y):
    """Create a paddle at the specified position."""
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
    paddle.penup()
    paddle.goto(x, y)
    return paddle

player_a = create_paddle(-350, 0)
player_b = create_paddle(350, 0)

# Create ball
ball = turtle.Turtle()
ball.speed(BALL_INITIAL_SPEED)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = BALL_SPEED
ball.dy = -BALL_SPEED

# Display score
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=SCORE_FONT)

# Paddle movement functions
def paddle_a_up():
    """Move player A's paddle up."""
    y = player_a.ycor()
    if y < MAX_Y:
        player_a.sety(y + 20)

def paddle_a_down():
    """Move player A's paddle down."""
    y = player_a.ycor()
    if y > MIN_Y:
        player_a.sety(y - 20)

def paddle_b_up():
    """Move player B's paddle up."""
    y = player_b.ycor()
    if y < MAX_Y:
        player_b.sety(y + 20)

def paddle_b_down():
    """Move player B's paddle down."""
    y = player_b.ycor()
    if y > MIN_Y:
        player_b.sety(y - 20)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

def update_score():
    """Update the score display."""
    score_display.clear()
    score_display.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=SCORE_FONT)

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision handling
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > MAX_X:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        update_score()

    if ball.xcor() < MIN_X:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        update_score()

    # Paddle collision handling
    if (340 < ball.xcor() < 350) and (player_b.ycor() - 50 < ball.ycor() < player_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (-350 < ball.xcor() < -340) and (player_a.ycor() - 50 < ball.ycor() < player_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
