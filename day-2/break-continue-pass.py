"""
================================================
BREAK, CONTINUE AND PASS IN PYTHON
================================================

These statements are used to control
the flow of loops and programs.

1. break
2. continue
3. pass

================================================
1. BREAK STATEMENT
================================================

break immediately terminates the loop.
"""

for i in range(1, 11):

    if i == 5:
        break

    print(i)

"""
Output:

1
2
3
4

Loop stops when i becomes 5.
"""

# ------------------------------------------------

"""
================================================
2. BREAK EXAMPLE
================================================
"""

number = 1

while number <= 10:

    if number == 6:
        break

    print(number)

    number += 1

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
3. CONTINUE STATEMENT
================================================

continue skips the current iteration
and moves to the next iteration.
"""

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

"""
Output:

1
2
4
5

3 is skipped.
"""

# ------------------------------------------------

"""
================================================
4. CONTINUE EXAMPLE
================================================
"""

for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)

"""
Output:

1
3
5
7
9

Even numbers skipped.
"""

# ------------------------------------------------

"""
================================================
5. PASS STATEMENT
================================================

pass does nothing.

Used as a placeholder.
"""

if True:
    pass

print("Program Running")

"""
Output:

Program Running
"""

# ------------------------------------------------

"""
================================================
6. PASS EXAMPLE
================================================
"""

for i in range(5):

    if i == 3:
        pass

    print(i)

"""
Output:

0
1
2
3
4

pass does not affect execution.
"""

# ------------------------------------------------

"""
================================================
7. BREAK IN LOGIN SYSTEM
================================================
"""

correct_password = "admin123"

attempts = [
    "test",
    "hello",
    "admin123"
]

for password in attempts:

    if password == correct_password:

        print("Login Successful")

        break

    print("Wrong Password")

"""
Output:

Wrong Password
Wrong Password
Login Successful
"""

# ------------------------------------------------

"""
================================================
8. CONTINUE IN DATA FILTERING
================================================
"""

numbers = [10, 15, 20, 25, 30]

for num in numbers:

    if num % 2 != 0:
        continue

    print(num)

"""
Output:

10
20
30
"""

# ------------------------------------------------

"""
================================================
9. DIFFERENCE BETWEEN BREAK
AND CONTINUE
================================================

break:

Stops the entire loop.

continue:

Skips current iteration only.
"""

# ------------------------------------------------

"""
Example: break
"""

for i in range(1, 6):

    if i == 3:
        break

    print(i)

"""
Output:

1
2
"""

# ------------------------------------------------

"""
Example: continue
"""

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

"""
Output:

1
2
4
5
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is break?

Answer: break immediately terminates
the loop.

------------------------------------------------

Q2. What is continue?

Answer: continue skips the current iteration
and moves to the next iteration.

------------------------------------------------

Q3. What is pass?

Answer: pass is a placeholder statement.

It does nothing.

------------------------------------------------

Q4. Difference Between break
and continue?

break: Stops the loop completely.

continue: Skips only current iteration.

------------------------------------------------

Q5. When is pass used?

Answer: When code is not implemented yet.

Example:

if condition:
    pass

------------------------------------------------

Q6. Can break be used in
while loops?

Answer: Yes.

------------------------------------------------

Q7. Can continue be used in
while loops?

Answer: Yes.

------------------------------------------------

Q8. Does pass affect program flow?

Answer: No.

It simply acts as a placeholder.
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Print numbers from 1 to 20
   and stop at 10 using break.

2. Print numbers from 1 to 20
   and skip 5 using continue.

3. Print only odd numbers
   using continue.

4. Create a password checker
   using break.

5. Print multiples of 3
   and skip multiples of 6.

6. Create an empty function
   using pass.

7. Create an empty class
   using pass.

8. Print numbers from 1 to 50
   and stop when number becomes 25.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

break

✓ Stops the loop completely

continue

✓ Skips current iteration

pass

✓ Placeholder
✓ Does nothing

Common Usage:

break
- Login Systems
- Search Operations
- Menu Programs

continue
- Filtering Data
- Skipping Invalid Records

pass
- Future Development
- Empty Functions
- Empty Classes
"""