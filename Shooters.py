import turtle
import time
import random

delay = 0.01
Black=0
White=0

w=turtle.Screen()
w.title("Shooters")
w.bgcolor("yellow")
w.setup(width=800,height=450)
w.tracer(0)

n=0
y1=160
borders=[]
while n<5:
    border=turtle.Turtle()
    border.shape("square")
    border.color("blue")
    border.penup()
    border.goto(-300,y1)
    y1=y1-90
    borders.append(border)
    n=n+1

n=0
y1=170
borders1=[]
while n<5:
    border=turtle.Turtle()
    border.shape("square")
    border.color("blue")
    border.penup()
    border.goto(300,y1)
    y1=y1-90
    borders1.append(border)
    n=n+1
    
plate=turtle.Turtle()
plate.shape("square")
plate.color("black")
plate.penup()
plate.goto(-360,0)
plate.direction="stop"

plate1=turtle.Turtle()
plate1.shape("square")
plate1.color("black")
plate1.penup()
plate1.goto(-360,20)
plate1.direction="stop"

plate2=turtle.Turtle()
plate2.shape("square")
plate2.color("black")
plate2.penup()
plate2.goto(-360,-20)
plate2.direction="stop"

plate3=turtle.Turtle()
plate3.shape("square")
plate3.color("white")
plate3.penup()
plate3.goto(360,0)
plate3.direction="stop"

plate4=turtle.Turtle()
plate4.shape("square")
plate4.color("white")
plate4.penup()
plate4.goto(360,20)
plate4.direction="stop"

plate5=turtle.Turtle()
plate5.shape("square")
plate5.color("white")
plate5.penup()
plate5.goto(360,-20)
plate5.direction="stop"

comet=turtle.Turtle()
comet.shape("circle")
comet.color("black")
comet.penup()
comet.goto(-340,0)
comet.direction="stop"

comet1=turtle.Turtle()
comet1.shape("circle")
comet1.color("white")
comet1.penup()
comet1.goto(340,0)
comet1.direction="stop"

pen = turtle.Turtle() 
pen.speed(0) 
pen.shape("circle")
pen.color("red") 
pen.penup() 
pen.hideturtle() 

pen.goto(0, 190) 
pen.write("Shooters",align="center",font=("algerian",24))
pen.goto(0, 160)
pen.write("Black : 0   White : 0", align="center",font=("candara", 22, "bold"))

def goup1(): 
        plate.direction = "left"
def godown1():
        plate.direction = "right"
def goup2(): 
        plate3.direction = "left"
def godown2():
        plate3.direction = "right"
def goshoot1():
        comet.direction = "down"
def goshoot2():
        comet1.direction = "down"

def move(): 
    if plate.direction == "left": 
        x = plate.ycor() 
        plate.sety(x+20)
        x = plate1.ycor() 
        plate1.sety(x+20)
        x = plate2.ycor() 
        plate2.sety(x+20)
        x = comet.xcor()
        if x < -320:
            x = comet.ycor()
            comet.sety(x+20)
        else:
            pass
        plate.direction="stop"
    if plate.direction == "right": 
        x = plate.ycor() 
        plate.sety(x-20)
        x = plate1.ycor() 
        plate1.sety(x-20)
        x = plate2.ycor()
        plate2.sety(x-20)
        x = comet.xcor()
        if x < -320:
            x = comet.ycor()
            comet.sety(x-20)
        else:
            pass
        plate.direction="stop"
    if plate3.direction == "left": 
        x = plate3.ycor() 
        plate3.sety(x+20)
        x = plate4.ycor() 
        plate4.sety(x+20)
        x = plate5.ycor() 
        plate5.sety(x+20)
        x = comet1.xcor()
        if x > 320:
            x = comet1.ycor()
            comet1.sety(x+20)
        else:
            pass
        plate3.direction="stop"
    if plate3.direction == "right": 
        x = plate3.ycor() 
        plate3.sety(x-20)
        x = plate4.ycor() 
        plate4.sety(x-20)
        x = plate5.ycor() 
        plate5.sety(x-20)
        x = comet1.xcor()
        plate3.direction="stop"
        if x > 320:
            x = comet1.ycor()
            comet1.sety(x-20)
        else:
            pass
    if comet.direction == "down": 
        x = comet.xcor()
        comet.setx(x+35)
    if comet1.direction == "down": 
        x = comet1.xcor()
        comet1.setx(x-35)

w.listen() 
w.onkeypress(goup1, "q") 
w.onkeypress(godown1, "z")
w.onkeypress(goup2, "9") 
w.onkeypress(godown2, "3")
w.onkeypress(goshoot1, "s") 
w.onkeypress(goshoot2, "5")

print("Welcome to Shooters.")
print("The controls are simple :-")
print("For Black press q for up and z for down and s for shoot.")
print("For White press 9 for up and 3 for down and 5 for shoot.")

while True:
    w.update()
    if Black==50:
        pen.goto(0, 0)
        pen.color("black")
        pen.write("Black Won",align="center",font=("algerian",40))
        time.sleep(1)
        break
    if White==50:
        pen.goto(0, 0)
        pen.color("white")
        pen.write("White Won",align="center",font=("algerian",40))
        time.sleep(1)
        break
    if plate.distance(comet1) < 20 or plate1.distance(comet1) < 20 or plate2.distance(comet1) < 20 or plate3.distance(comet) < 20 or plate4.distance(comet) < 20 or plate5.distance(comet) < 20:
        time.sleep(0.75)
        if plate.distance(comet1) < 20 or plate1.distance(comet1) < 20 or plate2.distance(comet1) < 20 :
            White=White+10
        else:
            Black=Black+10
        delay=0.01
        y=plate.ycor()
        comet.sety(y)
        comet.setx(-340)
        y=plate3.ycor()
        comet1.sety(y)
        comet1.setx(340)
        comet.direction=comet1.direction="stop"
        pen.clear()
        pen.goto(0, 190) 
        pen.write("Shooters",align="center",font=("algerian",24))
        pen.goto(0, 160)
        pen.write("Black : {}    White : {} ".format(Black, White), align="center", font=("candara", 22, "bold"))
    if plate2.ycor() < -185 or plate1.ycor() > 185:
        if plate2.ycor() < -185 :
            plate.direction = "left"
        else:
            plate.direction = "right"
    if comet1.xcor() < -370 or comet.xcor() > 370:
        if comet1.xcor() < -370 :
            y=plate3.ycor()
            comet1.sety(y)
            comet1.setx(340)
            comet1.direction="stop"
        else:
            y=plate.ycor()
            comet.sety(y)
            comet.setx(-340)
            comet.direction="stop"
    if plate5.ycor() < -185 or plate4.ycor() > 185:
        if plate5.ycor() < -185 :
            plate3.direction = "left"
        else:
            plate3.direction = "right"
    for x in borders1:
        if x.distance(comet) < 20:
            y=plate.ycor()
            comet.sety(y)
            comet.setx(-340)
            comet.direction="stop"
            col=random.choices(["green","blue","purple","brown","cyan","magenta","maroon","skyblue","chocolate","turquoise","navy blue"])
            x.color(col)
    for x in borders:
        if x.distance(comet1) < 20:
            y=plate3.ycor()
            comet1.sety(y)
            comet1.setx(340)
            comet1.direction="stop"
            col2=random.choices(["green","blue","purple","brown","cyan","magenta","maroon","skyblue","chocolate","turquoise","navy blue"])
            x.color(col2)
    move()
    time.sleep(delay)
w.mainloop()
exit()
