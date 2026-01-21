gender = input("Enter your biological gender: ")
hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))

if gender == "female":
    if 117 < hemoglobin_value < 155:
        print ("Normal hemoglobin value")
    elif hemoglobin_value >= 155 :
        print ("High hemoglobin value")
    elif hemoglobin_value <= 117 :
        print ("Low hemoglobin value")

if gender == "male":
    if 134 < hemoglobin_value < 167:
        print ("Normal hemoglobin value")
    elif hemoglobin_value >= 167 :
        print ("High hemoglobin value")
    elif hemoglobin_value <= 134 :
        print ("Low hemoglobin value")