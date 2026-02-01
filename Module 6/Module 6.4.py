def sum(integers):
    result = 0
    for integer in integers:
        result += integer
    return result

integers = []
integer = int(input("Enter an integer:"))
while integer != "":
    integer = int(integer)
    integers.append(integer)
    integer = input("Enter an integer or press Enter to quit:")
result = sum(integers)
print (f"The sum of all number(s) in the list is {result}.")
