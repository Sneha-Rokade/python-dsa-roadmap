"""
================================================
TUPLES IN PYTHON
================================================

What is a Tuple?

A tuple is an ordered collection
used to store multiple values.

Tuples are IMMUTABLE.

Immutable means: After creation, values cannot be changed.

================================================
CHARACTERISTICS OF TUPLE
================================================

1. Ordered
2. Immutable
3. Allows Duplicates
4. Indexed

================================================
1. CREATE A TUPLE
================================================
"""

employee = ("Alex", 25, "Engineer")

print(employee)

"""
Output:

('Alex', 25, 'Engineer')
"""

# ------------------------------------------------

"""
================================================
2. ACCESS TUPLE ELEMENTS
================================================
"""

employee = ("Alex", 25, "Engineer")

print(employee[0])
print(employee[1])
print(employee[2])

"""
Output:

Alex
25
Engineer
"""

# ------------------------------------------------

"""
================================================
3. NEGATIVE INDEXING
================================================
"""

employee = ("Alex", 25, "Engineer")

print(employee[-1])

"""
Output:

Engineer
"""

# ------------------------------------------------

"""
================================================
4. TUPLE LENGTH
================================================
"""

employee = ("Alex", 25, "Engineer")

print(len(employee))

"""
Output:

3
"""

# ------------------------------------------------

"""
================================================
5. ITERATE THROUGH TUPLE
================================================
"""

employee = ("Alex", 25, "Engineer")

for item in employee:

    print(item)

"""
Output:

Alex
25
Engineer
"""

# ------------------------------------------------

"""
================================================
6. TUPLE ALLOWS DUPLICATES
================================================
"""

numbers = (10, 20, 20, 30, 20)

print(numbers)

"""
Output:

(10, 20, 20, 30, 20)
"""

# ------------------------------------------------

"""
================================================
7. COUNT()
================================================

Counts occurrences of value.
"""

numbers = (10, 20, 20, 30, 20)

print(numbers.count(20))

"""
Output:

3
"""

# ------------------------------------------------

"""
================================================
8. INDEX()
================================================

Returns position of value.
"""

skills = ("Python", "SQL", "AWS")

print(skills.index("SQL"))

"""
Output:

1
"""

# ------------------------------------------------

"""
================================================
9. TUPLE SLICING
================================================
"""

skills = (

    "Python",
    "SQL",
    "AWS",
    "Docker",
    "Kubernetes"

)

print(skills[1:4])

"""
Output:

('SQL', 'AWS', 'Docker')
"""

# ------------------------------------------------

"""
================================================
10. SINGLE ELEMENT TUPLE
================================================
"""

number = (10,)

print(type(number))

"""
Output:

<class 'tuple'>

Comma is mandatory.
"""

# ------------------------------------------------

"""
================================================
11. WITHOUT COMMA
================================================
"""

number = (10)

print(type(number))

"""
Output:

<class 'int'>

This is not a tuple.
"""

# ------------------------------------------------

"""
================================================
12. TUPLE UNPACKING
================================================
"""

name, age, role = (

    "Alex",
    25,
    "Engineer"

)

print(name)
print(age)
print(role)

"""
Output:

Alex
25
Engineer
"""

# ------------------------------------------------

"""
================================================
13. NESTED TUPLE
================================================
"""

data = (

    ("Alex", 25),

    ("John", 30),

    ("Emma", 28)

)

print(data[0])

"""
Output:

('Alex', 25)
"""

# ------------------------------------------------

"""
================================================
14. ACCESS NESTED TUPLE
================================================
"""

data = (

    ("Alex", 25),

    ("John", 30),

    ("Emma", 28)

)

print(data[1][0])

"""
Output:

John
"""

# ------------------------------------------------

"""
================================================
15. IMMUTABILITY EXAMPLE
================================================
"""

skills = ("Python", "SQL", "AWS")

# skills[1] = "PostgreSQL"

"""
Error: TypeError

Tuple object does not support
item assignment.

Reason: Tuple is immutable.
"""

# ------------------------------------------------

"""
================================================
REAL WORLD EXAMPLE
================================================

Database Record

Tuples are often used for
fixed values.

Example: (id, name, role)
"""

employee = (
    101,
    "Alex",
    "Engineer"
)

print(employee)

# ------------------------------------------------

"""
================================================
LIST VS TUPLE
================================================

LIST
[] brackets
Mutable
More Methods
Slightly Slower

------------------------------------------------

TUPLE
() brackets
Immutable
Less Methods
Slightly Faster
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is a Tuple?

Answer: A tuple is an ordered, immutable
collection.

------------------------------------------------

Q2. Are Tuples Mutable?

Answer: No.

Tuples are immutable.

------------------------------------------------

Q3. Does Tuple Allow Duplicates?

Answer: Yes.

------------------------------------------------

Q4. Does Tuple Maintain Order?

Answer: Yes.

------------------------------------------------

Q5. What methods are available
for Tuple?

Answer: count()
index()

------------------------------------------------

Q7. Why use Tuple?

Answer: When data should not change.

Example:

Employee ID
Coordinates
Database Records

------------------------------------------------

Q8. What is Tuple Unpacking?

Answer: Assigning tuple values to
multiple variables.

Example: name, age = ("Alex", 25)

------------------------------------------------

Q9. How do you create a
single-element tuple?

Answer: number = (10,)

Comma is required.
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Create a tuple of skills.

2. Print first element.

3. Print last element.

4. Find tuple length.

5. Count occurrences of 20.

6. Find index of SQL.

7. Perform tuple slicing.

8. Create single-element tuple.

9. Create nested tuple.

10. Access nested tuple element.

11. Use tuple unpacking.

12. Compare List vs Tuple.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Concepts:

1. Tuple
2. Ordered
3. Immutable
4. Duplicates Allowed
5. Indexing
6. Negative Indexing
7. Slicing
8. count()
9. index()
10. Tuple Unpacking

Tuple Use Cases:

Database Records
Coordinates
Configuration Data
Fixed Values
API Responses
""" 