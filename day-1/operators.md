"""
================================================
PYTHON OPERATORS
================================================

What is an Operator?

An operator is a symbol that performs an
operation on one or more operands (values).

Example:

10 + 20

10 and 20 are operands
+ is an operator

================================================
1. ARITHMETIC OPERATORS
================================================

Used for mathematical calculations.
"""

a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

"""
Output:

Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
Floor Division: 2
Modulus: 0
Exponent: 100000
"""

# ---------------------------------------------

"""
Modulus (%)

Returns remainder.
"""

print(10 % 3)

"""
Output:
1
"""

# ---------------------------------------------

"""
================================================
2. COMPARISON OPERATORS
================================================

Returns True or False.
"""

x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

"""
Output:

False
True
False
True
False
True
"""

# ---------------------------------------------

"""
================================================
3. LOGICAL OPERATORS
================================================

Used to combine conditions.

and
or
not
"""

age = 25
salary = 4000000

print(age > 18 and salary > 100000)
print(age > 30 or salary > 100000)
print(not age > 18)

"""
Output:

True
True
False
"""

# ---------------------------------------------

"""
AND Operator

Both conditions must be True.
"""

print(True and True)
print(True and False)

"""
Output:

True
False
"""

# ---------------------------------------------

"""
OR Operator

At least one condition must be True.
"""

print(True or False)
print(False or False)

"""
Output:

True
False
"""

# ---------------------------------------------

"""
NOT Operator

Reverses the result.
"""

print(not True)
print(not False)

"""
Output:

False
True
"""

# ---------------------------------------------

"""
================================================
4. ASSIGNMENT OPERATORS
================================================

Used to assign values.
"""

number = 10

number += 5
print(number)

number -= 2
print(number)

number *= 2
print(number)

"""
Output:

15
13
26
"""

# ---------------------------------------------

"""
Equivalent Forms

number += 5

means

number = number + 5
"""

# ---------------------------------------------

"""
================================================
5. MEMBERSHIP OPERATORS
================================================

Checks whether a value exists in a collection.

in
not in
"""

skills = ["Python", "AWS", "Docker"]

print("Python" in skills)
print("React" in skills)

print("React" not in skills)

"""
Output:

True
False
True
"""

# ---------------------------------------------

"""
================================================
6. IDENTITY OPERATORS
================================================

Checks whether two variables refer to the same object.

is
is not
"""

a = [1, 2, 3]
b = a

print(a is b)

"""
Output:

True
"""

# ---------------------------------------------

c = [1, 2, 3]

print(a is c)

"""
Output:

False
"""

# ---------------------------------------------

"""
================================================
OPERATOR PRECEDENCE
================================================

Python follows BODMAS.

()

**
* / // %
+ -
"""

result = 10 + 5 * 2

print(result)

"""
Output:
20
"""

# Because:

5 * 2 = 10

10 + 10 = 20
"""

# ---------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is an operator?

Answer:
An operator is a symbol that performs
operations on values or variables.

---------------------------------------------

Q2. What are Arithmetic Operators?

Answer:

+
-
*
/
//
/%
**

---------------------------------------------

Q3. What does % do?

Answer:
Returns the remainder.

Example:

10 % 3 = 1

---------------------------------------------

Q4. Difference between / and // ?

/  -> Normal Division
// -> Floor Division

Example:

10 / 3 = 3.3333

10 // 3 = 3

---------------------------------------------

Q5. What does == mean?

Answer:
Checks value equality.

Example:

10 == 10

Returns True

---------------------------------------------

Q6. Difference between = and == ?

=  Assignment

== Comparison

Example:

age = 25

age == 25

---------------------------------------------

Q7. What are Logical Operators?

Answer:

and
or
not

---------------------------------------------

Q8. What does 'in' operator do?

Answer:
Checks whether a value exists in a collection.

Example:

"Python" in skills

Returns True
"""

# ---------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Find sum of two numbers.

2. Find remainder when 25 is divided by 4.

3. Check whether age is greater than 18.

4. Check if "AWS" exists in a list.

5. Use and operator to check:

age > 18
salary > 50000

6. Predict output:

print(10 + 2 * 3)

7. Predict output:

print(10 // 3)

8. Predict output:

print(10 % 3)
"""