#COP3035
#Group Project
#Hangman
#Cody Mitchell, Haley Little, Camron Clark

###Game Mechanics only###
#setup

attemptsLeft = 3

answer = "Word my dude"
uniqueChars = set(answer.lower())
guessedChars = set() #stores every char that user guesses
correctChars = set() #stores correctly guessed user inputs
currentWord = "" #stores all _ (and spaces), then updates as user enters correct chars
for i in range(0, len(answer)):
    if answer[i] == ' ':
        currentWord = currentWord + ' '
    else:
        currentWord = currentWord + '_'


#allow multi-letter words w/out user having to guess a space
if ' ' in uniqueChars:
    correctChars.add(' ')


#game loops until either no attempts left, or player has guessed all of the correct chars
while attemptsLeft != 0 and correctChars != uniqueChars:
    #print basic info before each turn
    print("Attempts left: " + str(attemptsLeft))
    print("Current word: " + currentWord)
    letter = input("Enter letter here: ")
    #input must be one char, and player must not have guessed it before
    #must be alphanumeric ###has not been implemented yet
    while len(letter) != 1:
        letter = input("Please enter only one letter: ")
    letter = letter.lower()
    while letter not in 'abcdefghijklmnopqrstuvwxyz':
        letter = input("Letter must be in alphabet: ").lower()
    while letter in guessedChars:
        letter = input("You've already guessed that letter. Please try again: ")
    #change letter to non-case sensitve
    letter = letter.lower()
    guessedChars.add(letter)
    if letter in uniqueChars:
        #add letter to correctChars set
        correctChars.add(letter)
        #update currentWord ( from _ -> to letter)
        for i in range (0, len(answer)):
            if answer[i].lower() == letter:
                currentWord = currentWord[:i] + answer[i] + currentWord[i+1:]
    else:
        attemptsLeft = attemptsLeft - 1
    
#end game prints
print("Current word: " + currentWord)
if attemptsLeft == 0:
    print("You lose. Please try again.")
else:
    print("Congrats! You win!")

   
