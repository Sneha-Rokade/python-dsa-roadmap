"""
================================================
PATTERN PROGRAMS IN PYTHON
================================================

What are Pattern Programs?

Pattern programs use loops (mostly nested loops)
to print shapes, stars, numbers, and characters.

Why Important?

1. Improves Logic Building
2. Strengthens Nested Loops
3. Common in Interviews
4. Helps in DSA Foundations

================================================
PATTERN 1
STAR TRIANGLE
================================================
"""

for i in range(1, 6):

    for j in range(i):

        print("*", end="")

    print()

"""
Output:

*
**
***
****
*****
"""

# ------------------------------------------------

"""
================================================
PATTERN 2
INVERTED STAR TRIANGLE
================================================
"""

for i in range(5, 0, -1):

    for j in range(i):

        print("*", end="")

    print()

"""
Output:

*****
****
***
**
*
"""

# ------------------------------------------------

"""
================================================
PATTERN 3
NUMBER TRIANGLE
================================================
"""

for i in range(1, 6):

    for j in range(1, i + 1):

        print(j, end="")

    print()

"""
Output:

1
12
123
1234
12345
"""

# ------------------------------------------------

"""
================================================
PATTERN 4
REPEATED NUMBER TRIANGLE
================================================
"""

for i in range(1, 6):

    for j in range(i):

        print(i, end="")

    print()

"""
Output:

1
22
333
4444
55555
"""

# ------------------------------------------------

"""
================================================
PATTERN 5
SQUARE STAR PATTERN
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
PATTERN 6
NUMBER SQUARE
================================================
"""

for i in range(5):

    for j in range(1, 6):

        print(j, end=" ")

    print()

"""
Output:

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

# ------------------------------------------------

"""
================================================
PATTERN 7
RIGHT ALIGNED TRIANGLE
================================================
"""

for i in range(1, 6):

    print(" " * (5 - i), end="")

    print("*" * i)

"""
Output:

    *
   **
  ***
 ****
*****
"""

# ------------------------------------------------

"""
================================================
PATTERN 8
PYRAMID
================================================
"""

rows = 5

for i in range(rows):

    print(" " * (rows - i - 1), end="")

    print("*" * (2 * i + 1))

"""
Output:

    *
   ***
  *****
 *******
*********
"""

# ------------------------------------------------

"""
================================================
PATTERN 9
INVERTED PYRAMID
================================================
"""

rows = 5

for i in range(rows):

    print(" " * i, end="")

    print("*" * (2 * (rows - i) - 1))

"""
Output:

*********
 *******
  *****
   ***
    *
"""

# ------------------------------------------------

"""
================================================
PATTERN 10
MULTIPLICATION TABLE GRID
================================================
"""

for i in range(1, 6):

    for j in range(1, 6):

        print(i * j, end="\t")

    print()

"""
Output:

1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. Why are pattern programs important?

Answer: They improve logical thinking and
understanding of nested loops.

------------------------------------------------

Q2. Which concept is most important
for pattern programs?

Answer: Nested Loops

------------------------------------------------

Q3. What is the role of the outer loop?

Answer: Controls the number of rows.

------------------------------------------------

Q4. What is the role of the inner loop?

Answer: Controls the number of columns
or items printed in each row.

------------------------------------------------

Q5. Are pattern programs useful in DSA?

Answer: Yes.

They strengthen looping and
problem-solving skills.
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1.

*
**
***
****
*****

------------------------------------------------

2.

*****
****
***
**
*

------------------------------------------------

3.

1
12
123
1234
12345

------------------------------------------------

4.

1
22
333
4444
55555

------------------------------------------------

5.

1
23
456
78910

------------------------------------------------

6.

A
AB
ABC
ABCD
ABCDE

------------------------------------------------

7.

*****
*****
*****
*****
*****

------------------------------------------------

8.

    *
   ***
  *****
 *******
*********

------------------------------------------------

9.

*********
 *******
  *****
   ***
    *

------------------------------------------------

10.

Print a multiplication grid of 10x10.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Concepts:

1. Nested Loops
2. Row Control
3. Column Control
4. Triangle Patterns
5. Pyramid Patterns
6. Number Patterns
7. Star Patterns

Pattern programs help build
problem-solving skills required for:

DSA
Competitive Programming
Interviews
Software Engineering
"""