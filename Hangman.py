#COP3035
#Group Project
#Hangman
#Cody Mitchell, Haley Little, Camron Clark

###Game Mechanics only###
#setup
attemptsLeft = 3
answer = "Word"
uniqueChars = set(answer)
guessedChars = set()
correctChars = set()

#allow multi-letter words w/out user having to guess a space
if ' ' in uniqueChars:
    correctChars.add(' ')

#game loops until either no attempts left, or player has guessed all of the correct chars
while attemptsLeft != 0 and correctChars != guessedChars:
    letter = input("Enter letter here: ")
    #input must be one char, and player must not have guessed it before
    while len(letter) != 1 or letter in guessedChars:
        letter = input("Please try again: ")
    guessedChars.add(letter)
    if letter in uniqueChars:
        correctChars.add(letter)
        #updateBoard(letter)
    else:
        attemptsLeft = attemptsLeft - 1
        #drawNext()
if attemptsLeft == 0:
    print("You lose. Please try again.")
else:
    print("Congrats! You win!")


