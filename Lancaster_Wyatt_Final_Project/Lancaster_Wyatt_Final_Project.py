# Program name: Lancaster_Wyatt_Final_Project
# Author: Wyatt Lancaster
# Date: 5/3/2022
# Summary: User has to guess the correct answer to the questions
# Variables:
#   wndw: turtle variable to create a window
#   quest: text for the questions
#   score1: text for the score
#   A,B,C,D: text for the questions
#   correctAnswr: The amount of answers the user has gotten correct
#   currentQ: the current question the user is on

   
# import modules
import time
import turtle

# set up of gui screen
wndw = turtle.Screen()
wndw.setup(1000, 600)
wndw.colormode(255)
wndw.bgcolor(248, 240, 227)
wndw.title("Quiz Game")

# Make the boxes

# box C
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-450, -250)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.color("white")
for sides in range(2):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()

#box D
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(25, -250)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.color("white")
for sides in range(2):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()

# box A
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-450, -75)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.color("white")
for sides in range(2):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()


# box B
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(25, -75)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
turtle.color("white")
for sides in range(2):
    turtle.fd(425)
    turtle.left(90)
    turtle.fd(125)
    turtle.left(90)
turtle.end_fill()


# question box
turtle.penup()
turtle.goto(-450, 100)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(625)
    turtle.left(90)
    turtle.fd(150)
    turtle.left(90)
turtle.end_fill()


# score box
turtle.penup()
turtle.goto(255, 100)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(0)
for sides in range(2):
    turtle.fd(225)
    turtle.left(90)
    turtle.fd(150)
    turtle.left(90)
turtle.end_fill()


# Create question turtle
quest = turtle.Turtle()
quest.speed(0)
quest.hideturtle()
quest.penup()
quest.goto(-425, 150)

# Create score turtle
score1 = turtle.Turtle()
score1.speed(0)
score1.hideturtle()
score1.penup()
score1.goto(250, 125)

#Create answer turtles
# A
A = turtle.Turtle()
A.speed(0)
A.hideturtle()
A.penup()
A.goto(-425, -50)

#B
B = turtle.Turtle()
B.speed(0)
B.hideturtle()
B.penup()
B.goto(50, -50)

#C
C = turtle.Turtle()
C.speed(0)
C.hideturtle()
C.penup()
C.goto(-425, -225)

#D
D = turtle.Turtle()
D.speed(0)
D.hideturtle()
D.penup()
D.goto(50, -225)

# Opening welcome
quest.write("Welcome to The Quiz!", font=("Verdana", 23, "bold"))
time.sleep(2)
quest.clear()

quest.write("Press a, b, c, or d to answer!", font=("Verdana", 23, "bold"))
time.sleep(2)
quest.clear()

quest.write("Good Luck!", font=("Verdana", 23, "bold"))
time.sleep(2)
quest.clear()


# number of correct answers
correctAnswr = 0

score1.write("{}".format(correctAnswr), font=("Verdana", 45, "bold"))

#variables
CurrentQ = 1

# key functions
def chooseAnswerA():
    global select
    select = 'A'
    evaluate()

def chooseAnswerB():
    global select
    select = 'B'
    evaluate()

def chooseAnswerC():
    global select
    select = 'C'
    evaluate()

def chooseAnswerD():
    global select
    select = 'D'
    evaluate()

def evaluate():
    global correctAnswr
    global CurrentQ
    if correct == select:
        quest.clear()
        quest.write("Correct", font=("Verdana", 23, "bold"))
        time.sleep(1.2)
        score1.clear()
        correctAnswr += 1
        score1.write("{}".format(correctAnswr), font=("Verdana", 62, "bold"))
    else:
        quest.clear()
        quest.write("Wrong the answer was {}".format(correct), font=("Verdana", 23, "bold"))
        quest.sleep(1.2)
        quest.clear()
    CurrentQ += 1
    clearBoard()
    GetQuestionNum()

def GetQuestionNum():
    if CurrentQ == 2:
       question2()

def clearBoard():
    quest.clear()
    A.clear()
    B.clear()
    C.clear()
    D.clear()

def question1():
    quest.write("Sample question", font=("Verdana", 23, "bold"))
    A.write("A. Wrong answer", font=("Verdana", 23, "bold"))
    B.write("B. Correct answer", font=("Verdana", 23, "bold"))
    C.write("C. Wrong answer", font=("Verdana", 23, "bold"))
    D.write("D. Wrong answer", font=("Verdana", 23, "bold"))
    global correct
    correct = 'B'

def question2():
    quest.write("Sample question", font=("Verdana", 23, "bold"))
    A.write("A. Correct answer", font=("Verdana", 23, "bold"))
    B.write("B. Wrong answer", font=("Verdana", 23, "bold"))
    C.write("C. Wrong answer", font=("Verdana", 23, "bold"))
    D.write("D. Wrong answer", font=("Verdana", 23, "bold"))
    global correct
    correct = 'A'


#key bindings
wndw.listen()
wndw.onkeypress(chooseAnswerA, "a")
wndw.onkeypress(chooseAnswerB, "b")
wndw.onkeypress(chooseAnswerC, "c")
wndw.onkeypress(chooseAnswerD, "d")

#start game
question1()
turtle.mainloop()