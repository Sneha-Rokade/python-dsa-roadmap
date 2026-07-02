
# Exercise 1. Arithmetic Product and Conditional Logic

# Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

# Exercise Purpose: Learn basic control flow and the use of if-else statements. Understand how code decisions change output based on a mathematical threshold.

# Given Input:

# Case 1: number1 = 20, number2 = 30
# Case 2: number1 = 40, number2 = 30
# Expected Output:

# The result is 600
# The result is 70

number_1 = int(input("Enter Num 1: "))

number_2 = int(input("Enter Num 2: "))

product = number_1 * number_2
sum = number_1 + number_2

if product <= 1000:
    print("the result is ", product)

else:
    print("the result is ", sum)

print("==============OR=======================")
#--------------------------------------------------

def multply_or_sum(num1, num2):

    products = num1 * num2

    if products <= 1000:
        return products
    else:
        return num1 + num2
    
result = multply_or_sum(20,30)
print("The result is: ", result)

    
result = multply_or_sum(40,30)
print("The result is: ", result)

