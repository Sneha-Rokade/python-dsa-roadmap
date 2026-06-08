# DUNDER METHODS IN PYTHON

## What are Dunder Methods?

Dunder means: Double Under

Methods that start and end with double underscores.

Examples:

__init__()

__str__()

__repr__()

__len__()

These are special methods built into Python.

## Why Are Dunder Methods Important?

They allow Python objects to behave like built-in objects.

Examples: print(object)

len(object)

object1 + object2

All use dunder methods internally.

## Common Dunder Methods

__init__()

__str__()

__repr__()

__len__()

__add__()

Most important for interviews:

__init__()

__str__()

# **init**()

Constructor method.
Runs automatically when object is created.

Example:

class Student:

    def __init__(self, name):

        self.name = name

student = Student("Alex")

# **str**()

Controls how an object appears when printed.
Without **str**:

class Student:

    def __init__(self, name):

        self.name = name

student = Student("Alex")

print(student)

Output: <__main__.Student object at 0x12345>
Not useful.

## Using **str**()

class Student:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return self.name


student = Student("Alex")

print(student)

Output: Alex
Much cleaner.

# Real World Example

Employee

class Employee:

    def __init__(self, name, salary):

        self.name = name

        self.salary = salary

    def __str__(self):

        return f"{self.name} - {self.salary}"

employee = Employee(
    "Alex",
    80000
)

print(employee)

Output: Alex - 80000

# **repr**()

Developer-friendly representation.

Example:

class Employee:

    def __repr__(self):

        return "Employee Object"

Usage: employee = Employee()
print(employee)

Output: Employee Object

# **len**()

Allows use of: len(object)

Example:

class Team:

    def __init__(self):

        self.members = [
            "Alex",
            "John",
            "Emma"
        ]

    def __len__(self):

        return len(self.members)

team = Team()
print(len(team))

Output: 3

# **add**()

Allows custom + operator behavior.

Example:

class Number:

    def __init__(self, value):

        self.value = value

    def __add__(self, other):

        return self.value + other.value

num1 = Number(10)

num2 = Number(20)

print(num1 + num2)

Output: 30

# **eq**()

Used for equality comparison.

Example:

class Student:

    def __init__(self, age):

        self.age = age

    def __eq__(self, other):

        return self.age == other.age

Usage:

s1 = Student(25)

s2 = Student(25)

print(s1 == s2)

Output: True

# Built-in Examples

String Length: len("Alex")

Internally: "Alex".__len__()

Addition: 10 + 20

Internally: 10.__add__(20)

Python uses dunder methods everywhere.

# Django Example

Django Models often implement: __str__()

Example:

class User(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):

        return self.name

Admin panel displays user names instead of object addresses.
Very common interview question.

# Advantages of Dunder Methods

* Better Object Representation
* Custom Operators
* Cleaner Code
* Integration with Python Features

# Interview Questions

### Q1. What is **init**()?

Answer: Constructor method.

### Q2. What is **str**()?

Answer: Controls object representation when printed.

### Q3. Why Use **str**()?

Answer: To provide meaningful object output.

### Q4. What is **len**()?

Answer: Allows use of len() on custom objects.

### Q5. What is **add**()?

Answer: Allows custom + operator behavior.

### Q6. What is **eq**()?

Answer: Controls equality comparison.

### Q7. Where is **str**() Used in Django?

Answer: Model representation in Django Admin.

### Q8. Why Are Dunder Methods Important?

Answer: They allow custom classes to integrate with Python's built-in functionality.

# Practice Questions

1. Create Student class with **str**().
2. Create Employee class with **str**().
3. Create Team class with **len**().
4. Create Number class with **add**().
5. Create Student class with **eq**().
6. Print custom objects.
7. Override **repr**().
8. Build Product class with **str**().
9. Create Cart class with **len**().
10. Create custom comparison logic.

# Summary

Important Dunder Methods:

* **init**()
* **str**()
* **repr**()
* **len**()
* **add**()
* **eq**()

Used In:

* Django Models
* Enterprise Applications
* APIs
* Custom Libraries

Dunder methods make Python classes behave like built-in Python objects.
