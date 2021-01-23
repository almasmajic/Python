import random
print("Hello! Welcome to 'Guess the number game'")
number = random.randint(1, 100)

for i in range(3):
    guess = int(input('\nTake a guess: '))
    if i < 2 and guess != number:
        if number < guess:
            print('Your number should be lower')
        elif number > guess:
            print('Your number should be higher')
    elif guess == number:
        print("That's correct!")
        break
    else:
        print(f'Sorry, you lost. The number was {number}')
        break