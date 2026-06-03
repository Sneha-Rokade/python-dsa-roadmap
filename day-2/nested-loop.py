"""
================================================
NESTED LOOPS IN PYTHON
================================================

What is a Nested Loop?

A nested loop is a loop inside another loop.

Syntax:

for i in range():
    for j in range():
        statements

Outer Loop:
Runs first

Inner Loop:
Runs completely for every iteration
of the outer loop.

================================================
1. BASIC NESTED LOOP
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
2. UNDERSTANDING EXECUTION
================================================

Outer Loop = 3 Times

For each outer iteration,
inner loop runs 3 times.

Total Executions:

3 × 3 = 9
"""

# ------------------------------------------------

"""
================================================
3. PRINT ROW AND COLUMN
================================================
"""

for row in range(1, 4):

    for column in range(1, 4):

        print(f"Row {row} Column {column}")

"""
Output:

Row 1 Column 1
Row 1 Column 2
Row 1 Column 3

Row 2 Column 1
Row 2 Column 2
Row 2 Column 3

Row 3 Column 1
Row 3 Column 2
Row 3 Column 3
"""

# ------------------------------------------------

"""
================================================
4. PRINT SQUARE PATTERN
================================================
"""

for i in range(5):

    for j in range(5):

        print("*", end=" ")

    print()

"""
Output:

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

# ------------------------------------------------

"""
================================================
5. PRINT NUMBER GRID
================================================
"""

for i in range(3):

    for j in range(3):

        print(j + 1, end=" ")

    print()

"""
Output:

1 2 3
1 2 3
1 2 3
"""

# ------------------------------------------------

"""
================================================
6. MULTIPLICATION TABLE GRID
================================================
"""

for i in range(1, 4):

    for j in range(1, 4):

        print(i * j, end=" ")

    print()

"""
Output:

1 2 3
2 4 6
3 6 9
"""

# ------------------------------------------------

"""
================================================
7. ITERATING THROUGH 2D LIST
================================================
"""

matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]

for row in matrix:

    for value in row:

        print(value, end=" ")

    print()

"""
Output:

1 2 3
4 5 6
7 8 9
"""

# ------------------------------------------------

"""
================================================
8. COUNT TOTAL ITERATIONS
================================================
"""

count = 0

for i in range(4):

    for j in range(4):

        count += 1

print(count)

"""
Output:

16

4 × 4 = 16
"""

# ------------------------------------------------

"""
================================================
9. REAL WORLD EXAMPLE
================================================

Cinema Seats

Rows = A, B, C

Seats = 1, 2, 3
"""

rows = ["A", "B", "C"]

for row in rows:

    for seat in range(1, 4):

        print(f"{row}{seat}")

"""
Output:

A1
A2
A3
B1
B2
B3
C1
C2
C3
"""

# ------------------------------------------------

"""
================================================
10. REAL WORLD EXAMPLE
================================================

Employee Attendance

Departments and Employees
"""

departments = ["HR", "IT"]

employees = ["Alex", "John"]

for department in departments:

    for employee in employees:

        print(department, "-", employee)

"""
Output:

HR - Alex
HR - John
IT - Alex
IT - John
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is a Nested Loop?

Answer: A loop inside another loop.

------------------------------------------------

Q2. How many times does the inner loop run?

Answer: The inner loop runs completely for
every iteration of the outer loop.

------------------------------------------------

Q3. If outer loop runs 3 times and
inner loop runs 4 times, how many
total iterations occur?

Answer: 3 × 4 = 12

------------------------------------------------

Q4. What is the Time Complexity of
two nested loops?

Answer: O(n²)

------------------------------------------------

Q5. Where are Nested Loops used?

Answer:

- Pattern Problems
- Matrices
- Tables
- Data Processing
- Grid Operations

------------------------------------------------

Q6. Can Nested Loops be used with
while loops?

Answer: Yes.

A while loop can be placed inside
another while loop.
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Print a 4x4 star square.

2. Print a 5x5 star square.

3. Print numbers:

1 2 3
1 2 3
1 2 3

4. Print:

1 1 1
2 2 2
3 3 3

5. Print multiplication grid.

6. Count total iterations in a
3x3 nested loop.

7. Print seat numbers:

A1 A2 A3
B1 B2 B3

8. Print all combinations of:

Colors = Red, Blue

Sizes = S, M, L
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Concepts:

1. Nested Loop
2. Outer Loop
3. Inner Loop
4. Row and Column
5. Grid Problems
6. Matrix Traversal
7. Pattern Building

Time Complexity:

Single Loop

O(n)

Nested Loop

O(n²)

Nested loops are heavily used in:

DSA
Matrices
Pattern Problems
Games
Data Processing
Backend Systems
"""