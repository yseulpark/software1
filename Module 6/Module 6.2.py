import random
def dice(sides):
    number = random.randint(1,sides)
    return number
sides = int(input("Enter the number of sides on the dice: "))
number = dice(sides)

while number != sides:
    print (number)
    number = dice(sides)
print (number)