# FUNCTIONS IN PYTHON

## What is a Function?

A function is a reusable block of code that performs a specific task.

Benefits:

* Code Reusability
* Better Readability
* Easier Maintenance
* Reduced Code Duplication

## Function Syntax

def function_name():
    print("Hello")

Calling Function: function_name()

Output: Hello

## Function Without Parameters

def greet():
    print("Welcome to Python")

greet()

Output: Welcome to Python

## Function With Parameters

def greet(name):
    print(f"Hello {name}")

greet("Alex")

Output: Hello Alex

## Multiple Parameters

def introduce(name, age):

    print(f"Name: {name}")

    print(f"Age: {age}")

introduce("Alex", 25)

Output: Name: Alex
        Age: 25

## Return Statement

A function can return data.

def add(a, b):

    return a + b

result = add(10, 20)

print(result)

Output: 30

## Difference Between print() and return

Using print:

def add(a, b):

    print(a + b)

add(10, 20)

Output: 30 

Using return:

def add(a, b):

    return a + b

result = add(10, 20)

print(result)

Output: 30

Return is preferred because the value can be reused later.

## Default Parameters

def greet(name="Alex"):

    print(f"Hello {name}")

greet()

greet("John")

Output:
Hello Alex
Hello John

## Keyword Arguments

def employee(name, role):

    print(name)

    print(role)

employee(role="Engineer", name="Alex")

Output:
Alex
Engineer

## Variable Scope

Local Variable:

def test():

    age = 25

    print(age)

test()

Global Variable:

age = 25

def test():

    print(age)

test()

## Real World Example

Calculate Salary

def calculate_salary(hours, rate):

    return hours * rate

salary = calculate_salary(160, 500)

print(salary)

Output: 80000

## Real World Example

Email Generator

def generate_email(name):

    return f"{name.lower()}@company.com"

print(generate_email("Alex"))

Output: alex@company.com

## Interview Questions

### Q1. Difference Between Parameter and Argument?

Parameter: def greet(name):

Argument: greet("Alex")

### Q4. Difference Between print and return?

print(): Displays output.

return: Sends value back to caller.

### Q5. Can a Function Return Multiple Values?

Yes.

def details():

    return "Alex", 25

name, age = details()

## Practice Questions

1. Create a function to print your name.
2. Create a function to add two numbers.
3. Create a function to find maximum number.
4. Create a function to find minimum number.
5. Create a function to check even or odd.
6. Create a function to calculate salary.
7. Create a function to generate email.
8. Create a function to reverse a string.
9. Create a function to count vowels.
10. Create a function to find square of a number.

## Summary

Important Concepts:

* Function
* Parameters
* Arguments
* Return
* Default Parameters
* Keyword Arguments
* Local Scope
* Global Scope

Functions are the foundation of:

* Django
* FastAPI
* Flask
* Automation Scripts
* Data Engineering
* AI/ML Projects
* Cloud Applications
