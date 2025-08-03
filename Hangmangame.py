# Hangman Game

# Import Library
import random

# List of 5 predefined words
words = ["html", "cake", "apple", "march", "sunflower", "blue"]

# Randomly choose a word
word = random.choice(words)

# No. of wrong guessess allowed
max_guesses = 6
guesses = 0

print("Welcome to Hangman Game!")
print("The word has", len(word), "letters.")

# Creating categories for the predefined words
if word == "html":
    print("Category: PROGRAMMING LANGUAGE")
if word == "cake":
    print("Category: BAKERY ITEM ")
if word == "apple":
    print("Category: FRUIT ")
if word == "march":
    print("Category: MONTH ")
if word == "sunflower":
    print("Category FLOWERS ")
if word == "blue":
    print("Category COLOUR ")

while guesses < max_guesses:
    choice = input("Enter your guess: ").lower()
    if choice == word:
        print("You guessed correctly!")
        break
    else:
        guesses += 1
        print("You guessed wrong,Try again.")
        print("You have", int(max_guesses - guesses), "guesses left.")

if guesses == max_guesses:
    print("You have lost. All 6 guesses used.")
    print("The word was", word)

# End of Hangman game
