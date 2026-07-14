# def sum_list(a):
#     total = 0
#     for i in a:
#         total += i
#     print(total)

# sum_list([1,2,3,4,5])

# b = [10,20,30,40,50]
# total = 0
# for i in b:
#     total += i

# print(total)

# 4. Factorial (Iteration)

# 👉 Write a function to calculate factorial using loop

def factorial(num):
    fact = 1

    for i in range(1, num+1):
        fact = fact * i
    return fact

print(factorial(5))


# 5. Reverse String

# 👉 Function to reverse a string

str1 = "Hello"

str2 = str1[::-1]
print(str2)


def reverse(str3):

    str1 = str3[::-1]
    return str1

result = reverse("Hello")
print(f"reversing a string hello -> {result}")