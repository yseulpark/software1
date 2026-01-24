import random
random_number = random.randint (1,10)
guess = int(input("Guess the number:"))
while guess != random_number :
    if guess < random_number:
        print("Too low")
    elif guess > random_number:
        print("Too high")
    guess = int(input("Guess the number:"))
print ("Correct!")