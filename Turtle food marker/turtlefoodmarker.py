import turtle
import time
import random

delay = 0.3

#screen
wn = turtle.Screen()
wn.title("TurtleSnake by Rajveer Narang")
wn.bgcolor("black")
wn.setup(width = 600, height =600)
wn.tracer(0)#turns off screen updates
#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("turtle")
head.color("orange")
head.penup()
head.goto(0,0)
head.direction ="down"

# Treat
treat = turtle.Turtle()
treat.speed(0)
treat.shape("circle")
treat.color("blue")
treat.penup()
treat.goto(0,100)

part =[]




#functions
def up():
    head.direction = "up"

def down():
    head.direction = "down"

def left():
    head.direction = "left"

def right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#Bindings with keyboard
wn.listen()
wn.onkeypress(up, "w")
wn.onkeypress(down, "s") 
wn.onkeypress(left, "a") 
wn.onkeypress(right, "d")  

#Main Game Loop
while True:
    wn.update()
#check for collision


    if head.distance(treat) < 20:
        #Move treat
        j = random.randint(-290,290)
        k = random.randint(-290,290)
        treat.goto(j,k)

        #new bodypart
        bodyadd = turtle.Turtle()
        bodyadd.speed(0)
        bodyadd.shape("triangle")
        bodyadd.color("green")
        bodyadd.penup()
        part.append(bodyadd)

        #move the end body part first
        for index in range(len(part)-1, 0, -1):
            x = part [index-1].xcor()
            y = part [index-1].ycor()
            part[index].goto(x,y)

            #Move segment 0 with the head
            if len(part) > 0:
                x = head.xcor()
                y = head.ycor()
                part[0].goto(x,y)
            



    move()

    time.sleep(delay)

wn.mainloop()