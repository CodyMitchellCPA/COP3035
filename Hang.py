# COP 3035 
# Final Project - Hangman
# Cody Mitchell, Haley Little, Camron Clark


### STILL NEED:
### 	1 or 2 player option - which will then either use a random word or ask the player 2 to input the secret word.


from __future__ import print_function		# use Python3 printing
import random					# select random word from list

### DEFINITIONS ###
def drawBoard(attemptsLeft, missedChars, correctChars, answer):
	print()

	# print remaining attempts
	print("Attempts Remaining: " + str(attemptsLeft))

	# print list of missed letters separated by a space
	print("Missed letters: ", end=' ')
	for letter in missedChars:
 		print(letter, end=' ')
	print()

	# print placeholders for letters and spaces in answer
	placeholder = ''
	for i in range(0, len(answer)):
		if answer[i] == ' ':
			placeholder = placeholder + ' '
		else:
			placeholder = placeholder + '_'


	# update current word ( _ to letter)
	for i in range(len(answer)):
		if answer[i] in correctChars:
			placeholder = placeholder[:i] + answer[i] + placeholder[i+1:]

	# print answers as they're guessed
	for letter in placeholder: 
		print(letter, end=' ')
	print()
	print()

def getInput(used):
	while True:
		letter = input("Enter a letter: ").lower()

		# can only guess each letter once
		if letter in used:
			print("OOPS! You already guessed that letter, try again.\n")

		# can only enter one letter at a time
		elif len(letter) != 1:
			print("OOPS! Only one letter at a time, try again.\n")
		
		# must be a letter in the alphabet
		elif letter not in 'abcdefghijklmnopqrstuvwxyz':
			print("OOPS! You must enter a letter in the alphabet, try again.\n")

		# if correct input then return the letter
		else:
			return letter

def randomWord(words):
	# selects a random word from the list
	selection = random.randint(0, len(words) - 1)
	return words[selection]

def rematch():
	# Asks player at end of the game if they would like to play again.
	print("Rematch? (yes/no)")

	# returns True if yes, returns False if no
	return input().lower().startswith("y")
### ###


### VARIABLES ###
words = 'ash, apple, airplane, amazing, bee sting, bird, baby, birthday cake, bubble, bananas, cat, cow goes moo, chocolate, chicken, cup, dog, diamond, doorbell, door, doll, egg, elephant, easy, ear ache, flying fish, fuzy, fruit, funny, frog, goat, gingerbread man, garden, green bean, greatful, high, hot, hello, happy, horse, ice, ice cream, itch, jolly, jingle, junk, kitchen, knife, kangaroo, leg, library, lion, light beam, leopard, map, milk, milkshake, money, platypus, pants, parachute, pepper, puppy, queen, rainbow, rocket, roof, salt and pepper, school, sandwich, shoes, snail, spaceship, sports, star, swimming, teeth, tennis, tiger, train, triangle, umbrella, vulture, vacuum, wax, water, web, worm, x ray'.split(', ')

print("WELCOME TO ~ H A N G M A N ~")
attemptsLeft = 10
missedChars = ""
correctChars = ""
answer = randomWord(words).lower()
gameOver = False
### ###


### GAME MECHANICS ###
while True:
	# allow multi word answer - ignore spaces and display the space
	if ' ' in answer:
		correctChars = correctChars + ' '

	# setup the game
	drawBoard(attemptsLeft, missedChars, correctChars, answer)

	# obtain the users input
	letter = getInput(missedChars + correctChars)
	

	# if letter is in answer, add it to the correctChars list
	if letter in answer:
		correctChars = correctChars + letter

		# verify if game is or is not over
		foundWord = True

		# if user has not found all the letters, the game continues
		for i in range(len(answer)):
			if answer[i] not in correctChars:
				foundWord = False
				break

		#alternatively, can just test to length of answer w/ length of correctChars
		#foundWord = False
		# if len(correctChars) == len(answer):
		# 	print("YOU WIN!\nThe answer was " + answer + "!\n")
		# 	gameOver = True

		# if user has found all the letters, the game is over
		if foundWord:
			print("YOU WIN!\nThe answer was " + answer + "!\n")
			gameOver = True

	# if letter is not in answer, add it to the missedChars list and remove an attempt
	else:
		missedChars = missedChars + letter
		attemptsLeft = attemptsLeft - 1

		# if user has no attempts left, the game is over
		if attemptsLeft == 0:
			drawBoard(attemptsLeft, missedChars, correctChars, answer)
			print("GAME OVER!\nYou ran out of attempts! The answer was " + answer + "!")
			print()
			gameOver = True

	# If game is over, give user the option for a rematch and reset all values
	if gameOver:
		if rematch():
			missedChars = ''
			correctChars = ''
			gameOver = False
			answer = randomWord(words).lower()

		else:
			break
### ###
