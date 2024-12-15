#defining function to adding two numbers
def addition(num1, num2):
    return num1+num2

#defining function to subtract two numbers
def subtraction(num1,num2):
    return num1-num2

#defining function to multiply two numbers
def multiply(num1, num2):
    return num1*num2

#defining function to divide the two numbers
def divide(num1,num2):
    return num1/num2


#displaying all the operations in the calculator
print("welcome to the Inbaa calculator -\n"
      "1. ADDITION\n" \
      "2. SUBTRACTION\n"\
      "3. MULTIPLICATION\n"\
      "4. DIVIDE\n")

#taking input values form the user
number = int(input("Select operations from 1,2,3,4:"))

first_value = int(input("Enter your first value: "))
second_value = int(input("Enter your second value: "))

if number == 1:
    print(first_value,"+",second_value,"=",addition(first_value,second_value))

elif number == 2:
    print(first_value,"-",second_value,"=",subtraction(first_value,second_value))

elif number == 3:
    print(first_value,"*",second_value,"=",multiply(first_value,second_value))

elif number == 4:
    print(first_value,"/",second_value,"=",divide(first_value,second_value))

else:
    print("Please provide input for the opeation")
          
