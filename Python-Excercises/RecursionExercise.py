
def factorial(n):

    if n==1:
        return 1
    else:
        return n * factorial(n-1)
    
a = int(input("Enter number: "))

result = factorial(a)
print(f"The factorial number of  is {result}")