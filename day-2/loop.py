"""
================================================
FOR LOOPS IN PYTHON
================================================

What is a Loop?

A loop is used to execute a block of code
multiple times.

Why Loops?

1. Avoid Repetition
2. Write Less Code
3. Improve Readability
4. Useful for Data Processing

Without Loop:

print(1)
print(2)
print(3)
print(4)
print(5)

With Loop:

for i in range(1, 6):
    print(i)

================================================
1. BASIC FOR LOOP
================================================
"""

for i in range(5):
    print(i)

"""
Output:

0
1
2
3
4

range(5)

Start = 0 (default)
Stop = 5 (excluded)
"""

# ------------------------------------------------

"""
================================================
2. FOR LOOP WITH START AND STOP
================================================
"""

for i in range(1, 6):
    print(i)

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
3. FOR LOOP WITH STEP
================================================
"""

for i in range(1, 11, 2):
    print(i)

"""
Output:

1
3
5
7
9

Step = 2
"""

# ------------------------------------------------

"""
================================================
4. PRINT EVEN NUMBERS
================================================
"""

for i in range(2, 11, 2):
    print(i)

"""
Output:

2
4
6
8
10
"""

# ------------------------------------------------

"""
================================================
5. PRINT ODD NUMBERS
================================================
"""

for i in range(1, 11, 2):
    print(i)

"""
Output:

1
3
5
7
9
"""

# ------------------------------------------------

"""
================================================
6. ITERATING THROUGH A STRING
================================================
"""

name = "Alex"

for char in name:
    print(char)

"""
Output:

A
l
e
x
"""

# ------------------------------------------------

"""
================================================
7. ITERATING THROUGH A LIST
================================================
"""

skills = ["Python", "SQL", "AWS"]

for skill in skills:
    print(skill)

"""
Output:

Python
SQL
AWS
"""

# ------------------------------------------------

"""
================================================
8. SUM OF NUMBERS
================================================
"""

total = 0

for i in range(1, 6):
    total = total + i

print(total)

"""
Output:

15

1 + 2 + 3 + 4 + 5
"""

# ------------------------------------------------

"""
================================================
9. COUNT EVEN NUMBERS
================================================
"""

numbers = [10, 15, 20, 25, 30]

count = 0

for num in numbers:

    if num % 2 == 0:
        count += 1

print(count)

"""
Output:

3
"""

# ------------------------------------------------

"""
================================================
10. FIND MAXIMUM NUMBER
================================================
"""

numbers = [10, 40, 5, 80, 20]

maximum = numbers[0]

for num in numbers:

    if num > maximum:
        maximum = num

print(maximum)

"""
Output:

80
"""

# ------------------------------------------------

"""
================================================
11. FIND MINIMUM NUMBER
================================================
"""

numbers = [10, 40, 5, 80, 20]

minimum = numbers[0]

for num in numbers:

    if num < minimum:
        minimum = num

print(minimum)

"""
Output:

5
"""

# ------------------------------------------------

"""
================================================
12. MULTIPLICATION TABLE
================================================
"""

number = 5

for i in range(1, 11):

    print(number * i)

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
13. NESTED LOOP INTRODUCTION
================================================
"""

for i in range(3):

    for j in range(3):

        print(i, j)

"""
Output:

0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is a Loop?

Answer:

A loop is used to execute a block
of code repeatedly.

------------------------------------------------

Q2. What is a For Loop?

Answer:

A for loop is used to iterate over
a sequence of values.

------------------------------------------------

Q3. What does range() do?

Answer:

range() generates a sequence of numbers.

Example:

range(5)

Produces:

0, 1, 2, 3, 4

------------------------------------------------

Q4. Why does range(5) stop at 4?

Answer:

The stop value is excluded.

range(start, stop)

Includes start
Excludes stop

------------------------------------------------

Q5. Difference between range(5)
and range(1, 6)?

range(5)

0 1 2 3 4

range(1, 6)

1 2 3 4 5

------------------------------------------------

Q6. How do you print even numbers?

Answer:

for i in range(2, 11, 2):
    print(i)

------------------------------------------------

Q7. How do you print odd numbers?

Answer:

for i in range(1, 11, 2):
    print(i)

------------------------------------------------

Q8. Can a for loop iterate over strings?

Answer: Yes.

Example:

for char in "Alex":
    print(char)

------------------------------------------------

Q9. Can a for loop iterate over lists?

Answer: Yes.

Example:

for item in my_list:
    print(item)

------------------------------------------------

Q10. What is a Nested Loop?

Answer: A loop inside another loop.
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Print numbers from 1 to 20

2. Print even numbers from 1 to 50

3. Print odd numbers from 1 to 50

4. Find sum of numbers from 1 to 100

5. Print multiplication table of 7

6. Count vowels in a string

7. Find maximum element in a list

8. Find minimum element in a list

9. Count even numbers in a list

10. Count odd numbers in a list

11. Print all characters of a string

12. Find sum of list elements
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Concepts:

1. For Loop
2. range()
3. Start, Stop, Step
4. Looping Through Strings
5. Looping Through Lists
6. Sum Using Loops
7. Count Using Loops
8. Maximum Element
9. Minimum Element
10. Nested Loops

"""