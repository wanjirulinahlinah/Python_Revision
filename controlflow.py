# Write a Python program that prints the numbers from 1 to 10 using a for loop.
def print_numbers():
    for num in range(1, 11):
        print(num)

print_numbers()
        


# Write a Python program that calculates the sum of all numbers from 1 to 100 using a for loop
def calculate_sum():
    sum=0
    for num in range(1,101):
        sum+=num
    return sum
    
result = calculate_sum()
print("The sum of numbers from 1 to 100 is:", result)