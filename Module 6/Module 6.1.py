import random
def dice():
    number = random.randint(1,6)
    return number
number = dice()
while number != 6:
    print (number)
    number = dice()
print (number)
