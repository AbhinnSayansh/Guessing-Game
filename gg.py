import random

num = random.randint(1, 100)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 100: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    elif guess>num:
        print(f"nope, {guess} is higher , go lower ")
    elif guess<num:
        print(f"nope, {guess} is  lower , go higher")
