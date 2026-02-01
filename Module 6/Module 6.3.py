def gasoline(gallons):
    liter = gallons * 3.78541178
    return liter
gallons = float(input("Enter the volume of gasoline in American gallons: "))
while gallons >= 0:
    liter = gasoline(gallons)
    print (liter)
    gallons = float(input("Enter the volume of gasoline in American gallons: "))
