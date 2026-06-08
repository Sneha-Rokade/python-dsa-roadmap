# F-STRING (Formatted String)

## What is an F-String?

F-String stands for **Formatted String Literal**.

It allows us to insert variables and expressions directly inside a string using curly braces `{}`.

Introduced in Python 3.6.

Syntax:

f"Text {variable}"

## Why Do We Use F-Strings?

Without F-Strings:

name = "Alex"
age =  25

print("My name is " + name + " and I am " + str(age) + " years old.")

Problems:

* Hard to read
* Need type conversion (`str(age)`)

With F-Strings:

name = "Alex"
age = 25

print(f"My name is {name} and I am {age} years old.")

Output:

My name is Alex and I am 25 years old.

Cleaner and more readable.

## Basic Example

name = "Rohit"

print(f"Welcome {name}")

Output:

Welcome Rohit

## Multiple Variables

name = "Alex"
city = "Alaska"
salary = 4000000

print(f"{name} lives in {city} and earns {salary}")

Output:
Alex lives in Alaska and earns 4000000

## Mathematical Expressions

We can perform calculations inside `{}`.

a = 10
b = 20

print(f"Sum = {a + b}")

Output:
Sum = 30

## Using Functions

name = "python"

print(f"Length = {len(name)}")

Output:
Length = 6

## Decimal Formatting
price = 99.98765

print(f"{price:.2f}")

Output:
99.99

Explanation:

.2f

means:

* 2 digits after decimal
* f = float

## Percentage Formatting

score = 85

print(f"Your score is {score}%")

Output:

Your score is 85%

## Alignment Example
name = "Alex"

print(f"{name:>10}")

Output:
     Alex

Used in reports and formatted output.

## Real-World Example

Employee Information:

name = "Rohit"
role = "Backend Engineer"
company = "Google"

print(f"{name} works as a {role} at {company}")

Output:

Rohit works as a Backend Engineer at Google

## Why F-Strings Are Preferred

Advantages:

1. Easy to Read
2. Fast Execution
3. No Type Conversion Required
4. Supports Expressions
5. Used in Modern Python Code

## Comparison

### String Concatenation
name = "Alex"

print("Hello " + name)

### Format Method

name = "Alex"

print("Hello {}".format(name))

### F-String

name = "Alex"

print(f"Hello {name}")

Most modern Python developers prefer F-Strings.

## Interview Questions

### Q1. What is an F-String?

An F-String is a formatted string literal that allows variables and expressions to be embedded directly inside a string using curly braces `{}`.

### Q2. Why are F-Strings preferred?

Because they are:

* More readable
* Faster
* Easier to write
* Support expressions directly

### Q3. When were F-Strings introduced?

Python 3.6

### Q4. Can we perform calculations inside an F-String?

Yes.

Example:
a = 10
b = 20

print(f"{a + b}")

Output:
30


### Q5. How do you print only 2 decimal places?

price = 99.98765

print(f"{price:.2f}")

Output:

99.99

## Practice Questions

### Question 1

name = "Rohit"

Print:
Hello Rohit

### Question 2

name = "Alex"
age = 25

Print:
My name is Alex and I am 25 years old

### Question 3

a = 10
b = 20

Print:
Sum = 30

### Question 4

price = 199.9876

Print:
199.99

### Question 5

name = "Alex"
role = "Software Engineer"

Print:
I am Alex and I work as a "Software Engineer"

## Summary

F-Strings are the modern and recommended way to create formatted strings in Python. They improve readability, reduce code complexity, and are widely used in production applications.
