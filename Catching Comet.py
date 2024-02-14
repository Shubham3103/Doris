import turtle
import time
import random

delay = 0.1
score=0
hscore=0

w=turtle.Screen()
w.title("Catching Comet")
w.bgcolor("black")
w.setup(width=800,height=700)
w.tracer(0)

plate=turtle.Turtle()
plate.shape("square")
plate.color("white")
plate.penup()
plate.goto(0,-310)
plate.direction="stop"

plate1=turtle.Turtle()
plate1.shape("square")
plate1.color("white")
plate1.penup()
plate1.goto(20,-310)
plate1.direction="stop"

plate2=turtle.Turtle()
plate2.shape("square")
plate2.color("white")
plate2.penup()
plate2.goto(-20,-310)
plate2.direction="stop"

plate3=turtle.Turtle()
plate3.shape("square")
plate3.color("white")
plate3.penup()
plate3.goto(-40,-310)
plate3.direction="stop"

plate4=turtle.Turtle()
plate4.shape("square")
plate4.color("white")
plate4.penup()
plate4.goto(40,-310)
plate4.direction="stop"

comet=turtle.Turtle()
comet.shape("circle")
comet.color("red")
comet.penup()
x=random.randint(-350,350)
comet.goto(x,310)

pen = turtle.Turtle() 
pen.speed(0) 
pen.shape("square")
pen.color("white") 
pen.penup() 
pen.hideturtle() 

pen.goto(0, 310) 
pen.write("Catching Comet",align="center",font=("algerian",26))
pen.goto(0, 280)
pen.write("Score : 0   High Score : 0", align="center",font=("candara", 24, "bold"))
pen.goto(0, 250)
pen.write("Press - 4 for left and 6 for right", align="center",font=("candara", 22))

def goleft(): 
        plate.direction = "left"
        plate1.direction = "left"
        plate2.direction = "left"
        plate3.direction = "left"
        plate4.direction = "left"
def goright():
        plate.direction = "right"
        plate1.direction = "right"
        plate2.direction = "right"
        plate3.direction = "right"
        plate4.direction = "right"
comet.direction = "down"
def move(): 
    if plate.direction == "left": 
        x = plate.xcor() 
        plate.setx(x-30)
        x = plate1.xcor() 
        plate1.setx(x-30)
        x = plate2.xcor() 
        plate2.setx(x-30)
        x = plate3.xcor() 
        plate3.setx(x-30)
        x = plate4.xcor() 
        plate4.setx(x-30)
    if plate.direction == "right": 
        x = plate.xcor() 
        plate.setx(x+30)
        x = plate1.xcor() 
        plate1.setx(x+30)
        x = plate2.xcor() 
        plate2.setx(x+30)
        x = plate3.xcor() 
        plate3.setx(x+30)
        x = plate4.xcor() 
        plate4.setx(x+30)
    if comet.direction == "down": 
        y = comet.ycor() 
        comet.sety(y-20)
w.listen() 
w.onkeypress(goleft, "4") 
w.onkeypress(goright, "6")
print("Welcome to Catching comet.")
print("The controls are simple :-")
print("press 4 for left and 6 for right.")
print("Catch the comet you will get 10 points")
print("You will win at 100 points")
print("If you will miss it, you will lose it.")

while True:
    w.update()
    if score==100:
        pen.goto(0, 0)
        pen.write("You Won",align="center",font=("algerian",40))
        time.sleep(1)
        break
    if  comet.ycor() < -340:
        time.sleep(1) 
        plate.goto(0, -310) 
        plate.direction = "Stop"
        plate1.goto(20, -310) 
        plate1.direction = "Stop"
        plate2.goto(-20, -310) 
        plate2.direction = "Stop"
        plate3.goto(-40, -310) 
        plate3.direction = "Stop"
        plate4.goto(40, -310) 
        plate4.direction = "Stop"
        x = random.randint(-350, 350)
        comet.direction = "down"
        comet.shape("circle") 
        comet.color("red")
        comet.goto(x, 310)
        score = 0
        delay = 0.1
        pen.clear()
        pen.goto(0, 310)
        pen.write("Catching Comet",align="center",font=("algerian",26))
        pen.goto(0, 280)
        pen.write("Score : {}     High Score : {} ".format(score, hscore), align="center", font=("candara", 24, "bold"))
        pen.goto(0, 250)
        pen.write("Press - 4 for left and 6 for right", align="center",font=("candara", 22))
    if plate.distance(comet) < 20 or plate1.distance(comet) < 20 or plate2.distance(comet) < 20 or plate3.distance(comet) < 20or plate4.distance(comet) < 20: 
        x = random.randint(-350, 350)  
        comet.shape("circle") 
        comet.color("red") 
        comet.goto(x, 310)
        delay -= 0.01
        score += 10
        if score > hscore: 
            hscore = score 
        pen.clear()
        pen.goto(0, 310)
        pen.write("Catching Comet",align="center",font=("algerian",26))
        pen.goto(0, 280)
        pen.write("Score : {}     High Score : {} ".format( 
            score, hscore), align="center", font=("candara", 24, "bold")) 
        pen.goto(0, 250)
        pen.write("Press - 4 for left and 6 for right", align="center",font=("candara", 22))
    if plate3.xcor() < -350 or plate4.xcor() > 350:
        if plate.direction == "right" :
            plate.direction = "left"
            plate1.direction = "left"
            plate2.direction = "left"
        else:
            plate.direction = "right"
            plate1.direction = "right"
            plate2.direction = "right"
    move()
    time.sleep(delay)
w.mainloop()
exit()  
