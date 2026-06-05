# STATIC METHODS IN PYTHON

## What is a Static Method?

A static method is a method that belongs to a class but does not operate on:

* Object Data (self)
* Class Data (cls)

It behaves like a normal function placed inside a class for better organization.

## Why Use Static Methods?

Sometimes a function is related to a class but does not need: self or cls

Example: A calculator utility.

add()
subtract()
multiply()

No object data required.
No class data required.

## Creating a Static Method

Use: @staticmethod

Example:

class MathUtils:

    @staticmethod
    def add(a, b):

        return a + b

Usage:

print(MathUtils.add(10, 20))

Output: 30

## No self Parameter

Normal Method: def show(self):

Class Method: def show(cls):


Static Method: def show():
No self.
No cls.

## Example 1

class Calculator:

    @staticmethod
    def multiply(a, b):

        return a * b

Usage:

print(Calculator.multiply(5, 4))

Output: 20

## Example 2

class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):

        return (celsius * 9/5) + 32

Usage:

print(Temperature.celsius_to_fahrenheit(25))

Output: 77.0

## Calling Through Object

Static methods can also be called using objects.

class MathUtils:

    @staticmethod
    def add(a, b):

        return a + b

Usage: math = MathUtils()

print(math.add(10, 20))

Output: 30

But calling through class is preferred.

## Real World Example

Email Validator

class Validator:

    @staticmethod
    def is_valid_email(email):

        return "@" in email

Usage:

print(
    Validator.is_valid_email(

        "alex@gmail.com"
    )
)

Output: True

## Real World Example

Password Validator

class PasswordValidator:

    @staticmethod
    def is_valid(password):

        return len(password) >= 8

Usage:

print(
    PasswordValidator.is_valid(
        "python123"
    )
)

Output: True

## Real World Example

Bank Utility

class BankUtils:

    @staticmethod
    def calculate_interest(
        principal,
        rate,
        years
    ):
        return principal * rate * years / 100

Usage:

interest = BankUtils.calculate_interest(
    100000,
    10,
    2
)

print(interest)

Output: 20000.0

## Difference Between Method Types

### Instance Method

def method(self):

Uses: Object Data

### Class Method

@classmethod

def method(cls):

Uses: Class Data

### Static Method

@staticmethod
def method():

Uses: Neither Object Nor Class Data

## Comparison Example

class Employee:

    company = "Google"

    def instance_method(self):

        print("Instance Method")

    @classmethod
    def class_method(cls):

        print(cls.company)

    @staticmethod
    def static_method():

        print("Static Method")

Usage:
employee = Employee()
employee.instance_method()
Employee.class_method()
Employee.static_method()

Output:
Instance Method
Google
Static Method

## When Should You Use Static Methods?

Use static methods when:

✅ Function belongs to class conceptually
✅ Does not need object data
✅ Does not need class data

Examples:

* Validation
* Conversion
* Utility Functions
* Formatting

## Django Example

Example Utility Class:

class UserUtils:

    @staticmethod
    def normalize_email(email):

        return email.lower()

Used in many large codebases.

## Advantages of Static Methods

* Better Organization
* Cleaner Code
* No Need To Create Object
* Utility Function Grouping

## Interview Questions

### Q1. What is a Static Method?

Answer: A method that belongs to a class but does not access object or class data.

### Q2. Which Decorator Creates a Static Method?

Answer: @staticmethod

### Q3. Does Static Method Use self?

Answer: No.

### Q4. Does Static Method Use cls?

Answer: No.

### Q5. Can Static Methods Access Instance Variables?

Answer: No.

### Q6. Can Static Methods Access Class Variables Directly?

Answer: No.
Unless class name is explicitly used.

### Q7. When Should We Use Static Methods?

Answer: For utility functions related to a class.

### Q8. Can We Call Static Methods Without Creating Objects?

Answer: Yes.

### Q9. Difference Between Class Method and Static Method?

Answer: Class Method: Uses cls.
Static Method: Uses neither self nor cls.

### Q10. Give Real World Examples of Static Methods.

Answer:

* Email Validation
* Password Validation
* Temperature Conversion
* Math Utilities

# Practice Questions

1. Create Calculator class.
2. Create Email Validator.
3. Create Password Validator.
4. Create Temperature Converter.
5. Create Currency Converter.
6. Create Student Utility class.
7. Create Interest Calculator.
8. Create Tax Calculator.
9. Create Discount Calculator.
10. Build Utility Methods using @staticmethod.

# Summary

Important Concepts:

* @staticmethod
* Utility Functions
* No self
* No cls

Method Types:

Instance Method: self

Class Method: cls

Static Method: Neither self nor cls

Used In:

* Django Utilities
* Validation Systems
* Converters
* Enterprise Applications

Static methods are best used for helper functions that logically belong to a class but do not require object or class state.
