"""
================================================
PYTHON DATA TYPES
================================================

What is a Data Type?

A data type defines the type of value stored in a variable.

Python automatically determines the data type.
This is called Dynamic Typing.

================================================
1. STRING (str)
================================================
"""

name = "Alex"

print(name)
print(type(name))

"""
Output:
Alex
<class 'str'>
"""

# ---------------------------------------------

"""
A string is a sequence of characters enclosed
inside single or double quotes.
"""

city = "Pune"
company = 'Google'

print(city)
print(company)

# ---------------------------------------------

"""
================================================
2. INTEGER (int)
================================================

Integers are whole numbers.
"""

age = 25

print(age)
print(type(age))

"""
Output:
25
<class 'int'>
"""

# ---------------------------------------------

"""
================================================
3. FLOAT (float)
================================================

Float represents decimal numbers.
"""

cgpa = 8.75

print(cgpa)
print(type(cgpa))

"""
Output:
8.75
<class 'float'>
"""

# ---------------------------------------------

"""
================================================
4. BOOLEAN (bool)
================================================

Boolean contains only two values:

True
False
"""

is_placed = True

print(is_placed)
print(type(is_placed))

"""
Output:
True
<class 'bool'>
"""

# ---------------------------------------------

"""
================================================
5. LIST
================================================

List is:

- Ordered
- Mutable
- Allows duplicates
- Uses square brackets []
"""

skills = ["Python", "AWS", "Docker"]

print(skills)
print(type(skills))

print(skills[0])
print(skills[1])

"""
Output:
['Python', 'AWS', 'Docker']
<class 'list'>
Python
AWS
"""

# ---------------------------------------------

"""
Lists are Mutable

We can modify values after creation.
"""

skills[1] = "Kubernetes"

print(skills)

"""
Output:
['Python', 'Kubernetes', 'Docker']
"""

# ---------------------------------------------

"""
================================================
6. TUPLE
================================================

Tuple is:

- Ordered
- Immutable
- Allows duplicates
- Uses parentheses ()
"""

coordinates = (10, 20, 30)

print(coordinates)
print(type(coordinates))

"""
Output:
(10, 20, 30)
<class 'tuple'>
"""

# ---------------------------------------------

"""
Tuple is Immutable

Values cannot be changed after creation.
"""

# coordinates[0] = 100
# Error

# ---------------------------------------------

"""
================================================
7. SET
================================================

Set is:

- Unordered
- Mutable
- No duplicates
- Uses curly braces {}
"""

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
print(type(numbers))

"""
Output:
{1, 2, 3, 4}
<class 'set'>
"""

# ---------------------------------------------

"""
Duplicates are automatically removed.
"""

# ---------------------------------------------

"""
================================================
8. DICTIONARY (dict)
================================================

Dictionary stores data as:

Key : Value

Uses curly braces {}
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Software Engineer"
}

print(employee)
print(type(employee))

"""
Output:
{
'name': 'Alex',
'age': 25,
'role': 'Software Engineer'
}
"""

# ---------------------------------------------

"""
Access values using keys.
"""

print(employee["name"])
print(employee["role"])

"""
Output:
Alex
Software Engineer
"""

# ---------------------------------------------

"""
================================================
MUTABLE VS IMMUTABLE
================================================

Mutable:
Value can be changed.

Examples:
List
Dictionary
Set

Immutable:
Value cannot be changed.

Examples:
String
Integer
Float
Boolean
Tuple
"""

# ---------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is a data type?

Answer:
A data type defines the type of value stored
inside a variable.

---------------------------------------------

Q2. What are the basic data types in Python?

Answer:

str
int
float
bool
list
tuple
set
dict

---------------------------------------------

Q3. What is the difference between List and Tuple?

List:
Mutable

Tuple:
Immutable

---------------------------------------------

Q4. What is a Dictionary?

Answer:
A collection of key-value pairs.

Example:

{
'name': 'Alex',
'age': 25
}

---------------------------------------------

Q5. What is a Set?

Answer:
A collection that stores unique values and
automatically removes duplicates.

---------------------------------------------

Q6. Which data types are Mutable?

Answer:

List
Dictionary
Set

---------------------------------------------

Q7. Which data types are Immutable?

Answer:

String
Integer
Float
Boolean
Tuple
"""

# ---------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Create a variable called company
   and store "Google"

2. Create age = 25
   Print its type

3. Create a list of 5 skills

4. Create a tuple of 3 cities

5. Create a set with duplicate values

6. Create a dictionary with:

   name
   age
   role

7. Identify:

   "Python" -> ?
   100 -> ?
   99.99 -> ?
   True -> ?
"""