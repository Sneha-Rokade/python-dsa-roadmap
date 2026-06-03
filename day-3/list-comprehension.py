"""
================================================
LIST COMPREHENSION IN PYTHON
================================================

What is List Comprehension?

List Comprehension is a shorter and
more Pythonic way to create lists.

Instead of using multiple lines with
a loop, we can create lists in a
single line.

================================================
TRADITIONAL METHOD
================================================
"""

numbers = []

for i in range(5):

    numbers.append(i)

print(numbers)

"""
Output:

[0, 1, 2, 3, 4]
"""

# ------------------------------------------------

"""
================================================
LIST COMPREHENSION METHOD
================================================
"""

numbers = [i for i in range(5)]

print(numbers)

"""
Output:

[0, 1, 2, 3, 4]
"""

# ------------------------------------------------

"""
================================================
SYNTAX
================================================

new_list = [expression for item in iterable]

Example: numbers = [i for i in range(5)]
"""

# ------------------------------------------------

"""
================================================
1. CREATE LIST OF NUMBERS
================================================
"""

numbers = [i for i in range(1, 11)]

print(numbers)

"""
Output: [1,2,3,4,5,6,7,8,9,10]
"""

# ------------------------------------------------

"""
================================================
2. SQUARE OF NUMBERS
================================================
"""

squares = [i * i for i in range(1, 6)]

print(squares)

"""
Output: [1, 4, 9, 16, 25]
"""

# ------------------------------------------------

"""
================================================
3. CUBE OF NUMBERS
================================================
"""

cubes = [i ** 3 for i in range(1, 6)]

print(cubes)

"""
Output: [1, 8, 27, 64, 125]
"""

# ------------------------------------------------

"""
================================================
4. EVEN NUMBERS
================================================
"""

evens = [
    i
    for i in range(1, 21)
    if i % 2 == 0
]

print(evens)

"""
Output: [2,4,6,8,10,12,14,16,18,20]
"""

# ------------------------------------------------

"""
================================================
5. ODD NUMBERS
================================================
"""

odds = [
    i
    for i in range(1, 21)
    if i % 2 != 0
]

print(odds)

"""
Output: [1,3,5,7,9,11,13,15,17,19]
"""

# ------------------------------------------------

"""
================================================
6. FILTER LONG WORDS
================================================
"""

skills = [
    "Python",
    "SQL",
    "Docker",
    "AWS",
    "Kubernetes"
]

result = [
    skill
    for skill in skills
    if len(skill) > 3
]

print(result)

"""
Output:

['Python', 'Docker', 'Kubernetes']
"""

# ------------------------------------------------

"""
================================================
7. UPPERCASE CONVERSION
================================================
"""

skills = [
    "python",
    "sql",
    "aws"
]

result = [
    skill.upper()
    for skill in skills
]

print(result)

"""
Output: ['PYTHON', 'SQL', 'AWS']
"""

# ------------------------------------------------

"""
================================================
8. FIRST LETTER EXTRACTION
================================================
"""

names = [
    "Alex",
    "John",
    "Emma"
]

result = [
    name[0]
    for name in names
]

print(result)

"""
Output: ['A', 'J', 'E']
"""

# ------------------------------------------------

"""
================================================
9. CONDITIONAL EXPRESSION
================================================
"""

numbers = [
    "Even"
    if i % 2 == 0
    else "Odd"
    for i in range(1, 6)
]

print(numbers)

"""
Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']
"""

# ------------------------------------------------

"""
================================================
10. REMOVE NEGATIVE NUMBERS
================================================
"""

numbers = [
    -5,
    10,
    -3,
    20,
    -1,
    30
]

positive_numbers = [
    num
    for num in numbers
    if num > 0
]

print(positive_numbers)

"""
Output: [10, 20, 30]
"""

# ------------------------------------------------

"""
================================================
11. CREATE LIST FROM STRING
================================================
"""

word = "Python"

letters = [
    char
    for char in word
]

print(letters)

"""
Output: ['P', 'y', 't', 'h', 'o', 'n']
"""

# ------------------------------------------------

"""
================================================
12. NESTED LIST COMPREHENSION
================================================
"""

matrix = [
    [j for j in range(3)]
    for i in range(3)
]

print(matrix)

"""
Output:
[
 [0,1,2],
 [0,1,2],
 [0,1,2]
]
"""

# ------------------------------------------------

"""
================================================
13. REAL WORLD EXAMPLE
================================================

Employee IDs
"""
employee_ids = [
    f"EMP{i}"
    for i in range(1001, 1006)
]

print(employee_ids)

"""
Output:
['EMP1001',
 'EMP1002',
 'EMP1003',
 'EMP1004',
 'EMP1005']
"""

# ------------------------------------------------

"""
================================================
14. REAL WORLD EXAMPLE
================================================

Email Extraction
"""

employees = [
    {
        "name": "Alex",
        "email": "alex@gmail.com"
    },
    {
        "name": "John",
        "email": "john@gmail.com"
    }
]

emails = [
    employee["email"]
    for employee in employees
]

print(emails)

"""
Output: ['alex@gmail.com', 'john@gmail.com']
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is List Comprehension?

Answer: A concise way to create lists.

------------------------------------------------

Q2. Why use List Comprehension?

Answer:
Less code
Better readability
Pythonic style

------------------------------------------------

Q3. Syntax of List Comprehension?

Answer: [expression for item in iterable]

------------------------------------------------

Q4. How do you filter values?

Answer: Use if condition.

Example:
[i for i in range(10)
 if i % 2 == 0]

------------------------------------------------

Q5. Can we use if-else?

Answer: Yes.

Example:
["Even" if i % 2 == 0
 else "Odd"
 for i in range(5)]

------------------------------------------------

Q6. Is List Comprehension faster?

Answer: Generally yes,
compared to traditional loops.

------------------------------------------------

Q7. Where is it used?

Answer: Data Processing
Backend Development
Automation
Machine Learning
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Create list from 1 to 100.

2. Create list of squares.

3. Create list of cubes.

4. Print even numbers.

5. Print odd numbers.

6. Convert names to uppercase.

7. Extract first letter of names.

8. Remove negative numbers.

9. Filter words longer than 5 chars.

10. Create employee IDs.

11. Extract emails from employee list.

12. Create multiplication table list.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Concepts:

1. List Comprehension
2. Filtering
3. Conditional Logic
4. Transformation
5. Nested Comprehension

Syntax:

[expression
 for item in iterable]

Benefits:

Less Code
Readable
Pythonic

"""