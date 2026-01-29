import random
die = int(input("Number of die to roll: "))
sum = 0

for index in range(die):
    dice = random.randint(1,6)
    sum += dice
print (f"The sum of the numbers is {sum}.")