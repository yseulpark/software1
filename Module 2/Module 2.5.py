talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

talent_to_pound = talents * 20
talent_to_lot = talent_to_pound * 32
talent_to_gram = talent_to_lot * 13.3

pound_to_lot = pounds * 32
pound_to_gram = pound_to_lot * 13.3

lot_to_gram = lots * 13.3

total_gram = talent_to_gram + pound_to_gram + lot_to_gram
total_kilograms = total_gram // 1000
grams_left = total_gram % 1000

print("The weight in modern units:")
print(f"{total_kilograms} kilograms and {grams_left} grams.")
