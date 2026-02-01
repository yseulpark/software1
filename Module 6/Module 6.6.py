import math

diameter1 = float(input("Enter the diameter of the first pizza: "))
diameter2 = float(input("Enter the diameter of the second pizza: "))
price1 = float(input("Enter the price of the first pizza:"))
price2 = float(input("Enter the price of the second pizza:"))

def unit_price(diameter,price):
    radius_meter = diameter / 200
    area = radius_meter **2 * math.pi
    result = price/area
    return result
result1 = unit_price(diameter1, price1)
result2 = unit_price(diameter2, price2)
if result1 < result2 :
    print ("Pizza 1 has better value for money.")
elif result1 > result2 :
    print ("Pizza 2 has better value for money.")
else :
    print("Pizza 1 and pizza 2 have the same value for money.")
