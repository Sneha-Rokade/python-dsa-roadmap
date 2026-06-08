# DECORATORS IN PYTHON

## What is a Decorator?

A decorator is a function that modifies or extends the behavior of another function without changing its original code.

Simple definition:

Decorator = Function that wraps another function

## Why Use Decorators?

Without decorators:

def login():

    print("User Logged In")

Suppose we want:

* Logging
* Authentication
* Timing
* Validation

We would need to modify the original function repeatedly.

Decorators solve this problem.

## Functions are First-Class Objects

In Python:

Functions can be:

* Assigned to variables
* Passed as arguments
* Returned from functions

Example:
def greet():

    print("Hello")


say_hello = greet

say_hello()

Output: Hello

## Function Inside Function

Example:
def outer():

    def inner():

        print("Inside Inner Function")

    inner()


outer()

Output: Inside Inner Function

## Returning Functions

Example:

def outer():

    def inner():

        print("Hello")

    return inner


greet = outer()

greet()

Output: Hello

Decorator concept is based on this.

# First Decorator

Example:

def decorator(func):

    def wrapper():

        print("Before Function")

        func()

        print("After Function")

    return wrapper

Function:

def greet():

    print("Hello")

Apply decorator:

greet = decorator(greet)

greet()

Output:

Before Function

Hello

After Function

# Using @ Syntax

Instead of: greet = decorator(greet)

Use:

@decorator
def greet():

    print("Hello")

Much cleaner.

## Example

def decorator(func):

    def wrapper():

        print("Starting Function")

        func()

        print("Ending Function")

    return wrapper

@decorator
def greet():

    print("Hello")

Usage: greet()

Output:
Starting Function
Hello
Ending Function

# Decorator with Arguments

Normal decorator:

def decorator(func):

    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper

Why?

Because functions may accept parameters.

## Example

def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper

Function:

@decorator
def add(a, b):

    return a + b

Usage: print(add(10, 20))

Output:

Before
After
30

# Real World Example

Logging

def logger(func):

    def wrapper(*args, **kwargs):

        print(f"Calling {func.__name__}")

        return func(*args, **kwargs)

    return wrapper

Usage:

@logger
def login():

    print("User Logged In")


login()

Output:

Calling login
User Logged In

# Authentication Example

def authenticate(func):

    def wrapper():

        print("Checking Authentication")

        func()

    return wrapper

Usage:

@authenticate
def dashboard():

    print("Dashboard Opened")

Output:

Checking Authentication
Dashboard Opened

# Execution Time Decorator

import time

def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(

            f"Execution Time: {end - start}"

        )

        return result

    return wrapper

Usage:

@timer
def calculate():

    total = sum(range(1000000))

    return total


calculate()

# Multiple Decorators

Example:

@decorator1
@decorator2
def greet():

    print("Hello")

Execution:

decorator1
    decorator2
        greet()

Order matters.

# Built-in Decorators

You already know:

@property
@staticmethod
@classmethod

These are decorators.

# Real World Django Example

Login Required

@login_required
def dashboard(request):

    pass

Only authenticated users can access.

# Django REST Framework Example

@api_view(["GET"])
def get_users(request):

    pass

Decorator modifies view behavior.

# Why Use functools.wraps?

Problem: print(function.__name__)

may show: wrapper

instead of actual function name.

Solution: from functools import wraps

Example: from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper

Best practice.

# Advantages of Decorators

* Reusable Logic
* Cleaner Code
* Less Duplication
* Better Separation of Concerns

# Interview Questions

### Q1. What is a Decorator?

Answer: A function that modifies another function without changing its source code.

### Q2. Why Use Decorators?

Answer: To add reusable functionality like logging, authentication, validation, etc.

### Q3. What Symbol Applies a Decorator?

Answer: @

### Q4. Why Use *args and **kwargs?

Answer: To support functions with any number of arguments.

### Q5. Are @property and @staticmethod Decorators?

Answer: Yes.

### Q6. What is a Wrapper Function?

Answer: The inner function that executes before/after the original function.

### Q7. Can Multiple Decorators Be Used?

Answer: Yes.

### Q8. What is functools.wraps?

Answer: A helper that preserves original function metadata.

### Q9. Where Are Decorators Used?

Answer:
* Django
* Flask
* FastAPI
* Authentication
* Logging

### Q10. Why Are Decorators Important?

Answer: They make code reusable and maintainable.

# Practice Questions

1. Create logging decorator.
2. Create authentication decorator.
3. Create timer decorator.
4. Create validation decorator.
5. Create greeting decorator.
6. Use decorator with arguments.
7. Use multiple decorators.
8. Use functools.wraps.
9. Create API access decorator.
10. Build mini login system using decorators.

# Summary

Important Concepts:

* Decorators
* Wrapper Functions
* @ Syntax
* *args
* **kwargs
* functools.wraps

Common Built-in Decorators:

* @property
* @staticmethod
* @classmethod

Used In:

* Django
* Flask
* FastAPI
* APIs
* Authentication Systems
* Logging Systems

Decorators are one of Python's most powerful features and are heavily used in modern backend frameworks.
