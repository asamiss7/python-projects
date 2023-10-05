import random

def generate():
 return int(random.random()*100000000)

phone = ['98' + str(generate()) for i in range(10000)]

print(phone)

# To store in csv file
with open("phone_number2.csv", "w") as file:
    file.write("Phone \n")
    
    for i in phone:
        file.write(i+"\n")