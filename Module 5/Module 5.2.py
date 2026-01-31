numbers = []
number = input("Enter a number: ")

while number != "":
    number = int(number)
    numbers.append(number)
    number = input("Enter the next number or press Enter to quit: ")

numbers.sort(reverse=True)
print (numbers[:5])