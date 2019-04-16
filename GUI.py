# COP 3035 
# Final Project - Hangman
# Cody Mitchell, Haley Little, Camron Clark
# Must be run with python 3

'''
    Main game begins on line 200
    TODO:
        Print hangman
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

### FUNCTIONS ###


    ### Graphics Functions ###

#Menu background
def printMenu():
    #refresh screen, draw background
    t.clear()
    t.penup()
    t.setx(-485)
    t.sety(-400)
    t.pendown()
    drawRectangle(1000, 300, 0, "#3e6fa0", "#3e6fa0")

    #Main Menu GUI that includes name of project and our names
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

    ### Choose num of players/ select word ###
def gameSetup():
    #user can only enter 1 or 2
    game = wn.numinput("Start Game", "Please enter 1 or 2 for number of players: ", minval=1, maxval=2)
    
    if game == 1:
        #chooses rand word from list
        words = 'ash, apple, airplane, amazing, bee sting, bird, baby, birthday cake, bubble, bananas, cat, cow goes moo, chocolate, chicken, cup, dog, diamond, doorbell, door, doll, egg, elephant, easy, ear ache, flying fish, fuzy, fruit, funny, frog, goat, gingerbread man, garden, green bean, greatful, high, hot, hello, happy, horse, ice, ice cream, itch, jolly, jingle, junk, kitchen, knife, kangaroo, leg, library, lion, light beam, leopard, map, milk, milkshake, money, platypus, pants, parachute, pepper, puppy, queen, rainbow, rocket, roof, salt and pepper, school, sandwich, shoes, snail, spaceship, sports, star, swimming, teeth, tennis, tiger, train, triangle, umbrella, vulture, vacuum, wax, water, web, worm, x ray'.split(', ')
        return randomWord(words) 
    elif game == 2:
        #prompts second user to input their challenge word
        return wn.textinput("Choose Word", "Player 2, please enter your challenge word: ").lower()


    # helper function for gameSetup
def randomWord(words):
	# selects a random word from the list
	selection = random.randint(0, len(words) - 1)
	return words[selection]

    ### Main game screen ###
def printScreen(answer, guessedLetters, attemptsLeft):
    #Main func that refreshes the screen tying each print method into one place
    t.clear()
    t.penup()
    t.setx(-485)
    t.sety(-400)
    t.pendown()
    drawRectangle(1000, 300, 0, "#3e6fa0", "#3e6fa0")   #background
    printAttempts(attemptsLeft)                         #top of screen
    printGuesses(answer, guessedLetters)                #right of screen
    printHangman(attemptsLeft)                          #middle of screen
    printWord(answer, guessedLetters)                   #middle, below the hangman


def drawRectangle(width, height, tilt, penColor, fillColor):
    #prints rectangle given parameters
    t.left(tilt)
    t.color(penColor, fillColor)
    t.begin_fill()
    for _ in range(0,2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def printAttempts(attemptsLeft):
    #prints # of attempts left, at top middle of screen
    t.color('black', 'black')
    t.penup()
    t.setx(-100)
    t.sety(350)
    t.pendown()
    t.write('Attempts Left: ' + str(attemptsLeft), font=("Arial", 24, 'normal'))

def printGuesses(answer, guessedLetters):
    #print each character in box on right side of screen

    #outline box
    t.penup()
    t.setx(325)
    t.sety(-100)
    t.pendown()
    drawRectangle(190, 400, 0, "black", "white")

    #title ("Guessed Letters:")
    t.penup()
    t.setx(350)
    t.sety(270)
    t.pendown()
    t.color('black', 'black')
    t.write('Guessed Letters:', font=("Arial", 12, 'underline'))

    ### print each guessed letter ###
    #setting up initial pos
    t.penup()
    t.setx(340)
    t.sety(230)
    t.pendown()
    i = 0
    for l in guessedLetters:
        #print each letter the user has guessed inside of box
        if l == ' ':
            #don't print space bar that was added during setup
            continue
        elif i == 3:
            #move to next line after three letters
            t.penup()
            t.right(90)
            t.forward(40)
            t.right(90)
            t.forward(90)
            t.left(180)
            t.pendown()
            i = 0
        elif l not in answer:
            #if letter wasn't correct (inside of answer), print in red
            t.color('red', 'red')
        else:
            #otherwise, print in black
            t.color('black', 'black')

        #finally, print letter
        t.penup()
        t.forward(30)
        t.pendown()
        t.write(l, font=("Arial", 20, 'normal'))
        i += 1


def printWord(answer, guessedLetters):
    #prints answer below hangman (using _ for unknown letters)
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

        #each word in answer (if applicable) is printed on a seperate line
        if s == ' ':
            t.penup()
            t.setx(-130)
            t.sety(t.ycor() - 30)
            t.pendown()

        elif s in guessedLetters:
            t.write(s, font=("Arial", 20, 'normal'))
        else:
            t.write('_', font=("Arial", 20, 'normal'))

def printBase():
    t.penup()
    t.setpos(-175, 200)
    t.seth(0)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(175)
    t.forward(-350)
def printHead():
    t.penup()
    t.seth(0)
    t.setpos(-200, 100)
    t.pendown()
    t.circle(25)
def printHangman(attemptsLeft):
    t.color('black', 'black')
    printBase()
    if attemptsLeft == 7:
        printBase()
        printHead()
    elif attemptsLeft == 6:
        #print base
        #print head
        a = ''
    elif attemptsLeft == 5:
        a = ''
    elif attemptsLeft == 4:
        a = ''
    elif attemptsLeft == 3:
        a = ''
    elif attemptsLeft == 2:
        a = ''
    elif attemptsLeft == 1:
        a = ''
    elif attemptsLeft == 0:
        a = ''
    t.seth(0)

### Game Setup functions ###

    
def errorMessage():
    ### Sets pos/ font of turtle to print message to user screen ###
    t.color('red', 'red')
    t.penup()
    t.setpos(-200, 100)
    t.pendown()

    
def getInput(answer, guessedLetters, attemptsLeft):
    ### returns a valid user-chosen character ###
    while True:
        letter = wn.textinput("Guess your word", "Enter a letter: ").lower()

	# can only guess each letter once
        if letter in guessedLetters:
            printScreen(answer, guessedLetters, attemptsLeft)
            errorMessage()
            t.write('OOPS! You already guessed that letter, try again.', font=("Arial", 12, 'normal'))

	# can only guess one letter at a time
        elif len(letter) != 1:
            printScreen(answer, guessedLetters, attemptsLeft)
            errorMessage()
            t.write('OOPS! Only enter one letter at one time, try again.', font=("Arial", 12, 'normal'))

	# must be a letter in the alphabet
        elif letter not in 'abcdefghijklmnopqrstuvwxyz':
            printScreen(answer, guessedLetters, attemptsLeft)
            errorMessage()
            t.write('OOPS! You must enter a letter in the alphabet, try again.', font=("Arial", 12, 'normal'))

	# if correct input, return the letter
        else:
            printScreen(answer, guessedLetters, attemptsLeft)
            return letter



####################################################   MAIN GAME   ####################################################





while True:

        #game setup
    attemptsLeft = 8
    guessedLetters = '' #stores each valid letter the player guesses
    correctLetters = '' #stores each guessed letter that is within answer
    printMenu()
    answer = gameSetup() #chooses rand word for 1 player, user input for 2 player

        #add ' ' if answer has a space in it, because user shouldn't have to guess ' ' 
    if ' ' in answer:
        guessedLetters += ' '
        correctLetters += ' '


        #OK actually play game this time
    while True:
        printScreen(answer, guessedLetters, attemptsLeft)
        if attemptsLeft == 0:
            #player has run out of attempts
            errorMessage()
            t.write('Boo you lost. Answer was: ' + answer, font=("Arial", 20, 'bold'))
            break
        elif len(set(answer)) == len(correctLetters):
            #player has guessed all letters in answer
            errorMessage()
            t.write('You win! Answer was: ' + answer, font=("Arial", 20, 'bold'))
            break
        else:
            #get valid char, and either reduce attempts or add to correct letters
            letter = getInput(answer, guessedLetters, attemptsLeft)
            guessedLetters += letter
            if letter not in answer:
                attemptsLeft -= 1
            else:
                correctLetters += letter

        #Asks user to rematch. Ends game if not, restarts if responded with yes
    rematch = wn.textinput("Game over.", "Would you like to play again? (yes or no)").lower().startswith("y")   
    if not rematch:
        break

wn.exitonclick()