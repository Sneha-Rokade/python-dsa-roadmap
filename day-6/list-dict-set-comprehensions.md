# LIST, DICTIONARY, AND SET COMPREHENSIONS IN PYTHON

## What is Comprehension?

Comprehension is a short and elegant way to create collections.

Instead of writing multiple lines using loops, we can write concise code.

Python supports:

* List Comprehension
* Dictionary Comprehension
* Set Comprehension

# WHY USE COMPREHENSIONS?

Without Comprehension:

numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:

    squares.append(num ** 2)

print(squares)

Output: [1, 4, 9, 16, 25]

Using Comprehension:

numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print(squares)

Output: [1, 4, 9, 16, 25]

Cleaner and shorter.

# LIST COMPREHENSION

## Syntax

[new_value for item in iterable]

## Example 1

numbers = [1, 2, 3, 4]

result = [num * 2 for num in numbers]

print(result)

Output: [2, 4, 6, 8]

## Example 3

Convert Strings to Uppercase

names = ["alex", "john", "emma"]

result = [name.upper() for name in names]

print(result)

Output: ['ALEX', 'JOHN', 'EMMA']

# LIST COMPREHENSION WITH CONDITION

Syntax:

[expression for item in iterable if condition]

## Example 1

Even Numbers

numbers = [1, 2, 3, 4, 5, 6]

evens = [
    num
    for num in numbers
    if num % 2 == 0
]

print(evens)

Output: [2, 4, 6]

## Example 2

Numbers Greater Than 10

numbers = [5, 10, 15, 20]

result = [
    num
    for num in numbers
    if num > 10
]

print(result)

Output: [15, 20]

# IF-ELSE IN LIST COMPREHENSION

Syntax: [value_if_true if condition else value_if_false for item in iterable]

## Example

numbers = [1, 2, 3, 4, 5]

result = [
    "Even"
    if num % 2 == 0
    else "Odd"
    for num in numbers
]

print(result)

Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# NESTED LIST COMPREHENSION

Example:
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flatten = [
    num
    for row in matrix
    for num in row
]

print(flatten)

Output: [1, 2, 3, 4, 5, 6]

# DICTIONARY COMPREHENSION

## Syntax {key:value for item in iterable}

## Example 1

Create Squares Dictionary

numbers = [1, 2, 3, 4]

squares = {
    num: num ** 2
    for num in numbers
}

print(squares)

Output:
{
 1:1,
 2:4,
 3:9,
 4:16
}

## Example 2

Word Length Dictionary

words = [
    "python",
    "django",
    "api"
]

lengths = {
    word: len(word)
    for word in words
}

print(lengths)

Output:
{
 'python': 6,
 'django': 6,
 'api': 3
}

# DICTIONARY COMPREHENSION WITH CONDITION

Example:

numbers = [1, 2, 3, 4, 5]

result = {
    num: num ** 2
    for num in numbers
    if num % 2 == 0
}

print(result)

Output:
{
 2:4,
 4:16
}

# SET COMPREHENSION

## Syntax {expression for item in iterable}

## Example 1

numbers = [1, 2, 3, 4]

result = {
    num ** 2
    for num in numbers
}

print(result)

Output: {1, 4, 9, 16}

## Example 2

Remove Duplicates

numbers = [
    1, 1, 2, 2, 3, 3
]

unique = {
    num
    for num in numbers
}

print(unique)

Output: {1, 2, 3}

# REAL WORLD EXAMPLE

Student Marks

marks = {
    "Alex": 85,
    "John": 90,
    "Emma": 78
}

result = {
    name: marks
    for name, marks in marks.items()
    if marks >= 80
}

print(result)

Output:
{
 'Alex':85,
 'John':90
}

# REAL WORLD EXAMPLE

Email Extraction

users = [
    "alex@gmail.com",
    "john@yahoo.com",
    "emma@gmail.com"
]

gmail_users = [
    email
    for email in users
    if "@gmail.com" in email
]

print(gmail_users)

Output:

[
 'alex@gmail.com',
 'emma@gmail.com'
]

# COMPREHENSION VS LOOPS

Traditional Loop:

result = []

for num in numbers:

    result.append(num * 2)

Comprehension:

result = [
    num * 2
    for num in numbers
]

Less code.
More readable.

# WHEN NOT TO USE COMPREHENSIONS

Bad:

result = [
    complex_logic_here
    for item in items
    if multiple_conditions
]

If code becomes difficult to read, use normal loops.
Readability is more important.

# ADVANTAGES

* Shorter Code
* Better Readability
* Faster Execution
* Pythonic Style

# INTERVIEW QUESTIONS

### Q1. What is List Comprehension?

Answer: A concise way to create lists using a single line of code.

### Q2. What is Dictionary Comprehension?

Answer: A concise way to create dictionaries.

### Q3. What is Set Comprehension?

Answer: A concise way to create sets.

### Q4. Can We Use Conditions?

Answer: Yes.

Using: if

inside comprehension.

### Q5. Can We Use if-else?

Answer: Yes.

### Q6. Can We Create Nested Comprehensions?

Answer: Yes.

### Q7. Why Use Comprehensions?

Answer: Cleaner and more efficient code.

### Q8. Are Comprehensions Faster Than Loops?

Answer: Usually yes.

### Q9. Which Collection Types Support Comprehensions?

Answer:

* List
* Dictionary
* Set

### Q10. Should We Always Use Comprehensions?

Answer: No.

Only when readability remains good.

# PRACTICE QUESTIONS

1. Create squares using list comprehension.
2. Create cubes using list comprehension.
3. Find even numbers.
4. Find odd numbers.
5. Create uppercase names list.
6. Create dictionary of squares.
7. Create dictionary of word lengths.
8. Create unique values using set comprehension.
9. Flatten nested list.
10. Filter student marks above 80.

# SUMMARY

Important Concepts:

* List Comprehension
* Dictionary Comprehension
* Set Comprehension
* Conditional Comprehension
* Nested Comprehension

Syntax:

List: [expression for item in iterable]

Dictionary: {key:value for item in iterable}

Set: {expression for item in iterable}

Used In:

* Django
* Data Engineering
* APIs
* Automation
* Enterprise Applications

Comprehensions are one of the most Pythonic ways to create and transform collections efficiently.
