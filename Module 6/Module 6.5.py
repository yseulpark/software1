def remove_uneven(first_list):
    second_list = []
    for i in first_list:
        if i % 2 == 0:
            second_list.append(i)
    return second_list

first_list = []

while True:
    integer = input("Enter an integer or press Enter to quit:")
    if integer == "":
        break
    integer = int(integer)
    first_list.append(integer)

second_list = remove_uneven(first_list)
print ("Original list:",first_list)
print ("Even numbers only:", second_list)