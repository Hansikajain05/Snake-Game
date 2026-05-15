import turtle
import random
import time

from requests import head
delay=0.1
score=0
highest_score=0
bodies=[]

#creating a Screen
s1=turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("black")
s1.setup(width=600,height=600)

#creating a snake head
h1=turtle.Turtle()
h1.shape("circle")
h1.speed(0)
h1.color("white")
h1.fillcolor("white")
h1.penup()
h1.goto(0,0)
h1.direction="stop"

#creating a food
f1=turtle.Turtle()
f1.shape("square")
f1.speed(0)
f1.color("red")
f1.fillcolor("red")
f1.penup()
f1.ht()
f1.goto(280,280)
f1.st()
f1.direction="stop"

#score board
sb=turtle.Turtle()
sb.ht()
sb.penup()
sb.goto(-260,260)
sb.write("Score: 0  Highest Score: 0",align="left",font=("Arial",14,"normal"))

def moveup():
    if h1.direction!="down":
        h1.direction="up"

def movedown():
    if h1.direction!="up":
        h1.direction="down"

def moveleft():
    if h1.direction!="right":
        h1.direction="left"

def moveright():
    if h1.direction!="left":
        h1.direction="right"
        
def movestop():
    h1.direction="stop"
        
def move():
    if h1.direction=="up":
        y=h1.ycor()
        h1.sety(y+20)
    if h1.direction=="down":
        y=h1.ycor()
        h1.sety(y-20)
    if h1.direction=="left":
        x=h1.xcor()
        h1.setx(x-20)
    if h1.direction=="right":
        x=h1.xcor()
        h1.setx(x+20)
        
        
#event handling
s1.listen()
s1.onkeypress(moveup,"Up")
s1.onkeypress(movedown,"Down")
s1.onkeypress(moveleft,"Left")
s1.onkeypress(moveright,"Right")
s1.onkeypress(movestop,"space")

while True:
    s1.update()
    
    # check collision with border
    if h1.xcor()>290 :
        h1.setx(-290)
    if h1.xcor()<-290 :
        h1.setx(290)
    if h1.ycor()>290 :
        h1.sety(-290)
    if h1.ycor()<-290 :
        h1.sety(290)
        
    # check collision with food
    if h1.distance(f1)<20:
        # move food to random place
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        f1.goto(x,y)
        
        # add body to snake
        b1=turtle.Turtle()
        b1.shape("square")
        b1.speed(0)
        b1.color("blue")
        b1.fillcolor("lightblue")
        b1.penup()
        bodies.append(b1)
        
        # increase score
        score+=100
        if score>highest_score:
            highest_score=score
        sb.clear()
        sb.write("Score: {} | Highest Score: {}".format(score,highest_score),align="left",font=("Arial",14,"normal"))
        delay=delay-0.001   #increase speed
    # move the  snake body
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)
        if len(bodies)>0:
            x=h1.xcor()
            y=h1.ycor()
            bodies[0].goto(x,y)
    move()
        
    # check collision with body
    for b in bodies:
        if b.distance(h1)<20:
            time.sleep(1)
            h1.goto(0,0)
            h1.direction="stop"
            for b in bodies:
                b.ht()
            bodies.clear()
            score=0
            delay=0.1
            sb.clear()
            sb.write("Score: {} | Highest Score: {}".format(score,highest_score),align="left",font=("Arial",14,"normal"))
            
    time.sleep(delay)
s1.mainloop()        
        
        