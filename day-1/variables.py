""""
=========================================
PYTHON VARIABLES - DAY 1 NOTES
=========================================

What is a Variable?
-------------------
A variable is a container used to store data in memory.

Example:
name = "Sneha"

Here:
Variable Name = name
Value = "Sneha"

Python automatically determines the data type.
This is called Dynamic Typing.

=========================================
VARIABLE CREATION
=========================================
"""

name = "Sneha"
age = 31
salary = 4000000

print(name)
print(age)
print(salary)

"""
Output:
Sneha
31
4000000
"""

# --------------------------------------

"""
VARIABLE REASSIGNMENT

Variables can be changed after creation.
"""

city = "Pune"
print(city)

city = "Mumbai"
print(city)

"""
Output:
Pune
Mumbai
"""

# --------------------------------------

"""
DYNAMIC TYPING

Python automatically assigns data types.
"""

value = 100
print(type(value))

value = "Python"
print(type(value))

"""
Output:
<class 'int'>
<class 'str'>
"""

# --------------------------------------

"""
COMMON DATA TYPES
"""

name = "Sneha"       # string
age = 31             # integer
cgpa = 8.5           # float
is_placed = True     # boolean

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_placed))

# --------------------------------------

"""
MULTIPLE VARIABLES
"""

company = "Google"
location = "Pune"
package = 4000000

print(company, location, package)

# --------------------------------------

"""
F-STRING FORMATTING

Modern and preferred way.
"""

name = "Sneha"
age = 31

print(f"My name is {name}")
print(f"My age is {age}")

"""
Output:
My name is Sneha
My age is 31
"""

# --------------------------------------

"""
VARIABLE NAMING RULES

Allowed:
"""

student_name = "Sneha"
studentAge = 31
_age = 31

# --------------------------------------

"""
Not Allowed:

2name = "Sneha"
student-name = "Sneha"
class = "Python"

Reason:
Variable cannot start with number.
Hyphen not allowed.
Keywords not allowed.
"""

# --------------------------------------

"""
MEMORY BASICS

When:

name = "Sneha"

Python creates an object in memory
and variable 'name' points to it.

name ----> "Sneha"

When:

name = "Rohit"

name now points to new value.

name ----> "Rohit"
"""

# --------------------------------------

"""
INTERVIEW QUESTIONS

Q1. What is a variable?

Answer:
A variable is a named memory location
used to store data.

--------------------------------------

Q2. Is Python statically typed?

Answer:
No.
Python is dynamically typed.

--------------------------------------

Q3. What is dynamic typing?

Answer:
The data type is automatically determined
during runtime.

--------------------------------------

Q4. Can variable values be changed?

Answer:
Yes.
Variables can be reassigned.

--------------------------------------

Q5. What is the difference between:

age = 25

and

age = "25"

Answer:

25      -> Integer
"25"    -> String

=========================================
PRACTICE QUESTIONS
=========================================

1. Create variables:
   name, city, salary

2. Print using f-string

3. Change city value

4. Print type of:
   int
   str
   float
   bool

5. Create:
   name = "Alex"
   role = "Software Enginner"

   Print:
   "I want 4000000 package at Google"
"""