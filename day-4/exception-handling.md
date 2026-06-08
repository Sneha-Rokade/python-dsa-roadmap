# EXCEPTION HANDLING IN PYTHON

## What is an Exception?

An exception is a runtime error that occurs while a program is executing.

Examples:

* Dividing by zero
* Accessing invalid list index
* Opening non-existent file
* Invalid user input

## Example Without Exception Handling

a = 10
b = 0

print(a / b)

Output: ZeroDivisionError

Program stops immediately.

## Why Use Exception Handling?

Benefits:

* Prevent application crashes
* Improve user experience
* Handle unexpected situations
* Write robust applications

Backend applications use exception handling heavily.

## try and except

Syntax:

try:
    risky_code

except:
    error_handling_code

Example:

try:

    num = 10 / 0

except:

    print("Cannot divide by zero")

Output: Cannot divide by zero

Program continues running.

## Catch Specific Exceptions

Example:

try:

    num = 10 / 0

except ZeroDivisionError:

    print("Division by zero is not allowed")

Output: Division by zero is not allowed

## Multiple Exceptions

try:

    number = int(input("Enter Number: "))

    result = 100 / number

except ValueError:

    print("Invalid Number")

except ZeroDivisionError:

    print("Cannot Divide By Zero")

## Exception As Variable

try:

    num = 10 / 0

except Exception as error:

    print(error)

Output: division by zero

Useful for debugging.

## else Block

Runs only if no exception occurs.

try:

    result = 10 / 2

except ZeroDivisionError:

    print("Error")

else:

    print("Success")

Output: Success

## finally Block

Always executes.

try:

    result = 10 / 2

except:

    print("Error")

finally:

    print("Program Finished")

Output: Program Finished

Even if an exception occurs, finally executes.

## Complete Example

try:

    number = int(input("Enter Number: "))

    result = 100 / number

except ValueError:

    print("Enter Valid Number")

except ZeroDivisionError:

    print("Zero Not Allowed")

else:

    print("Result:", result)

finally:

    print("Execution Completed")

## Raising Exceptions

You can create exceptions manually.

Example:

age = -1

if age < 0:

    raise ValueError("Age cannot be negative")

Output:

ValueError: Age cannot be negative

## Custom Exception Example

salary = -5000

if salary < 0:

    raise Exception("Salary cannot be negative")

## Real World Example

Login Validation

password = ""

if password == "":

    raise ValueError("Password cannot be empty")

## Real World Example

Bank Withdrawal

balance = 1000

withdraw = 5000

if withdraw > balance:

    raise Exception("Insufficient Balance")

## Common Python Exceptions

### ZeroDivisionError

10 / 0

### ValueError

int("hello")

### IndexError

numbers = [10, 20]

print(numbers[5])

### KeyError

employee = {"name": "Alex"}

print(employee["salary"])

### TypeError

10 + "hello"

### FileNotFoundError

open("abc.txt")

## Real Backend Example

try:

    user = get_user(user_id)

except Exception:

    return {
        "message": "User Not Found"
    }

Common in Django and REST APIs.

## Interview Questions

### Q1. What is Exception Handling?

Answer: A mechanism used to handle runtime errors without crashing the program.

### Q2. Why Use Exception Handling?

Answer: To make applications reliable and prevent crashes.

### Q3. Difference Between Syntax Error and Exception?

Syntax Error: Occurs before execution.

Exception: Occurs during execution.

### Q4. What is try Block?

Answer: Contains code that may generate an exception.

### Q5. What is except Block?

Answer: Handles exceptions.

### Q6. What is finally Block?

Answer: Always executes whether exception occurs or not.

### Q7. What is else Block?

Answer: Executes when no exception occurs.

### Q8. What is raise?

Answer: Used to generate exceptions manually.

### Q9. Difference Between Exception and Error?

Exception: Can be handled.

Error: Usually critical problem.

### Q10. What is Exception as e?

Example: except Exception as e

Used to access exception details.

## Practice Questions

1. Handle divide by zero.
2. Handle invalid input.
3. Handle list index error.
4. Handle dictionary key error.
5. Handle file not found error.
6. Use else block.
7. Use finally block.
8. Raise ValueError.
9. Create login validation.
10. Create bank withdrawal validation.

## Summary

Important Concepts:

* Exception
* try
* except
* else
* finally
* raise

Common Exceptions:

* ZeroDivisionError
* ValueError
* IndexError
* KeyError
* TypeError
* FileNotFoundError

Used In:

* Django
* Flask
* FastAPI
* APIs
* Databases
* Cloud Applications

Every production application relies on exception handling.
