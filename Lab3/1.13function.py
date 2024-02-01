"""Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20.
This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""
import random
guess_times = 1

name = str(input("Hello! What is your name?\n"))
k = int(input(f"Let's play \"Guess the number\"\n{name}, choose a range of numbers from 1 to k (k must be big for more fun)\nPlease, enter positive integer k = "))

print(f"Well, {name}, I am thinking of a number between 1 and {k}.")

num = random.randint(1, k)  

guess = int(input("Take a guess.\n"))

found = bool(num != guess) 
while found: 
    if guess < num:
        guess_times += 1
        guess = int(input("Your guess is too low.\nTake a guess.\n"))
    elif guess > num:
        guess_times += 1
        guess = int(input("Your guess is too high.\nTake a guess.\n"))
    else:
        break

print(f"Good job, {name}! You guessed my number in {guess_times} guesses!")
