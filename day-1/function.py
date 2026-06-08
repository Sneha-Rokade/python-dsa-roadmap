"""
================================================
FUNCTIONS IN PYTHON
================================================

What is a Function?

A function is a reusable block of code
that performs a specific task.

Why Functions?

1. Code Reusability
2. Better Organization
3. Easy Maintenance
4. Reduces Repetition

Without Function:

print("Welcome Alex")
print("Welcome Alex")
print("Welcome Alex")

Same code repeated multiple times.

================================================
1. CREATING A FUNCTION
================================================
"""

def greet():
    print("Welcome Alex")

greet()

"""
Output:
Welcome Alex
"""

# ------------------------------------------------

"""
Function Definition:

def greet():
    print("Welcome Alex")

Function Call:

greet()

Function will execute only when called.
"""

# ------------------------------------------------

"""
================================================
2. FUNCTION WITH PARAMETERS
================================================

Parameters are values received by a function.
"""

def greet(name):
    print(f"Welcome {name}")

greet("Alex")

"""
Output:
Welcome Alex
"""

# ------------------------------------------------

"""
Multiple Parameters
"""

def employee(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

employee("Alex", 25)

"""
Output:
Name: Alex
Age: 25
"""

# ------------------------------------------------

"""
================================================
3. FUNCTION WITH RETURN VALUE
================================================

return sends data back to the caller.
"""

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

"""
Output:
30
"""

# ------------------------------------------------

"""
Difference:

print() -> displays output

return -> sends value back
"""

# ------------------------------------------------

"""
================================================
4. FIND SQUARE OF NUMBER
================================================
"""

def square(num):
    return num * num

print(square(5))

"""
Output:
25
"""

# ------------------------------------------------

"""
================================================
5. FIND MAXIMUM OF TWO NUMBERS
================================================
"""

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(100, 200))

"""
Output:
200
"""

# ------------------------------------------------

"""
================================================
6. CHECK EVEN OR ODD
================================================
"""

def check_even(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(20))

"""
Output:
Even
"""

# ------------------------------------------------

"""
================================================
7. DEFAULT PARAMETERS
================================================

Default value is used if no value
is passed during function call.
"""

def greet(name="Alex"):
    print(f"Welcome {name}")

greet()

"""
Output:
Welcome Alex
"""

# ------------------------------------------------

greet("John")

"""
Output:
Welcome John
"""

# ------------------------------------------------

"""
================================================
8. KEYWORD ARGUMENTS
================================================
"""

def employee(name, age):
    print(name)
    print(age)

employee(age=25, name="Alex")

"""
Output:
Alex
25
"""

# ------------------------------------------------

"""
================================================
9. LOCAL VARIABLES
================================================

Variables created inside a function
exist only inside that function.
"""

def test():
    age = 25
    print(age)

test()

"""
Output:
25
"""

# print(age)

"""
Error

age exists only inside function.
"""

# ------------------------------------------------

"""
================================================
10. GLOBAL VARIABLES
================================================
"""

company = "Google"

def show_company():
    print(company)

show_company()

"""
Output:
Google
"""

# ------------------------------------------------

"""
================================================
11. REAL WORLD EXAMPLE
================================================

Calculate Salary Bonus
"""

def calculate_bonus(salary):

    bonus = salary * 0.10

    return bonus

print(calculate_bonus(100000))

"""
Output:
10000.0
"""

# ------------------------------------------------

"""
================================================
12. REAL WORLD EXAMPLE
================================================

Login Validation
"""

def login(username, password):

    if username == "admin" and password == "1234":
        return "Login Successful"

    return "Invalid Credentials"

print(login("admin", "1234"))

"""
Output:
Login Successful
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is a Function?

Answer:

A function is a reusable block of code
that performs a specific task.

------------------------------------------------

Q2. Why do we use Functions?

Answer:

1. Reusability
2. Better Code Organization
3. Easy Maintenance
4. Reduces Code Duplication

------------------------------------------------

Q3. What is the syntax of a Function?

Answer:

def function_name():
    statements

------------------------------------------------

Q4. What is a Parameter?

Answer:

A parameter is a variable defined in
the function definition.

Example:

def greet(name):
    print(name)

'name' is parameter.

------------------------------------------------

Q5. What is an Argument?

Answer:

Value passed during function call.

Example:

greet("Alex")

"Alex" is argument.

------------------------------------------------

Q6. Difference between Parameter and Argument?

Parameter:

def greet(name)

Argument:

greet("Alex")

------------------------------------------------

Q7. What is return?

Answer:

return sends a value back to the caller.

Example:

def add(a,b):
    return a+b

------------------------------------------------

Q8. Difference between return and print?

print:
Displays output.

return:
Sends value back for further use.

------------------------------------------------

Q9. What is a Local Variable?

Answer:

Variable created inside a function.

Accessible only within that function.

------------------------------------------------

Q10. What is a Global Variable?

Answer:

Variable declared outside a function.

Accessible throughout the program.
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Create a function to print your name.

2. Create a function to add two numbers.

3. Create a function to subtract two numbers.

4. Create a function to multiply two numbers.

5. Create a function to find maximum number.

6. Create a function to find minimum number.

7. Create a function to check even or odd.

8. Create a function to calculate area
   of a rectangle.

9. Create a function to count vowels
   in a string.

10. Create a function to reverse a string.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Concepts:

1. Function Definition
2. Function Call
3. Parameters
4. Arguments
5. Return Statement
6. Default Parameters
7. Keyword Arguments
8. Local Variables
9. Global Variables

Functions are heavily used in:

Backend Development
APIs
Automation
Data Engineering
Machine Learning
Cloud Applications
Microservices
"""