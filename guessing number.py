from random import randrange
guesses = 4
guess = ""
number = randrange(1, 20)
guess_count = 0
guess_limit = 3
out_of_guess = False

name = input("Hello! what is your name?\n")
print("Well, " + name + ", i am thinking a number between 1 to 20.")
guess = int(input("Take a guess.\n"))

while guess != guesses and not(out_of_guess):
    if guess > guesses:
        print("your guess is too high.")
        guess = int(input("Take a guess.\n"))
        guess_count +=1
    elif guess < guesses:
        print("you guess is too low")
        guess = int(input("Take a guess.\n"))
        out_of_guess = True

if out_of_guess:
    print("sorry,you lose!")
else:
    print("Good job, Albert! you guess my number in 3 guesses")
