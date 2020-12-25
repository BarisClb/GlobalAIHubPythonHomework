import random
import sys

# Welcome Code

user_name = input("Please enter your name: ")
user_play = input(f"Hello {user_name}, would you like to play the Hangman Game? ")
possible_answers = ["YES", "Yes", "yes", "Y", "y"]

if user_play in possible_answers:
    print("Let's play the Hangman Game!")
else:
    sys.exit("Maybe another time then!") 

# The Game

# Variables

answers = ["Python", "Computer", "Program"]
answer = random.choice(answers)
guessed_letters = ""
found_letters = 0
letter_tries = 10
word_tries = 3
winner = False

# Letter Guesses

print(f"You have {letter_tries} tries to guess the letters. If you guess it right, it won't affect the remaining number of tries.")

while letter_tries > 0:
    if found_letters == len(answer):
        print(f"You found all the letters! The answer was {answer}!")
        letter_tries = 0
        winner = True
        break
    guessed_letter = input("Guess a letter: ")
    guessed_letters += guessed_letter
    print(f"{letter_tries} tries left.")
    if len(guessed_letter) > 1:
        print("No cheating! You can only guess one letter.")
        letter_tries -= 1
        print(f"{letter_tries} tries left.")
    else:
        if guessed_letter.lower() in answer.lower():
            print("You found a letter!")
            found_letters += 1
        else:
            print("Wrong guess.")
            letter_tries -= 1
            guessed_letter.lower() in answer.lower()
        for letter in answer:
            if letter.lower() in guessed_letters.lower():
                print(letter)
            else:
                print("_")
        print(f"{letter_tries} tries left.")

# Word Guesses

if winner == False:
    print(f"You are out of letter tries. Now, try to guess the word! You have {word_tries} tries left.")

while word_tries > 0 and winner == False:
    if answer.lower() == input("What's your guess? ").lower():
        print(f"You guessed it right! The answer was {answer}!")
        word_tries = 0
        winner = True
    else:
        print(f"You guessed it wrong.")
        word_tries -= 1
        print(f"{word_tries} tries left.")

# End of the Game

if winner == True:
    print("Congratulations, you won!")
elif winner == False:
    print("You lost. Better luck next time!")