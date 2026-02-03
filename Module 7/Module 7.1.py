seasons = ("Spring","Summer","Autumn","Winter")
print ("1-January\n2-February\n3-March\n4-April\n5-May\n6-June\n7-July\n8-August\n9-September\n10-October\n11-November\n12-December")
user_input = int(input("Choose a month by entering the corresponding number:"))

if user_input == 12 or user_input == 1 or user_input == 2:
    print (f"Month number {user_input} is in {seasons[3]}.")
elif user_input == 3 or user_input == 4 or user_input == 5:
    print (f"Month number {user_input} is in {seasons[0]}.")
elif user_input == 6 or user_input == 7 or user_input == 8:
    print (f"Month number {user_input} is in {seasons[1]}.")
elif user_input == 9 or user_input == 10 or user_input == 11:
    print (f"Month number {user_input} is in {seasons[2]}.")
else :
    print ("Invalid input.")