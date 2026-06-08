"""
================================================
TYPE CASTING IN PYTHON
================================================

What is Type Casting?

Type Casting means converting one
data type into another data type.

Examples:

String -> Integer
Integer -> String
Integer -> Float
Float -> Integer

Why Type Casting?

input() always returns string.

To perform mathematical operations,
we must convert strings into numbers.

================================================
1. CHECK DATA TYPE
================================================
"""

age = "25"

print(type(age))

"""
Output:

<class 'str'>
"""

# ------------------------------------------------

"""
================================================
2. STRING TO INTEGER
================================================
"""

age = "25"

age = int(age)

print(age)
print(type(age))

"""
Output:

25

<class 'int'>
"""

# ------------------------------------------------

"""
================================================
3. STRING TO FLOAT
================================================
"""

salary = "50000.50"

salary = float(salary)

print(salary)
print(type(salary))

"""
Output:

50000.5

<class 'float'>
"""

# ------------------------------------------------

"""
================================================
4. INTEGER TO STRING
================================================
"""

employee_id = 101

employee_id = str(employee_id)

print(employee_id)
print(type(employee_id))

"""
Output:

101

<class 'str'>
"""

# ------------------------------------------------

"""
================================================
5. INTEGER TO FLOAT
================================================
"""

number = 100

number = float(number)

print(number)
print(type(number))

"""
Output:

100.0

<class 'float'>
"""

# ------------------------------------------------

"""
================================================
6. FLOAT TO INTEGER
================================================
"""

cgpa = 8.9

cgpa = int(cgpa)

print(cgpa)

"""
Output:

8

Decimal part removed.
"""

# ------------------------------------------------

"""
================================================
7. USER INPUT WITH TYPE CASTING
================================================
"""

age = int(input("Enter your age: "))

print(age)
print(type(age))

"""
Input:

25

Output:

25

<class 'int'>
"""

# ------------------------------------------------

"""
================================================
8. ADDITION WITHOUT TYPE CASTING
================================================
"""

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)

"""
Input:

10
20

Output:

1020

Reason:

Both are strings.
"""

# ------------------------------------------------

"""
================================================
9. ADDITION WITH TYPE CASTING
================================================
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)

"""
Input:

10
20

Output:

30
"""

# ------------------------------------------------

"""
================================================
10. FLOAT INPUT
================================================
"""

price = float(input("Enter product price: "))

print(price)

"""
Input:

99.99

Output:

99.99
"""

# ------------------------------------------------

"""
================================================
11. BOOLEAN TYPE CASTING
================================================
"""

value = bool(1)

print(value)

"""
Output:

True
"""

value = bool(0)

print(value)

"""
Output:

False
"""

# ------------------------------------------------

"""
================================================
12. REAL WORLD EXAMPLE
================================================

EMPLOYEE SALARY CALCULATOR
"""

basic_salary = float(input("Enter salary: "))

bonus = float(input("Enter bonus: "))

total_salary = basic_salary + bonus

print(f"Total Salary: {total_salary}")

"""
Input:

50000
5000

Output:

55000
"""

# ------------------------------------------------

"""
================================================
13. REAL WORLD EXAMPLE
================================================

STUDENT MARKS
"""

marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))

total = marks1 + marks2 + marks3

print(f"Total Marks: {total}")

"""
Input:

80
90
85

Output:

255
"""

# ------------------------------------------------

"""
================================================
COMMON TYPE CASTING FUNCTIONS
================================================

int()

Converts to Integer

Example: int("25")

-----------------------------------------------

float()

Converts to Float

Example: float("99.9")

-----------------------------------------------

str()

Converts to String

Example: str(100)

-----------------------------------------------

bool()

Converts to Boolean

Example: bool(1)

True
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is Type Casting?

Answer: Type Casting is converting one
data type into another.

------------------------------------------------

Q2. Why is Type Casting needed?

Answer: Because input() returns strings.

To perform calculations,
we convert strings into numbers.

------------------------------------------------

Q3. Which function converts
string to integer?

Answer: int()

------------------------------------------------

Q4. Which function converts
string to float?

Answer: float()

------------------------------------------------

Q5. Which function converts
integer to string?

Answer: str()

------------------------------------------------

Q6. What happens when
int(8.9) is executed?

Output: 8

Decimal part is removed.

------------------------------------------------

Q7. What is the output?

num1 = "10"
num2 = "20"

print(num1 + num2)

Answer:

1020

Because strings are concatenated.

------------------------------------------------

Q8. What is the output?

num1 = int("10")
num2 = int("20")

print(num1 + num2)

Answer:

30
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Take age input and convert to int.

2. Take salary input and convert to float.

3. Take two numbers and find sum.

4. Take three marks and find total.

5. Take product price and quantity
   and calculate total cost.

6. Convert integer to string.

7. Convert float to integer.

8. Check data type before and
   after type casting.

9. Create simple calculator.

10. Create employee salary calculator.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Type Casting Functions:

int()
float()
str()
bool()

Important Point:

input() returns string by default.

Most Common Usage:

age = int(input())

price = float(input())

Concepts Learned:

1. String to Integer
2. String to Float
3. Integer to String
4. Integer to Float
5. Float to Integer
6. Boolean Conversion

Used In:

Forms
APIs
Backend Development
Data Processing
Calculations
Web Applications
"""