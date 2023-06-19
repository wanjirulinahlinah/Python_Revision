# Write a program to add two numbers entered by the user and display the sum.

def add_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is", sum)
add_numbers()

# Write a program to calculate the product of two numbers entered by the user.

def multiply_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    product = num1 * num2
    print("The product of", num1, "and", num2, "is", product)
multiply_numbers()

# Write a program to calculate the average of three numbers entered by the user.

def average_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    average = num1 + num2 + num3
    print("The average of", num1, "and", num2,  "and", num3, "is", average)
average_numbers()

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")

