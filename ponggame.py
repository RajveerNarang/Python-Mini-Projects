import turtle

wn = turtle.Screen()
wn.title("The Pong Game by Rajveer Narang")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

#points calc
point_1 = 0
point_2 = 0


#paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("Orange")
#20x20 default
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)



#paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("red")
#20x20 default
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto( 350, 0)

#bounce ball
ball_1 = turtle.Turtle()
ball_1.speed(0)
ball_1.shape("circle")
ball_1.color("white")
ball_1.penup()
ball_1.goto( 0, 0)
ball_1.dx= 0.5
ball_1.dy= 0.5

#keep
keep =turtle.Turtle()
keep.speed(0)
keep.color("white")
keep.penup()
keep.hideturtle()
keep.goto(0 , 260)
keep.write("Player 1: 0 Player 2: 0", align="center", font=("Courier",24,"normal"))


#points



#funtion part paddle 1
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


#funtion part paddle 2
def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

#keyboard input module paddle 1
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_up, "W")

wn.listen()
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_1_down, "S")

#keyboard input module paddle 2
wn.listen()
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")




#Main loop
while  True:
    wn.update()

#move the ball
    ball_1.setx(ball_1.xcor() + ball_1.dx)
    ball_1.sety(ball_1.ycor() +ball_1.dy )


    

    
    if ball_1.ycor() > 290:
        ball_1.sety(290)
        ball_1.dy *=-1

    if ball_1.ycor() < -290:
        ball_1.sety(- 290)
        ball_1.dy *=-1

    if ball_1.xcor() > 390:
        ball_1.goto(0,0)
        ball_1.dx *= -1
        point_1 += 1
        keep.clear()
        keep.write("Player 1: {} Player 2: {}".format(point_1 , point_2), align="center", font=("Courier",24,"normal"))

        


    if ball_1.xcor() < -390:
        ball_1.goto(0,0)
        ball_1.dx *= -1
        point_2 += 1
        keep.clear()
        keep.write("Player 1: {} Player 2: {}".format(point_1 , point_2), align="center", font=("Courier",24,"normal"))

#collision with paddle
    if (ball_1.xcor() > 340 and ball_1.xcor() < 350) and (ball_1.ycor() < paddle_2.ycor() + 40 and ball_1.ycor() > paddle_2.ycor() -40 ):
        ball_1.setx(340)
        ball_1.dx *=-1

    if (ball_1.xcor() < -340 and ball_1.xcor() > -350) and (ball_1.ycor() < paddle_1.ycor() + 40 and ball_1.ycor() > paddle_1.ycor() -40 ):
        ball_1.setx(-340)
        ball_1.dx *=-1
   

    
   

    