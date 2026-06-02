"""
================================================
CONDITIONAL STATEMENTS IN PYTHON
================================================

What are Conditional Statements?

Conditional statements are used to make decisions
in a program.

They execute different blocks of code based on
whether a condition is True or False.

Real World Examples:

1. Login System
   If username and password are correct
   Login Successful

2. ATM Machine
   If balance is sufficient
   Withdraw money

3. E-commerce
   If order amount > 5000
   Apply discount

================================================
1. IF STATEMENT
================================================

Executes code only when condition is True.
"""

age = 25

if age >= 18:
    print("Eligible to Vote")

"""
Output:
Eligible to Vote
"""

# ------------------------------------------------

"""
Flow:

Condition True
      ↓
Execute Block

Condition False
      ↓
Skip Block
"""

# ------------------------------------------------

"""
================================================
2. IF ELSE STATEMENT
================================================

Used when we want to handle both True
and False cases.
"""

age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

"""
Output:
Not Eligible
"""

# ------------------------------------------------

"""
================================================
3. IF ELIF ELSE STATEMENT
================================================

Used when multiple conditions need to be checked.
"""

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

"""
Output:
Grade B
"""

# ------------------------------------------------

"""
================================================
4. POSITIVE OR NEGATIVE NUMBER
================================================
"""

number = -5

if number >= 0:
    print("Positive")
else:
    print("Negative")

"""
Output:
Negative
"""

# ------------------------------------------------

"""
================================================
5. EVEN OR ODD
================================================
"""

number = 20

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

"""
Output:
Even
"""

# ------------------------------------------------

"""
================================================
6. FIND GREATER NUMBER
================================================
"""

num1 = 100
num2 = 200

if num1 > num2:
    print(num1)
else:
    print(num2)

"""
Output:
200
"""

# ------------------------------------------------

"""
================================================
7. LOGIN SYSTEM
================================================
"""

username = "admin"
password = "1234"

entered_username = "admin"
entered_password = "1234"

if username == entered_username and password == entered_password:
    print("Login Successful")
else:
    print("Invalid Credentials")

"""
Output:
Login Successful
"""

# ------------------------------------------------

"""
================================================
8. NESTED IF
================================================

Nested If means an if statement
inside another if statement.
"""

age = 25
salary = 50000

if age >= 18:
    if salary >= 30000:
        print("Eligible for Loan")

"""
Output:
Eligible for Loan
"""

# ------------------------------------------------

"""
================================================
9. LOGICAL OPERATORS WITH CONDITIONS
================================================
"""

age = 25
salary = 50000

if age >= 18 and salary >= 30000:
    print("Eligible")

"""
Output:
Eligible
"""

# ------------------------------------------------

"""
OR Operator

At least one condition must be True.
"""

age = 16
special_permission = True

if age >= 18 or special_permission:
    print("Allowed")

"""
Output:
Allowed
"""

# ------------------------------------------------

"""
NOT Operator

Reverses the result.
"""

is_blocked = False

if not is_blocked:
    print("Access Granted")

"""
Output:
Access Granted
"""

# ------------------------------------------------

"""
================================================
REAL WORLD EXAMPLE - ATM
================================================
"""

balance = 10000
withdraw_amount = 2000

if withdraw_amount <= balance:
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")

"""
Output:
Withdrawal Successful
"""

# ------------------------------------------------

"""
================================================
REAL WORLD EXAMPLE - DISCOUNT SYSTEM
================================================
"""

amount = 6000

if amount >= 5000:
    print("Discount Applied")
else:
    print("No Discount")

"""
Output:
Discount Applied
"""

# ------------------------------------------------

"""
================================================
COMMON MISTAKES
================================================

Wrong:
"""

# if age = 18:
#     print("Eligible")

"""
Reason:

=  Assignment Operator

Cannot be used for comparison.
"""

# ------------------------------------------------

"""
Correct:
"""

age = 18

if age == 18:
    print("Eligible")

"""
Output:
Eligible
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What are Conditional Statements?

Answer:
Conditional statements allow a program
to make decisions based on conditions.

------------------------------------------------

Q2. What is the difference between
if and if else?

Answer:

if:
Executes only when condition is True.

if else:
Handles both True and False conditions.

------------------------------------------------

Q3. What is elif?

Answer:

elif stands for "else if".

Used to check multiple conditions.

------------------------------------------------

Q4. What is Nested If?

Answer:

An if statement inside another
if statement.

------------------------------------------------

Q5. What operators are commonly used
with conditions?

Answer:

==
!=
>
<
>=
<=
and
or
not

------------------------------------------------

Q6. Difference between = and == ?

Answer:

=  Assignment Operator

== Comparison Operator

Example:

age = 25

age == 25

------------------------------------------------

Q7. Why are conditional statements important?

Answer:

They help programs make decisions and
control the flow of execution.

Examples:

Login Systems
ATM Systems
Payment Systems
E-commerce Applications
Banking Applications
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Check if a person is eligible to vote.

2. Check if a number is positive or negative.

3. Check if a number is even or odd.

4. Find greater of two numbers.

5. Find greatest among three numbers.

6. Grade Calculator.

7. ATM Withdrawal Program.

8. Login Validation System.

9. Check whether a year is leap year.

10. Check whether a person is eligible
    for a loan using age and salary.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

if       -> Single condition

if else  -> Two outcomes

if elif else -> Multiple conditions

Nested if -> if inside another if

Logical Operators:

and
or
not

Used heavily in:

Web Applications
Backend Development
Authentication
Payment Systems
Business Logic
"""