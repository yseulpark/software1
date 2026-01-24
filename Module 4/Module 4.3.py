number = str(input("Enter the number:"))
max = min = float(number)
while number != "":
    number = float(number)
    if number > max:
        max = number
    elif number < min:
        min = number
    number = str(input("Enter the number:"))
print (f"The largest number is {max} and the smallest number is {min}.")