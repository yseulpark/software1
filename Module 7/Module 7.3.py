airports = {}

while True:
    print ("What action would you like to take?")
    print ("1-Enter a new airport\n2-Fetch the information of an existing airport\n3-Quit")
    user_input = int(input("Enter the number of the action you would like to take: "))
    if user_input == 1:
        new_icao = input("Enter the ICAO code: ")
        new_airport = input("Enter the name of the airport: ")
        airports[new_icao]= new_airport
    elif user_input == 2:
        find_airport = input("Enter the ICAO code of the airport you are looking for: ")
        if find_airport in airports:
            print (f"The airport is {airports[find_airport]}.")
        else:
            print ("Airport not found.")
    elif user_input == 3:
        print ("Program stopped.")
        break
    else:
        print ("Invalid input.")