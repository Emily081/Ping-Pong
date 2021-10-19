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
ballXDirection = 0.9
ballYDirection = 0.9

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


def moveRightPaddleDown():
    y = rightPaddle.ycor()
    y = y - 90
    rightPaddle.sety(y)

def moveLeftPaddleUp():
    y = leftPaddle.ycor()
    y = y+90
    leftPaddle.sety(y)


def moveLeftPaddleUDown():
    y = leftPaddle.ycor()
    y = y - 90
    leftPaddle.sety(y)

window.listen()

window.onkey(moveLeftPaddleUp, 'w')
window.onkey(moveLeftPaddleUDown, 's')
window.onkey(moveRightPaddleUp, 'Up')
window.onkey(moveRightPaddleDown, 'Down')

# forever loop to move the ball

while True:
    window.update()
    ball.setx(ball.xcor() + ballXDirection)
    ball.sety(ball.ycor() + ballYDirection)

    if ball.ycor() > 290:
        ball.sety(290)
        ballYDirection = ballYDirection*-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ballXDirection*-1
        playerAScore += 1
        pen.clear()
        pen.write("Player A : {}          Player B : {}".format(playerAScore, playerBScore), align="center")
    if ball.ycor() < -290:
        ball.sety(-290)
        ballYDirection = ballYDirection * -1
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballXDirection * -1
        playerBScore += 1
        pen.clear()
        pen.write("Player A : {}          Player B : {}".format(playerAScore, playerBScore), align="center")

    if (ball.xcor() > 340) and (ball.xcor() < 350) and (
            ball.ycor() < rightPaddle.ycor() + 40 and ball.ycor() > rightPaddle.ycor() - 40):
        ball.setx(340)
        ballXDirection *= -1

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (
            ball.ycor() < leftPaddle.ycor() + 40 and ball.ycor() > leftPaddle.ycor() - 40):
        ball.setx(-340)
        ballXDirection *= -1

window.update()
ball.setx(ball.xcor() + ballXDirection)
ball.sety(ball.ycor() + ballYDirection)



lola.exitonclick()

