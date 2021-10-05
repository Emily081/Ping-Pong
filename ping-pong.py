import turtle as lola
import turtle

# for the score
playerAScore = 0
playerBScore = 0

# creating the screen
window = lola.Screen()
window.title('PingPong')

window.bgcolor('black')
window.setup(width=800, height=600)

# this is the right paddle
rightPaddle = lola.Turtle()
rightPaddle.speed(0)
rightPaddle.shape('square')
rightPaddle.color('lime')
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350, 0)
# this is the left paddle

leftPaddle = lola.Turtle()
leftPaddle.speed(0)
leftPaddle.shape('square')
leftPaddle.color('red')
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

# this is the ball

ball = lola.Turtle()
ball.shape('circle')
ball.speed(0)
ball.color('white')
ball.penup()
ball.goto(5,5)

# this will change the ball position on the screen
ballXDirection = 0.4
ballYDirection = 0.4

# this is the pen to write the score
pen = lola.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color('blue')
pen.penup()
pen.goto(0, 260)
pen.write("Score", align="center", font=('merriweather', 24, 'normal'))

# Fuctions to move the paddkes up and down
def moveRightPaddleUp():
    y = rightPaddle.ycor()
    y = y+90
    rightPaddle.sety(y)


def moveRightPaddleUDown():
    y = rightPaddle.ycor()
    y = y - 90
    rightPaddle.sety(y)

def moveLeftPaddleUp():
    y = rightPaddle.ycor()
    y = y+90
    rightPaddle.sety(y)


def moveLeftPaddleUDown():
    y = rightPaddle.ycor()
    y = y - 90
    rightPaddle.sety(y)

lola.exitonclick()

