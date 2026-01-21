gender = input("Enter your biological gender: ")
hemoglobin_value = float(input("Enter your hemoglobin value: "))

if gender == "female" and 117 < hemoglobin_value < 155 :
    print ("Normal hemoglobin value")
elif gender == "female" and hemoglobin_value >= 155 :
    print ("High hemoglobin value")
elif gender == "female" and hemoglobin_value <= 117 :
    print ("Low hemoglobin value")

if gender == "male" and 134 < hemoglobin_value < 167 :
    print ("Normal hemoglobin value")
elif gender == "male" and hemoglobin_value >= 167 :
    print("High hemoglobin value")
elif gender == "male" and hemoglobin_value <= 134:
    print("Low hemoglobin value")