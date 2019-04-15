# COP 3035 
# Final Project - Hangman
# Cody Mitchell, Haley Little, Camron Clark

'''
    Main game begins on line 200
    TODO:
        1. Print new screen at end of game
            Winning screen
            Losing Screen
            *already asks if user wants to rematch*
        2. Print error when user enters wrong num
        3. Print hangman
'''

from __future__ import print_function		# use Python3 printing
import turtle
import random

#graphics setup
t = turtle.Turtle()
wn = turtle.Screen()
wn.title("Hangman V1.1")
t.hideturtle()
t.speed(0)
wn.tracer(0,0)

wn.screensize()
wn.setup(width = 1.0, height = 1.0)

### DEFINITIONS ###

def randomWord(words):
	# selects a random word from the list
	selection = random.randint(0, len(words) - 1)
	return words[selection]


def drawRectangle(width, height, tilt, penColor, fillColor):
    #prints rectangle
    t.left(tilt)
    t.color(penColor, fillColor)
    t.begin_fill()
    for _ in range(0,2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def printScreen(answer, guessedLetters, attemptsLeft):
    #parent func that refreshes the screen using each print method
    t.clear()
    t.penup()
    t.setx(-485)
    t.sety(-400)
    t.pendown()
    drawRectangle(1000, 300, 0, "#3e6fa0", "#3e6fa0")
    printAttempts(attemptsLeft)
    printGuesses(answer, guessedLetters)
    printWord(answer, guessedLetters)
    #printHangman(attemptsLeft)

def printAttempts(attemptsLeft):
    #prints # of attempts left at top middle of screen
    t.color('black', 'black')
    t.penup()
    t.setx(-100)
    t.sety(350)
    t.pendown()
    t.write('Attempts Left: ' + str(attemptsLeft), font=("Arial", 24, 'normal'))

#print each character in box on right side of screen
def printGuesses(answer, guessedLetters):
    #outline box
    t.penup()
    t.setx(325)
    t.sety(-100)
    t.pendown()
    drawRectangle(150, 400, 0, "black", "white")

    #title ("Guessed Letters:")
    t.penup()
    t.setx(350)
    t.sety(270)
    t.pendown()
    t.color('black', 'black')
    t.write('Guessed Letters:', font=("Arial", 12, 'underline'))
            #each char
    
    #print each guessed letter
    #setting up initial pos
    t.penup()
    t.setx(340)
    t.sety(230)
    t.pendown()
    i = 0
    for l in guessedLetters:
        #don't print space bar
        if l == ' ':
            continue
        #move to next line after three letters    
        if i == 3:
            t.penup()
            t.right(90)
            t.forward(40)
            t.right(90)
            t.forward(90)
            t.left(180)
            t.pendown()
            i = 0
        if l not in answer:
             t.color('red', 'red')
        else:
            t.color('black', 'black')

        #finally print letter
        t.penup()
        t.forward(30)
        t.pendown()
        t.write(l, font=("Arial", 20, 'normal'))
        i += 1

#prints answer below hangman (using _ for unknown letters)
def printWord(answer, guessedLetters):
    #supposed to have black outline but I can't get that to work
    t.color('white', 'black')
    t.penup()
    t.setx(-130)
    t.sety(-150)
    t.pendown()
    #goes through answer, printing each letter if already guessed, or _ if not
    for s in answer:
        t.penup()
        t.forward(30)
        t.pendown()

        #goes to next line for each word inside of letter
        if s == ' ':
            t.penup()
            t.setx(-100)
            t.sety(t.ycor() - 30)
            t.pendown()

        elif s in guessedLetters:
            t.write(s, font=("Arial", 20, 'normal'))
        else:
            t.write('_', font=("Arial", 20, 'normal'))


#Get user input through turtle
def getInput(guessedLetters):
    #must not be guessed, > 1 letter, or non-alphabetical
    while True:
        letter = wn.textinput("Guess your word", "Enter a letter: ").lower()
        if letter not in guessedLetters and len(letter) == 1 and letter in 'abcdefghijklmnopqrstuvwxyz':
            return letter

#Menu background
def printMenu():
    t.clear()
    t.penup()
    t.setx(-485)
    t.sety(-400)
    t.pendown()
    drawRectangle(1000, 300, 0, "#3e6fa0", "#3e6fa0")

    #Menu GUI that includes name of project and our names
    t.color('black', 'black')
    t.penup()
    t.setx(-150)
    t.sety(50)
    t.pendown()
    t.write("Hangman V1", font=("Arial", 40, 'normal'))
    t.penup()
    t.setx(-200)
    t.sety(0)
    t.pendown()
    t.write("By Cody, Haley, and Camron", font=("Arial", 24, 'normal'))


def gameSetup():

    game = wn.numinput("Start Game", "Please enter 1 or 2 for number of players: ", minval=1, maxval=2)
    
    while True:
        if game == 1:
            words = 'ash, apple, airplane, amazing, bee sting, bird, baby, birthday cake, bubble, bananas, cat, cow goes moo, chocolate, chicken, cup, dog, diamond, doorbell, door, doll, egg, elephant, easy, ear ache, flying fish, fuzy, fruit, funny, frog, goat, gingerbread man, garden, green bean, greatful, high, hot, hello, happy, horse, ice, ice cream, itch, jolly, jingle, junk, kitchen, knife, kangaroo, leg, library, lion, light beam, leopard, map, milk, milkshake, money, platypus, pants, parachute, pepper, puppy, queen, rainbow, rocket, roof, salt and pepper, school, sandwich, shoes, snail, spaceship, sports, star, swimming, teeth, tennis, tiger, train, triangle, umbrella, vulture, vacuum, wax, water, web, worm, x ray'.split(', ')
            return randomWord(words) 
        elif game == 2:
            return wn.textinput("Choose Word", "Player 2, please enter your challenge word: ").lower()

  #Play game
while True:
    #setup
    attL = 5
    attemptsLeft = attL
    guessedLetters = ''
    correctLetters = ''
    printMenu()
    answer = gameSetup()
    #auto adds ' ' so that user doesn't have to guess a space
    if ' ' in answer:
        guessedLetters += ' '
        correctLetters += ' '

    #OK actually play game this time
    while True:
        printScreen(answer, guessedLetters, attemptsLeft)
        if attemptsLeft == 0:
            break
        elif len(set(answer)) == len(correctLetters):
            break
        else:
            #get valid word, and either reduce attempts or add to correct letters
            letter = getInput(guessedLetters)
            guessedLetters += letter
            if letter not in answer:
                attemptsLeft -= 1
            else:
                correctLetters += letter
    rematch = wn.textinput("Game over.", "Would you like to play again? (yes or no)").lower().startswith("y")
    #if user does not want to rematch, ends game
    if not rematch:
        break
    



wn.exitonclick()