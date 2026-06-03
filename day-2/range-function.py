"""
================================================
RANGE FUNCTION IN PYTHON
================================================

What is range()?

range() generates a sequence of numbers.

It is commonly used with loops.

Syntax:

range(stop)

range(start, stop)

range(start, stop, step)

================================================
1. RANGE WITH STOP VALUE
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

Start = 0 (default)
Stop = 5 (excluded)
"""

# ------------------------------------------------

"""
================================================
2. RANGE WITH START AND STOP
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

Start = 1
Stop = 6 (excluded)
"""

# ------------------------------------------------

"""
================================================
3. RANGE WITH STEP
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

for i in range(2, 21, 2):
    print(i)

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
5. PRINT ODD NUMBERS
================================================
"""

for i in range(1, 20, 2):
    print(i)

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
6. COUNT BACKWARDS
================================================
"""

for i in range(10, 0, -1):
    print(i)

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

Negative step moves backward.
"""

# ------------------------------------------------

"""
================================================
7. PRINT MULTIPLES OF 5
================================================
"""

for i in range(5, 51, 5):
    print(i)

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
8. SUM OF NUMBERS
================================================
"""

total = 0

for i in range(1, 6):

    total += i

print(total)

"""
Output:

15
"""

# ------------------------------------------------

"""
================================================
9. LENGTH OF RANGE
================================================
"""

count = 0

for i in range(1, 11):

    count += 1

print(count)

"""
Output:

10
"""

# ------------------------------------------------

"""
================================================
10. REAL WORLD EXAMPLE
================================================

Generate Employee IDs
"""

for employee_id in range(1001, 1006):
    print(employee_id)

"""
Output:

1001
1002
1003
1004
1005
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is range()?

Answer: range() generates a sequence of numbers.

------------------------------------------------

Q2. What is the syntax of range()?

Answer:

range(stop)

range(start, stop)

range(start, stop, step)

------------------------------------------------

Q3. What does range(5) produce?

Answer:

0
1
2
3
4

------------------------------------------------

Q4. Why does range(5) stop at 4?

Answer: The stop value is excluded.

------------------------------------------------

Q5. What does range(1, 6) produce?

Answer:

1
2
3
4
5

------------------------------------------------

Q6. What does range(1, 10, 2) produce?

Answer:

1
3
5
7
9

------------------------------------------------

Q7. How do you count backwards using range()?

Answer: Use a negative step.

Example:

range(10, 0, -1)

------------------------------------------------

Q8. How do you print even numbers using range()?

Answer: range(2, 21, 2)

------------------------------------------------

Q9. How do you print odd numbers using range()?

Answer: range(1, 20, 2)

------------------------------------------------

Q10. Is the stop value included?

Answer: No.

The stop value is excluded.
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Print numbers from 1 to 50

2. Print numbers from 50 to 1

3. Print even numbers from 1 to 100

4. Print odd numbers from 1 to 100

5. Print multiples of 3

6. Print multiples of 7

7. Find sum of numbers from 1 to 100

8. Print multiplication table of 9

9. Count numbers from 1 to 100

10. Print numbers in reverse order
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Concepts:

1. range(stop)
2. range(start, stop)
3. range(start, stop, step)
4. Positive Step
5. Negative Step
6. Even Numbers
7. Odd Numbers
8. Reverse Counting

range() is one of the most frequently
used functions in:

Python Programming
DSA
Automation
Backend Development
Data Processing
"""