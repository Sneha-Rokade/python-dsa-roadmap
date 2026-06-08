# MODULES IN PYTHON

## What is a Module?

A module is a Python file that contains:

* Functions
* Variables
* Classes

which can be reused in other Python files.

Example: calculator.py

This file itself is a module.

## Why Use Modules?

Benefits:

* Code Reusability
* Better Organization
* Easier Maintenance
* Reduced Duplication

Large projects use hundreds of modules.

Django itself is made up of many modules.

## Creating Your First Module

Create: math_operations.py

Code:

def add(a, b):

    return a + b


def subtract(a, b):

    return a - b

## Importing a Module

Create: main.py

Code: import math_operations

result = math_operations.add(10, 20)

print(result)

Output: 30

## Import Specific Function

Instead of importing the entire module.

from math_operations import add

print(add(10, 20))

Output: 30

## Import Multiple Functions

from math_operations import add, subtract

print(add(10, 20))

print(subtract(20, 10))

Output: 30
        10

## Import Everything

from math_operations import *

print(add(10, 20))

Note: Not recommended in large projects.

Reason: Harder to understand where functions come from.

## Module Alias

import math_operations as mo

print(mo.add(10, 20))

Output: 30

Alias helps shorten long module names.

## Built-in Modules

Python provides many modules.

Examples:

### math

import math

print(math.sqrt(25))

Output: 5.0

### random

import random

print(random.randint(1, 10))

Output: Random number between 1 and 10

### datetime

import datetime

print(datetime.datetime.now())

Used heavily in backend development.

### os
import os

print(os.getcwd())

Returns current directory.

## Real World Example

Generate Employee ID

employee_utils.py

def generate_employee_id(id):

    return f"EMP{id}"

main.py

from employee_utils import generate_employee_id

print(generate_employee_id(101))

Output: EMP101

## Real World Example

Email Utility Module

email_utils.py

def create_email(name):

    return f"{name.lower()}@company.com"

main.py

from email_utils import create_email

print(create_email("Alex"))

Output: alex@company.com

## **name** Special Variable

Every Python file has: __name__

Example: print(__name__)

When run directly:__main__

## Why Use **main**?

Example:

def add(a, b):

    return a + b


if __name__ == "__main__":

    print(add(10, 20))

This ensures code runs only when the file is executed directly.

Very common interview question.

## Interview Questions

### Q1. What is a Module?

Answer: A Python file containing reusable code.

### Q2. Difference Between Module and Function?

Function: Reusable block of code.

Module: File containing functions, variables, and classes.

### Q4. How Do You Import a Module?

import module_name

### Q5. How Do You Import Specific Functions?

from module_name import function_name

### Q6. What is an Alias?

Answer: Alternative name for a module.

Example: import math as m

### Q7. What is **name**?

Answer: Special variable that identifies how a file is executed.

### Q8. Why Use

if **name** == "**main**"

Answer: To prevent code from running when imported.

## Practice Questions

1. Create a calculator module.
2. Create an employee module.
3. Create an email utility module.
4. Import a specific function.
5. Use module alias.
6. Use math module.
7. Use random module.
8. Use datetime module.
9. Print current working directory using os.
10. Use **name** and **main**.

## Summary

Important Concepts:

* Module
* import
* from import
* Alias
* Built-in Modules
* **name**
* **main**

Common Modules:

* math
* random
* datetime
* os

Used In:

* Django
* FastAPI
* Flask
* Automation
* Data Engineering
* AI/ML
* Cloud Applications

Every large Python project is made up of modules.
