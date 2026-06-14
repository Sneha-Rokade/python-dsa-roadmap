# LAMBDA, MAP, FILTER, AND REDUCE IN PYTHON

## Functional Programming in Python

Python supports a programming style called:

Functional Programming

Common tools:

* lambda
* map()
* filter()
* reduce()

These help write concise and efficient code.

# LAMBDA FUNCTIONS

## What is a Lambda Function?

A lambda function is an anonymous function.

Anonymous means: No function name

Normal function:

def square(x):

    return x * x

Lambda version:

lambda x: x * x

## Lambda Syntax

lambda arguments: expression

Example: square = lambda x: x * x

print(square(5))

Output: 25

## Lambda with Multiple Arguments

add = lambda a, b: a + b

print(add(10, 20))

Output: 30

## Lambda Example

multiply = lambda a, b: a * b

print(multiply(5, 4))

Output: 20

## Why Use Lambda?

Useful when:

* Small functions
* One-time use
* Passed into map(), filter(), sort()

# MAP FUNCTION

## What is map()?

map() applies a function to every item in an iterable.

Syntax: map(function, iterable)

## Example 1

Without map: numbers = [1, 2, 3, 4]

result = []

for num in numbers:

    result.append(num * 2)

print(result)

Output: [2, 4, 6, 8]

## Using map()

numbers = [1, 2, 3, 4]

result = map(
    lambda x: x * 2,
    numbers
)

print(list(result))

Output: [2, 4, 6, 8]

## Example 2

numbers = [1, 2, 3, 4]

squares = map(
    lambda x: x ** 2,
    numbers
)

print(list(squares))

Output: [1, 4, 9, 16]

# FILTER FUNCTION

## What is filter()?

filter() selects items that satisfy a condition.

Syntax: filter(function, iterable)

## Example 1

Find even numbers.

numbers = [1, 2, 3, 4, 5, 6]

evens = filter(
    lambda x: x % 2 == 0,
    numbers
)

print(list(evens))

Output: [2, 4, 6]

## Example 2

Find numbers greater than 10.

numbers = [5, 10, 15, 20]

result = filter(
    lambda x: x > 10,
    numbers
)

print(list(result))

Output: [15, 20]

# REDUCE FUNCTION

## What is reduce()?

reduce() applies a function repeatedly and reduces a sequence to a single value.

Must import: from functools import reduce

## Example 1

Sum all numbers.

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(
    lambda a, b: a + b,
    numbers
)

print(result)

Output: 10

## How reduce() Works

For: [1, 2, 3, 4]

Steps:
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10

Final answer: 10

## Example 2

Find product.

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(
    lambda a, b: a * b,
    numbers
)

print(result)

Output: 24

# Combining Lambda + Map

numbers = [1, 2, 3, 4]

result = map(
    lambda x: x * 10,
    numbers
)

print(list(result))

Output: [10, 20, 30, 40]

# Combining Lambda + Filter

numbers = [1, 2, 3, 4, 5, 6]

result = filter(
    lambda x: x > 3,
    numbers
)

print(list(result))

Output: [4, 5, 6]

# Real World Example

Student Marks

marks = [35, 90, 25, 78, 60]

passed = filter(
    lambda x: x >= 40,
    marks
)

print(list(passed))

Output: [90, 78, 60]

# Real World Example

Price Calculation

prices = [100, 200, 300]

discounted = map(
    lambda x: x * 0.9,
    prices
)

print(list(discounted))

Output: [90.0, 180.0, 270.0]

# Sorting with Lambda

Very common interview question.

Example:

students = [

    ("Alex", 25),

    ("John", 22),

    ("Emma", 28)
]

students.sort(

    key=lambda student: student[1]

)

print(students)

Output:
[
 ('John', 22),
 ('Alex', 25),
 ('Emma', 28)
]

# Advantages

## Lambda

* Short code
* One-line functions

## Map

* Transform data

## Filter

* Select data

## Reduce

* Aggregate data

# Interview Questions

### Q1. What is a Lambda Function?

Answer: An anonymous function created using the lambda keyword.

### Q2. What is map()?

Answer: Applies a function to every element of an iterable.

### Q3. What is filter()?

Answer: Filters elements based on a condition.

### Q4. What is reduce()?

Answer: Reduces a sequence to a single value.

### Q5. Which Module Provides reduce()?

Answer: functools

### Q6. Can Lambda Have Multiple Arguments?

Answer: Yes.

### Q7. Why Use Lambda?

Answer: For small one-time functions.

### Q8. What Does map() Return?

Answer: A map object.

Usually converted using: list()

### Q9. What Does filter() Return?

Answer: A filter object.

Usually converted using: list()

### Q10. Real World Uses?

Answer:

* Data Processing
* APIs
* Django QuerySets
* Sorting
* Analytics

# Practice Questions

1. Create square lambda.
2. Create add lambda.
3. Double list values using map().
4. Find squares using map().
5. Find even numbers using filter().
6. Find odd numbers using filter().
7. Find numbers greater than 50.
8. Sum list using reduce().
9. Multiply list using reduce().
10. Sort students using lambda.

# Summary

Important Concepts:

* lambda
* map()
* filter()
* reduce()

Use Cases:

* Data Transformation
* Data Filtering
* Aggregation
* Sorting

Used In:

* Data Engineering
* Analytics
* Django
* APIs
* Enterprise Applications
