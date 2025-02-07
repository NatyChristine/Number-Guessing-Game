#number guessing game
import random 

result = random.randint(1, 50)

while True:
    guess = int(input("Guess a number from 1 to 50: "))
    if guess == result:
        print(f"CONGRATULATIONS: The number was {result}")
        break
    elif guess < result:
        print("Too low")
    elif guess >= result:
        print("Too high")

