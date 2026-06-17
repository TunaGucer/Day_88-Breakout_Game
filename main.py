import time
from turtle import Screen

from Breakout_turtles import Breakout
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
screen=Screen()
screen.bgcolor("black")
screen.setup(width=600,height=800)
screen.title("Breakout Game")
screen.tracer(0)

the_paddle=Paddle((0,-350))
breakout_width = 20
breakout_height = 20
gap = 5
turtle_count=0
hit_count=0

breakout_turtles=[]
for y in range(300, 200, -(breakout_height + gap)):
    if y == 300:
        color = "red"
    elif y == 275:
        color = "orange"
    elif y == 250:
        color = "yellow"
    else:
        color = "green"
    for x in range(-250, 251, breakout_width + gap):
        breakout_turtle = Breakout((x, y),color)
        breakout_turtles.append(breakout_turtle)
        turtle_count+=1

ball=Ball()
scoreboard=Scoreboard()
scoreboard.update_scoreboard()

def go_right():
    new_x = the_paddle.xcor() + 20
    the_paddle.setx(new_x)

def go_left():
    new_x = the_paddle.xcor() - 20
    the_paddle.setx(new_x)


screen.listen()
screen.onkey(go_left,key="Left")
screen.onkey(go_right,key="Right")
game_is_on=True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    if hit_count==turtle_count:
        game_is_on=False

    if ball.xcor()>290 or ball.xcor() < -290:
        ball.bounce()
    if ball.distance(the_paddle) < 70 and ball.ycor() < -340:
        ball.hit()
        hit_count+=1
    if ball.ycor()<-350:
        ball.reset_position()
        scoreboard.miss()
        scoreboard.update_scoreboard()
        if scoreboard.life_count==0:
            game_is_on=False

    for breakout_turtle in breakout_turtles[:]:
        if ball.distance(breakout_turtle) < 20:
            ball.hit()

            if breakout_turtle.ycor() == 300:
                scoreboard.point(5)
            elif breakout_turtle.ycor() == 275:
                scoreboard.point(3)
            elif breakout_turtle.ycor() == 250:
                scoreboard.point(2)
            else:
                scoreboard.point(1)

            breakout_turtle.hideturtle()
            breakout_turtle.goto(10000, 10000)
            breakout_turtles.remove(breakout_turtle)
            break


screen.exitonclick()