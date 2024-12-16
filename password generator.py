#importing random from the python library
import random

#importing string from the python library
import string

#defining function with the name of generating_password
def generating_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

#checking condition if the length is lesser than it display as a none
    if length<8:
        print("Password length should be at least 8 characters.")
        return None

    Higher_password = ''.join(random.choice(characters) for i in range(length))
    return Higher_password

#receiving input from the user
length=int(input("Enter the length of password: "))
print("Generating password for the user: ",generating_password(length))                        
