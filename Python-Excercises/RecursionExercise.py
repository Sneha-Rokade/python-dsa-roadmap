
def factorial(n):

    if n==1:
        return 1
    else:
        return n * factorial(n-1)
    
a = int(input("Enter number: "))

result = factorial(a)
print(f"The factorial number of  is {result}")

# To calculate the factorial using recursion, I define a function `factorial(n)` where the function calls itself with a smaller value of `n`.

# First, I define a **base case**, which is `if n == 1: return 1`. This is important because it stops the recursion. Without this condition, the function would keep calling itself infinitely and cause a stack overflow.

# Then, I define the **recursive case** as `return n * factorial(n - 1)`. This means the function keeps reducing the problem into smaller subproblems until it reaches the base case.

# For example, if I call `factorial(5)`, it works like:
# factorial(5) = 5 × factorial(4)
# factorial(4) = 4 × factorial(3)
# factorial(3) = 3 × factorial(2)
# factorial(2) = 2 × factorial(1)

# Once it reaches `factorial(1)`, it returns 1, and then all previous calls get resolved step by step:
# 2 × 1 = 2
# 3 × 2 = 6
# 4 × 6 = 24
# 5 × 24 = 120

# So the final result is 120.

# In summary, recursion works by breaking a problem into smaller subproblems, solving the smallest one, and then building the result back up.
