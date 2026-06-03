"""
================================================
INPUT AND OUTPUT IN PYTHON
================================================

What is Input?

Input means taking data from the user.

Examples:

- Enter Name
- Enter Age
- Enter Salary
- Enter Marks

What is Output?

Output means displaying information
to the user.

Example:

print("Hello World")

================================================
1. SIMPLE OUTPUT
================================================
"""

print("Hello World")

"""
Output:

Hello World
"""

# ------------------------------------------------

"""
================================================
2. PRINT MULTIPLE VALUES
================================================
"""

name = "Alex"
age = 25

print(name, age)

"""
Output:

Alex 25
"""

# ------------------------------------------------

"""
================================================
3. SIMPLE INPUT
================================================
"""

name = input("Enter your name: ")

print(name)

"""
Input:

Alex

Output:

Alex

Note:

input() always returns a string.
"""

# ------------------------------------------------

"""
================================================
4. INPUT AND OUTPUT
================================================
"""

name = input("Enter your name: ")

print("Welcome", name)

"""
Input:

Alex

Output:

Welcome Alex
"""

# ------------------------------------------------

"""
================================================
5. USING F-STRINGS
================================================
"""

name = input("Enter your name: ")

print(f"Welcome {name}")

"""
Input:

Alex

Output:

Welcome Alex
"""

# ------------------------------------------------

"""
================================================
6. TAKING AGE INPUT
================================================
"""

age = input("Enter your age: ")

print(age)

"""
Input:

25

Output:

25

Data Type:

String
"""

# ------------------------------------------------

"""
================================================
7. CHECK INPUT TYPE
================================================
"""

age = input("Enter your age: ")

print(type(age))

"""
Output:

<class 'str'>

Important:

input() returns string by default.
"""

# ------------------------------------------------

"""
================================================
8. MULTIPLE INPUTS
================================================
"""

first_name = input("Enter first name: ")

last_name = input("Enter last name: ")

print(first_name, last_name)

"""
Input:

Alex
Smith

Output:

Alex Smith
"""

# ------------------------------------------------

"""
================================================
9. EMPLOYEE DETAILS
================================================
"""

employee_name = input("Enter employee name: ")

role = input("Enter role: ")

print(f"Employee: {employee_name}")
print(f"Role: {role}")

"""
Example Output:

Employee: Alex
Role: Software Engineer
"""

# ------------------------------------------------

"""
================================================
10. STUDENT DETAILS
================================================
"""

student_name = input("Enter student name: ")

college = input("Enter college name: ")

print(f"{student_name} studies at {college}")

"""
Example Output:

Alex studies at ABC University
"""

# ------------------------------------------------

"""
================================================
11. REAL WORLD EXAMPLE
================================================

LOGIN SYSTEM
"""

username = input("Enter username: ")

password = input("Enter password: ")

print("Login Attempt Received")

"""
In real applications,
input values are validated
against database records.
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is Input?

Answer: Input means taking data from the user.

------------------------------------------------

Q2. What is Output?

Answer: Output means displaying information
to the user.

------------------------------------------------

Q3. Which function is used
to take input?

Answer: input()

------------------------------------------------

Q4. Which function is used
to display output?

Answer: print()

------------------------------------------------

Q5. What data type does input()
return?

Answer: String (str)

------------------------------------------------

Q6. How do you display a variable?

Answer:

print(variable_name)

Example:

print(name)

------------------------------------------------

Q7. What is the benefit of f-strings?

Answer: They allow easy variable formatting.

Example:

print(f"Hello {name}")
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Take name input and print it.

2. Take age input and print it.

3. Take city input and print it.

4. Take college name and print it.

5. Take employee details and display them.

6. Take username and password.

7. Take two names and print full name.

8. Create a student information program.

9. Create an employee information program.

10. Create a customer registration form.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Functions:

input()

Used to take user input.

print()

Used to display output.

Important Note:

input() always returns string.

Concepts Learned:

1. Input
2. Output
3. print()
4. input()
5. f-Strings
6. User Interaction

These concepts are used in:

Forms
Login Systems
Web Applications
APIs
Backend Development
Desktop Applications
"""