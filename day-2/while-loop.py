"""
================================================
WHILE LOOP IN PYTHON
================================================

What is a While Loop?

A while loop executes a block of code
as long as the condition remains True.

Difference Between For and While

For Loop:
Used when number of iterations is known.

While Loop:
Used when number of iterations is unknown.

================================================
1. BASIC WHILE LOOP
================================================
"""

count = 1

while count <= 5:
    print(count)
    count += 1

"""
Output:

1
2
3
4
5
"""

# ------------------------------------------------

"""
================================================
2. PRINT NUMBERS 1 TO 10
================================================
"""

number = 1

while number <= 10:
    print(number)
    number += 1

"""
Output:

1
2
3
4
5
6
7
8
9
10
"""

# ------------------------------------------------

"""
================================================
3. PRINT EVEN NUMBERS
================================================
"""

number = 2

while number <= 20:
    print(number)
    number += 2

"""
Output:

2
4
6
8
10
12
14
16
18
20
"""

# ------------------------------------------------

"""
================================================
4. PRINT ODD NUMBERS
================================================
"""

number = 1

while number <= 19:
    print(number)
    number += 2

"""
Output:

1
3
5
7
9
11
13
15
17
19
"""

# ------------------------------------------------

"""
================================================
5. SUM OF NUMBERS
================================================
"""

n = 5

count = 1
total = 0

while count <= n:

    total += count

    count += 1

print(total)

"""
Output:

15

1 + 2 + 3 + 4 + 5
"""

# ------------------------------------------------

"""
================================================
6. MULTIPLICATION TABLE
================================================
"""

number = 5

count = 1

while count <= 10:

    print(number * count)

    count += 1

"""
Output:

5
10
15
20
25
30
35
40
45
50
"""

# ------------------------------------------------

"""
================================================
7. COUNT DOWN
================================================
"""

count = 10

while count >= 1:

    print(count)

    count -= 1

"""
Output:

10
9
8
7
6
5
4
3
2
1
"""

# ------------------------------------------------

"""
================================================
8. FIND NUMBER OF DIGITS
================================================
"""

number = 12345

count = 0

while number > 0:

    number = number // 10

    count += 1

print(count)

"""
Output:

5
"""

# ------------------------------------------------

"""
================================================
9. REVERSE A NUMBER
================================================
"""

number = 1234

reverse = 0

while number > 0:

    digit = number % 10

    reverse = reverse * 10 + digit

    number = number // 10

print(reverse)

"""
Output:

4321
"""

# ------------------------------------------------

"""
================================================
10. FACTORIAL OF A NUMBER
================================================
"""

number = 5

factorial = 1

while number > 0:

    factorial *= number

    number -= 1

print(factorial)

"""
Output:

120
"""

# ------------------------------------------------

"""
================================================
11. INFINITE LOOP
================================================
"""

# while True:
#     print("Hello")

"""
This loop never stops.

Use carefully.
"""

# ------------------------------------------------

"""
================================================
12. USER INPUT EXAMPLE
================================================
"""

# password = ""

# while password != "admin123":

#     password = input("Enter Password: ")

# print("Login Successful")

"""
Loop continues until correct password
is entered.
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is a While Loop?

Answer: A while loop executes a block of code
as long as the condition remains True.

------------------------------------------------

Q2. When should we use a While Loop?

Answer: When the number of iterations is unknown.

------------------------------------------------

Q3. Difference Between For and While?

For Loop: Known number of iterations.

While Loop: Unknown number of iterations.

------------------------------------------------

Q4. What causes an Infinite Loop?

Answer: When the loop condition never becomes False.

Example:

while True:
    print("Hello")

------------------------------------------------

Q5. How do we stop a While Loop?

Answer: By changing the condition to False.

Example:

count += 1

------------------------------------------------

Q6. Can While Loop be used for input validation?

Answer: Yes.

Example:

Keep asking for password
until correct value is entered.

------------------------------------------------

Q7. How is While Loop used in Real Projects?

Answer:

- Login Systems
- Menu Systems
- Chat Applications
- Game Loops
- Automation Scripts
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Print numbers from 1 to 20

2. Print numbers from 20 to 1

3. Print even numbers from 1 to 50

4. Print odd numbers from 1 to 50

5. Find sum of numbers from 1 to n

6. Find factorial of a number

7. Count digits in a number

8. Reverse a number

9. Check whether a number is palindrome

10. Create a simple login system
using while loop
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Concepts:

1. While Loop
2. Condition Checking
3. Counter Variable
4. Increment
5. Decrement
6. Infinite Loop
7. Factorial
8. Reverse Number
9. Count Digits
10. Input Validation

"""