import random
import os
import time
import sys

def get_new_word(): # opens the word file, picks a random number and sets the contents of that line to the selected word
    randNumber = random.randint(0, 99)
    file = open('word_list.txt', 'r')
    words = file.readlines()
    word = words[randNumber]
    return word


def validate(guess, guessedLetters):  # test if it's just a single letter that's not been guessed before
    if len(guess) > 1:
        code = 0
    else:
        guess = guess.lower()
        if guess not in 'abcdefghijklmnopqrstuvwxyz':
            code = 0
        else:
            if guess in guessedLetters:
               code = 1
            else:
                code = guess
    return code  # return a 1 for repeated guess, 0 for invalid entry, the given letter for a valid guess

def print_word(word, guessedLetters): # goes through the word and only prints the character if the player has guessed it
    won = True
    printedWord = ''
    for i in word:
        if i in guessedLetters:
            printedWord = printedWord + i
        else:
            printedWord = printedWord + '*' # if every word of the character can be shown, then the player has won
            won = False
    print(printedWord)
    return won

def main():
    word = get_new_word()
    lives = 7
    guessedLetters = []
    while lives > 0:  # game loop
 
        if print_word(word, guessedLetters): # prints censored word and also checks if game has been won or not
            break
        
        print("Please enter your next guess: ", end='')
        guess = input()
        code = validate(guess, guessedLetters) # tells the user if their guess was valid or not
        if code == 1:
            print("You've already guessed that letter!")
        elif code == 0:
            print("Invalid entry")
        else:
            guessedLetters.append(code)
            if code not in word: # removes a life if the letter isn't in the word
                lives -= 1

        print()
        
    if lives == 0: # win/lose messages depending on what caused the game loop to finish
        print("You lose!")
    else:
        print("Congratulations, you win!")
    time.sleep(3)


if __name__ == "__main__":
    main()
