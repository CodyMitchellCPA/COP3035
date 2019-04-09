#COP3035
#Group Project
#Hangman
#Cody Mitchell, Haley Little, Camron Clark

###Game Mechanics only###
#setup
attemptsLeft = 3




answer = "Word my dude"
uniqueChars = set(answer.lower())
guessedChars = set()
correctChars = set()
currentWord = ""
#currentWord
for i in range(0, len(answer)):
    if answer[i] == ' ':
        currentWord = currentWord + ' '
    else:
        currentWord = currentWord + '$'


#allow multi-letter words w/out user having to guess a space
if ' ' in uniqueChars:
    correctChars.add(' ')
print("Attempts left: " + str(attemptsLeft))
print("Current word: " + currentWord)

#game loops until either no attempts left, or player has guessed all of the correct chars
while attemptsLeft != 0 and correctChars != uniqueChars:
    letter = input("Enter letter here: ").lower()
    #input must be one char, and player must not have guessed it before
    while len(letter) != 1:
        letter = input("Please enter only one letter: ").lower()
    while letter in guessedChars:
        letter = input("You've already guessed that letter. Please try again: ").lower()
    guessedChars.add(letter)
    if letter in uniqueChars:
        correctChars.add(letter)
        #updateBoard(letter)
    else:
        attemptsLeft = attemptsLeft - 1
    print("Attempts left: " + str(attemptsLeft))
    print("Current word: " + currentWord)
        #drawNext()
if attemptsLeft == 0:
    print("You lose. Please try again.")
else:
    print("Congrats! You win!")

   
