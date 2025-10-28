import random

#Variables
gameTitle = "Word Raider"
listOfWords = []

#File handling
with open('words.txt', 'r') as file:
    contents = file.read()
    listOfWords = contents.splitlines()

#Random word
randomWord = random.choice(listOfWords)

#Game
lettersGuessed = set()
lettersNotInTheWord = set()
maxTurns = 5
turnCounter = 0

print("Welcome to:", gameTitle, " A game about guessing a word!")
print("You have to guess a 5 letter word. You have 5 turns")

while(turnCounter < maxTurns):
    guess = input("Write er guess and press Enter: ")

    if(len(guess) != 5 or not guess.isalpha()):
        print("Word has to be letters and 5 characters")
        continue

    guess.lower()

    for i in range(len(guess)):
        if guess[i] in randomWord:
            lettersGuessed.add(guess[i])
        else:
            lettersNotInTheWord.add(guess[i])
    
    print("In the word:", lettersGuessed)
    print("Not in the word:", lettersNotInTheWord)

    turnCounter += 1
