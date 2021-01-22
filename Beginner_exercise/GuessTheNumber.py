import random
print("Hello! Welcome to 'Guess the number game'")

number = random.randint(1, 100)
guess = int(input("\nGuess a number between 1 and 100: "))

while guess != number:
    if guess < number:
        print("You need to guess higher. Try again.")
        guess = int(input("\nGuess a number between 1 and 100: "))
    else:
        print("You need to guess lower. Try again!")
        guess = int(input("\nGuess a number between 1 and 100: "))

print("YAY! You guessed the number!")