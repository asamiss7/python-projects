import random
import string

def letters():
    random_str =  ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    return random_str

def integer():
    return int(random.random()*10000)

email = [letters() + str(integer()) + "@gmail.com" for i in range(1000)]

print(email)

# To store in csv file
with open("email2.csv","w") as file:
    file.write("Email \n")

    for i in email:
     file.write(i + "\n")