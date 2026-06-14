# ADVANCED EXCEPTION HANDLING IN PYTHON

## Introduction

In Day 4, we learned:

* try
* except
* else
* finally

Now we will learn advanced concepts used in:

* Django
* REST APIs
* Enterprise Applications
* Production Systems

# REVIEW OF BASIC EXCEPTION HANDLING

try:
    number = int(input())
    print(100 / number)

except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Division By Zero")

This handles common exceptions.
Now let's go deeper.

# EXCEPTION HIERARCHY

All Python exceptions inherit from:

BaseException
    |
    └── Exception
            |
            ├── ValueError
            ├── TypeError
            ├── IndexError
            ├── KeyError
            ├── FileNotFoundError
            ├── ZeroDivisionError
            └── RuntimeError

Understanding hierarchy is important for interviews.

# CATCHING MULTIPLE EXCEPTIONS

Instead of:

try:
    value = int(input())
except ValueError:
    print("Value Error")
except TypeError:
    print("Type Error")

You can write:

try:

    value = int(input())
except (ValueError, TypeError):
    print("Invalid Input")

Cleaner code.

# EXCEPTION OBJECT

Every exception contains information.

Example:

try:
    print(10 / 0)
except ZeroDivisionError as error:
    print(error)

Output: division by zero

# EXCEPTION TYPE

Example:

try:
    print(10 / 0)
except Exception as error:

    print(type(error))

Output: <class 'ZeroDivisionError'>

Useful for debugging.

# GENERIC EXCEPTION HANDLING

Example:

try:
    risky_operation()
except Exception as error:
    print(error)

Output: Any Exception

## When To Use It?

Good:

try:
    database_operation()
except Exception as error:
    logger.error(error)

Bad: except:

Always prefer: except Exception

over: except:

# ELSE BLOCK

Runs only if no exception occurs.

Example:

try:
    number = int(input())
except ValueError:
    print("Invalid Input")

else:
    print("Success")

Input: 25

Output: Success

# FINALLY BLOCK

Always executes.

Example:

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error")
finally:
    print("Cleanup Done")

Output:
Error
Cleanup Done

# REAL WORLD FILE EXAMPLE

file = None

try:
    file = open("data.txt")
except FileNotFoundError:
    print("File Missing")
finally:
    if file:
        file.close()

Even if error occurs:

file.close()

still executes.

# RAISING EXCEPTIONS

You can manually create exceptions.

Syntax: raise ExceptionType("Message")

## Example
age = 15

if age < 18:
    raise ValueError(
        "Age Must Be 18 Or Above"
    )

Output: ValueError

# BUSINESS RULE VALIDATION

Example:
salary = -100

if salary < 0:
    raise ValueError(
        "Salary Cannot Be Negative"
    )

Used heavily in real applications.

# RE-RAISING EXCEPTIONS

Sometimes we log an exception and raise it again.

Example:

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Logged Error")
    raise

Output:
Logged Error
ZeroDivisionError

Very common in enterprise applications.

# ASSERT STATEMENT

Used during development.

Example: age = 25

assert age >= 18

Runs successfully.

Example: age = 15

assert age >= 18

Output: AssertionError

# NESTED TRY BLOCKS

Example:

try:
    try:
        print(10 / 0)
    except ValueError:
        print("Value Error")
except ZeroDivisionError:
    print("Outer Handler")

Output: Outer Handler

Rarely used.

# CUSTOM ERROR MESSAGES

Bad: raise ValueError()

Good:

raise ValueError(

    "Invalid User Age"

)

Always provide meaningful messages.

# EXCEPTION CHAINING

Example:

try:
    print(10 / 0)
except ZeroDivisionError as error:
    raise ValueError(
        "Calculation Failed"
    ) from error

Output: ValueError

while preserving original cause.
Used in large applications.

# LOGGING EXCEPTIONS

Production systems use logging.

Example:

import logging

try:
    print(10 / 0)
except Exception as error:
    logging.error(error)

Never rely only on: print()
in production.


# DJANGO EXAMPLE

Finding User:
try:
    user = User.objects.get(id=1)
except User.DoesNotExist:
    print("User Not Found")

Very common Django pattern.

# DJANGO FORM VALIDATION

if age < 18:

    raise ValueError(
        "Age Restriction"
    )

Used in:

* Forms
* APIs
* Serializers

# API EXAMPLE

try:

    data = response.json()

except ValueError:

    print("Invalid JSON")

Used in almost every backend system.

# PRODUCTION BEST PRACTICES

## 1. Catch Specific Exceptions

Good: except ValueError:

Bad: except Exception:

when specific exception is known.

## 2. Use Finally For Cleanup

Examples:

* Files
* Database Connections
* Network Connections

## 3. Log Errors

Good: logging.error(error)

Bad: print(error)

## 4. Don't Ignore Exceptions

Bad:

except:
    pass

Very dangerous.

## 5. Raise Meaningful Errors

Good:
raise ValueError(
    "Invalid Email Format"
)

# INTERVIEW QUESTIONS

### Q1. What is Exception Hierarchy?

Answer: A structured inheritance tree of exceptions.

### Q2. Difference Between Exception and BaseException?

Answer: Exception is the parent class of most application errors.
BaseException is the root class.

### Q3. What is raise?

Answer: Used to manually trigger exceptions.

### Q4. What is Re-Raising?

Answer: Handling an exception and raising it again.

### Q5. What is AssertionError?

Answer: Error raised when assert condition fails.

### Q6. Why Use Finally?

Answer: To guarantee cleanup operations.

### Q7. What is Exception Chaining?

Answer: Raising a new exception while preserving original cause.

### Q8. Why Log Exceptions?

Answer: For debugging and production monitoring.

### Q9. Which Exception Should Be Preferred?

Answer: Specific exceptions.

### Q10. Why Avoid except: ?

Answer: It catches everything and makes debugging difficult.

# PRACTICE QUESTIONS

1. Handle multiple exceptions.
2. Print exception object.
3. Use else block.
4. Use finally block.
5. Raise ValueError manually.
6. Raise TypeError manually.
7. Create salary validator.
8. Create age validator.
9. Implement assertion checks.
10. Log exceptions using logging module.

# SUMMARY

Advanced Concepts Covered:

* Exception Hierarchy
* Multiple Exceptions
* Exception Objects
* Generic Exception Handling
* Raising Exceptions
* Re-Raising Exceptions
* AssertionError
* Exception Chaining
* Logging Exceptions
* Production Best Practices

Used In:

* Django
* REST APIs
* Databases
* Enterprise Applications
* Production Systems

Advanced exception handling is a critical skill because professional applications must not only handle errors but also log, trace, and recover from them properly.
