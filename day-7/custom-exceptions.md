# CUSTOM EXCEPTIONS IN PYTHON

## What are Custom Exceptions?

Python provides built-in exceptions:

* ValueError
* TypeError
* KeyError
* IndexError
* FileNotFoundError

However, real-world applications often require business-specific errors.

Examples:

* InvalidAgeError
* InsufficientBalanceError
* UserNotFoundError
* InvalidCouponError

These are called **Custom Exceptions**.

# Why Use Custom Exceptions?

Imagine: age = 15

if age < 18:
    raise ValueError("Invalid Age")

Works fine.

But:

raise InvalidAgeError(
    "Age must be 18 or above"
)

is much more meaningful.

# Creating Your First Custom Exception

Syntax:

class MyException(Exception):
    pass

Every custom exception should inherit from: Exception

# Example 1

class InvalidAgeError(Exception):
    pass

Usage:

age = 15

if age < 18:
    raise InvalidAgeError(
        "Age must be 18 or above"
    )

Output:

InvalidAgeError: Age must be 18 or above

# Handling Custom Exceptions

class InvalidAgeError(Exception):
    pass

try:
    age = 15
    if age < 18:
        raise InvalidAgeError(
            "Age must be 18+"
        )
except InvalidAgeError as error:
    print(error)

Output: Age must be 18+

# Real World Example

Banking System

class InsufficientBalanceError(
    Exception
):
    pass

Usage:

balance = 1000
withdraw = 5000
if withdraw > balance:
    raise InsufficientBalanceError(
        "Not Enough Balance"
    )

Output: InsufficientBalanceError

# Custom Exception with Constructor

Sometimes we want extra information.

Example:

class InvalidAgeError(Exception):

    def __init__(self, age):
        self.age = age
        self.message = (
            f"{age} is not allowed"
        )
        super().__init__(self.message)

Usage: raiSe InvalidAgeError(15)

Output: 15 is not allowed

# Understanding super()

super().__init__(message)

Calls parent Exception constructor.
Important interview topic.

# Example: Student Marks

class InvalidMarksError(
    Exception
):
    pass

Usage: marks = 120

if marks > 100:
    raise InvalidMarksError(
        "Marks cannot exceed 100"
    )

# Example: User Not Found

class UserNotFoundError(
    Exception
):
    pass

Usage: user = None

if user is None:
    raise UserNotFoundError(
        "User does not exist"
    )

Very common in Django.

# Multiple Custom Exceptions

Example:

class InvalidAgeError(
    Exception
):
    pass

class InvalidSalaryError(
    Exception
):
    pass

Usage: raise InvalidAgeError()
raise InvalidSalaryError()

# Exception Hierarchy

Example:

Exception
├── InvalidAgeError
├── InvalidSalaryError
└── UserNotFoundError

All inherit from: Exception

# Base Application Exception

Large projects create a common parent.

Example:
class AppError(Exception):
    pass

Custom exceptions:

class InvalidAgeError(
    AppError
):
    pass

class UserNotFoundError(
    AppError
):
    pass

Now all application errors inherit from:

AppError

# Handling All App Errors

try:
    raise InvalidAgeError()
except AppError:
    print("Application Error")

Useful in enterprise systems.

# Real World E-Commerce Example

class ProductOutOfStockError(
    Exception
):
    pass

Usage:

stock = 0
if stock == 0:
    raise ProductOutOfStockError(
        "Product unavailable"
    )

# Real World ATM Example

class InsufficientBalanceError(
    Exception
):
    pass

balance = 500
amount = 1000

if amount > balance:
    raise InsufficientBalanceError(
        "Balance too low"
    )

# Real World Login System

class InvalidCredentialsError(
    Exception
):
    pass

password = "123"
if password != "admin123":
    raise InvalidCredentialsError(
        "Wrong password"
    )

# Django Example

class UserBlockedError(
    Exception
):
    pass

Usage:

if user.is_blocked:

    raise UserBlockedError(
        "Account Blocked"
    )

Common in business logic.

# Django REST API Example

class InvalidCouponError(
    Exception
):
    pass

if coupon_expired:
    raise InvalidCouponError(
        "Coupon Expired"
    )

# Custom Exception with Error Code

Example:

class APIError(Exception):

    def __init__(
        self,
        code,
        message
    ):

        self.code = code
        self.message = message
        super().__init__(message)

Usage:
raise APIError(
    400,
    "Bad Request"
)
Useful in APIs.

# Best Practices

## Use Meaningful Names

Good: InvalidAgeError
Bad: MyError

## Inherit from Exception

Good: class MyError(Exception):
Bad: class MyError:

## Add Useful Messages

Good:
raise InvalidAgeError(
    "Age must be 18+"
)

Bad: raise InvalidAgeError()

## Group Related Exceptions

Example:

AppError
├── UserError
├── ProductError
└── PaymentError

Useful for large projects.

# Interview Questions

### Q1. What is a Custom Exception?

Answer: An exception created by developers for application-specific errors.

### Q2. Why Use Custom Exceptions?

Answer: To represent business-specific errors clearly.

### Q3. Which Class Should Custom Exceptions Inherit From?

Answer: Exception

### Q4. What is pass Used For?

Answer: Placeholder when no additional logic is needed.

### Q5. Can Custom Exceptions Have Constructors?

Answer: Yes.

Using: __init__()

### Q6. Why Use super()?

Answer: To call parent Exception constructor.

### Q7. Can We Create Multiple Custom Exceptions?

Answer: Yes.

### Q8. What is an Application Base Exception?

Answer: A common parent exception for all project-specific exceptions.

### Q9. Are Custom Exceptions Used in Django?

Answer: Yes.
Frequently in business logic and APIs.

### Q10. Real World Examples?

Answer:

* InvalidAgeError
* UserNotFoundError
* ProductOutOfStockError
* InvalidCouponError
* InsufficientBalanceError

# Practice Questions

1. Create InvalidAgeError.
2. Create InvalidSalaryError.
3. Create UserNotFoundError.
4. Create InvalidMarksError.
5. Create ProductOutOfStockError.
6. Create InvalidCredentialsError.
7. Add constructor to custom exception.
8. Create AppError base class.
9. Handle multiple custom exceptions.
10. Build mini ATM system using custom exceptions.

# Summary

Important Concepts:

* Custom Exceptions
* Inheritance
* Exception Class
* super()
* Application Exceptions

Real World Usage:

* Banking Systems
* E-Commerce
* Django Applications
* REST APIs
* Enterprise Software

Custom exceptions make applications more readable, maintainable, and professional by clearly representing business-specific errors.
