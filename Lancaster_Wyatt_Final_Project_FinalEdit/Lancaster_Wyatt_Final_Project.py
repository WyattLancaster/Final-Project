# Program name: Lancaster_Wyatt_Final_Project
# Author: Wyatt Lancaster
# Date: 5/16/2022
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

# lives variable



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

# Create lives turtle
lives = turtle.Turtle()
lives.speed(0)
lives.hideturtle()
lives.penup()
lives.goto(250, 180)

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

# number of current lives
playerLives = 5

lives.write("{}".format(playerLives), font=("Verdana", 45, "bold"))

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
    global playerLives
    if correct == select:
        quest.clear()
        quest.write("Correct", font=("Verdana", 23, "bold"))
        time.sleep(1.2)
        quest.clear()
        score1.clear()
        correctAnswr += 1
        score1.write("{}".format(correctAnswr), font=("Verdana", 45, "bold"))
        CurrentQ = CurrentQ + 1
    else:
        lives.clear()
        playerLives -= 1
        lives.write("{}".format(playerLives), font=("Verdana", 45, "bold"))
        quest.clear()
        quest.write("Wrong the answer was {}".format(correct), font=("Verdana", 23, "bold"))
        time.sleep(1.2)
        quest.clear()
        CurrentQ = CurrentQ + 1
    clearBoard()
    GetQuestionNum()
    GetPlayerLives()
    winningEnding()

def GetQuestionNum():
    if CurrentQ == 2:
       question2()
    elif CurrentQ == 3:
        question3()
    elif CurrentQ == 4:
        question4()
    elif CurrentQ == 5:
        question5()
    elif CurrentQ == 6:
       question6()
    elif CurrentQ == 7:
        question7()
    elif CurrentQ == 8:
        question8()
    elif CurrentQ == 9:
        question9()
    elif CurrentQ == 10:
        question10()

def GetPlayerLives():
    if playerLives <= 0:
        gameOver()

def winningEnding():
    if CurrentQ >= 11:
        youWon()

def clearBoard():
    quest.clear()
    A.clear()
    B.clear()
    C.clear()
    D.clear()

def gameOver():
    quest.write("Game Over. Final score was {}".format(correctAnswr), font=("Verdana", 23, "bold"))

def youWon():
    quest.write("You Won! Final score was {}/10".format(correctAnswr), font=("Verdana", 23, "bold"))

def question1():
    quest.write("What is 9x3", font=("Verdana", 23, "bold"))
    A.write("A. 64", font=("Verdana", 23, "bold"))
    B.write("B. 27", font=("Verdana", 23, "bold"))
    C.write("C. 32", font=("Verdana", 23, "bold"))
    D.write("D. 36", font=("Verdana", 23, "bold"))
    global correct
    correct = 'B'

def question2():
    quest.write("What is 8x2+13", font=("Verdana", 23, "bold"))
    A.write("A. 29", font=("Verdana", 23, "bold"))
    B.write("B. 21", font=("Verdana", 23, "bold"))
    C.write("C. 32", font=("Verdana", 23, "bold"))
    D.write("D. 45", font=("Verdana", 23, "bold"))
    global correct
    correct = 'A'

def question3():
    quest.write("What is 32/4x2", font=("Verdana", 23, "bold"))
    A.write("A. 16", font=("Verdana", 23, "bold"))
    B.write("B. 23", font=("Verdana", 23, "bold"))
    C.write("C. 4", font=("Verdana", 23, "bold"))
    D.write("D. 18", font=("Verdana", 23, "bold"))
    global correct
    correct = 'C'

def question4():
    quest.write("5x16", font=("Verdana", 23, "bold"))
    A.write("A. 47", font=("Verdana", 23, "bold"))
    B.write("B. 56", font=("Verdana", 23, "bold"))
    C.write("C. 72", font=("Verdana", 23, "bold"))
    D.write("D. 80", font=("Verdana", 23, "bold"))
    global correct
    correct = 'D'

def question5():
    quest.write("What is 27/9", font=("Verdana", 23, "bold"))
    A.write("A. 2", font=("Verdana", 23, "bold"))
    B.write("B. 5", font=("Verdana", 23, "bold"))
    C.write("C. 3", font=("Verdana", 23, "bold"))
    D.write("D. 4", font=("Verdana", 23, "bold"))
    global correct
    correct = 'C'

def question6():
    quest.write("What is 125/5", font=("Verdana", 23, "bold"))
    A.write("A. 15", font=("Verdana", 23, "bold"))
    B.write("B. 25", font=("Verdana", 23, "bold"))
    C.write("C. 4", font=("Verdana", 23, "bold"))
    D.write("D. 10", font=("Verdana", 23, "bold"))
    global correct
    correct = 'B'

def question7():
    quest.write("What is (72-12)x2", font=("Verdana", 23, "bold"))
    A.write("A. 120", font=("Verdana", 23, "bold"))
    B.write("B. 48", font=("Verdana", 23, "bold"))
    C.write("C. 27", font=("Verdana", 23, "bold"))
    D.write("D. 140", font=("Verdana", 23, "bold"))
    global correct
    correct = 'A'

def question8():
    quest.write("What is 59+8", font=("Verdana", 23, "bold"))
    A.write("A. 64", font=("Verdana", 23, "bold"))
    B.write("B. 52", font=("Verdana", 23, "bold"))
    C.write("C. 67", font=("Verdana", 23, "bold"))
    D.write("D. 63", font=("Verdana", 23, "bold"))
    global correct
    correct = 'C'

def question9():
    quest.write("What is 82-84", font=("Verdana", 23, "bold"))
    A.write("A. 0", font=("Verdana", 23, "bold"))
    B.write("B. 2", font=("Verdana", 23, "bold"))
    C.write("C. 5", font=("Verdana", 23, "bold"))
    D.write("D. -2", font=("Verdana", 23, "bold"))
    global correct
    correct = 'D'

def question10():
    quest.write("What is 100x3-150", font=("Verdana", 23, "bold"))
    A.write("A. 150", font=("Verdana", 23, "bold"))
    B.write("B. 239", font=("Verdana", 23, "bold"))
    C.write("C. 120", font=("Verdana", 23, "bold"))
    D.write("D. 200", font=("Verdana", 23, "bold"))
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