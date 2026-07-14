# Write a function to return the square of a number

def square_of_num(n):
    return n * n

result = square_of_num(5)
print(f"The sqaure of a number 5 is {result}")

n = lambda x: x * x

print(f"The sqaure of a number 9 is {n(9)} using lamda")

def check_even(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter num: "))
res = check_even(num)
print(f"The Number is {res}")

a = lambda x: "Even" if x % 2 == 0 else "Odd"

print(f"The number is {a(10)} using lamda")

# value_if_true if condition else value_if_false



