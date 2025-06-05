import random
from art import art

print(art)

print("Welcome to the Number Guessing Number!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempt = 10 if choice == "easy" else 5

org = random.randint(1, 101)

while True:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempt -= 1
    if guess < org:
        print("Too low")
    elif guess > org:
        print("Too high")
    else:
        print("You win!")
        break
    if attempt == 0:
        print("You ran out of guesses. You lose!")
        break

    print("Guess again.")
