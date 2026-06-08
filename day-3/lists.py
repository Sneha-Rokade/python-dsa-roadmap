"""
================================================
LISTS IN PYTHON
================================================

What is a List?

A list is used to store multiple values
in a single variable.

Example:

skills = ["Python", "SQL", "AWS"]

Why Lists?

Without List:

skill1 = "Python"
skill2 = "SQL"
skill3 = "AWS"

With List:

skills = ["Python", "SQL", "AWS"]

Lists help store and manage collections
of data efficiently.

================================================
CHARACTERISTICS OF LIST
================================================

1. Ordered
2. Mutable
3. Allows Duplicates
4. Indexed

================================================
1. CREATE A LIST
================================================
"""

skills = ["Python", "SQL", "AWS"]

print(skills)

"""
Output:

['Python', 'SQL', 'AWS']
"""

# ------------------------------------------------

"""
================================================
2. ACCESS ELEMENTS USING INDEX
================================================
"""

skills = ["Python", "SQL", "AWS"]

print(skills[0])
print(skills[1])
print(skills[2])

"""
Output:

Python
SQL
AWS

Index starts from 0.
"""

# ------------------------------------------------

"""
================================================
3. NEGATIVE INDEXING
================================================
"""

skills = ["Python", "SQL", "AWS"]

print(skills[-1])

"""
Output:

AWS

-1 means last element.
"""

# ------------------------------------------------

"""
================================================
4. LIST WITH DIFFERENT DATA TYPES
================================================
"""

employee = [

    "Alex",

    25,

    True,

    50000.50

]

print(employee)

"""
Output:

['Alex', 25, True, 50000.5]
"""

# ------------------------------------------------

"""
================================================
5. MODIFY LIST ELEMENT
================================================
"""

skills = ["Python", "SQL", "AWS"]

skills[1] = "PostgreSQL"

print(skills)

"""
Output:

['Python', 'PostgreSQL', 'AWS']

Lists are mutable.
"""

# ------------------------------------------------

"""
================================================
6. FIND LENGTH OF LIST
================================================
"""

skills = ["Python", "SQL", "AWS"]

print(len(skills))

"""
Output:

3
"""

# ------------------------------------------------

"""
================================================
7. ITERATE THROUGH LIST
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
8. CHECK ELEMENT EXISTS
================================================
"""

skills = ["Python", "SQL", "AWS"]

print("Python" in skills)

"""
Output:

True
"""

# ------------------------------------------------

"""
================================================
9. LIST SLICING
================================================
"""

skills = [

    "Python",
    "SQL",
    "AWS",
    "Docker",
    "Kubernetes"

]

print(skills[1:4])

"""
Output:

['SQL', 'AWS', 'Docker']

Start Included
End Excluded
"""

# ------------------------------------------------

"""
================================================
10. EMPTY LIST
================================================
"""

employees = []

print(employees)

"""
Output:

[]
"""

# ------------------------------------------------

"""
================================================
11. NESTED LIST
================================================
"""

matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]

print(matrix)

"""
Output:

[[1,2,3],[4,5,6],[7,8,9]]
"""

# ------------------------------------------------

"""
================================================
12. ACCESS NESTED LIST
================================================
"""

matrix = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]

]

print(matrix[0][0])

"""
Output:

1
"""

# ------------------------------------------------

"""
================================================
13. SUM OF LIST ELEMENTS
================================================
"""

numbers = [10, 20, 30, 40]

total = 0

for num in numbers:

    total += num

print(total)

"""
Output:

100
"""

# ------------------------------------------------

"""
================================================
14. FIND MAXIMUM ELEMENT
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
15. FIND MINIMUM ELEMENT
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
INTERVIEW QUESTIONS
================================================

Q1. What is a List?

Answer: A list is an ordered, mutable collection
used to store multiple values.

------------------------------------------------

Q2. Are Lists Mutable?

Answer: Yes.

Elements can be modified after creation.

------------------------------------------------

Q3. Does List Allow Duplicates?

Answer: Yes.

Example: [1,1,2,2,3]

------------------------------------------------

Q4. Does List Maintain Order?

Answer: Yes.

------------------------------------------------

Q5. What is Indexing?

Answer: Accessing elements using position.

Example: skills[0]

------------------------------------------------

Q6. What is Negative Indexing?

Answer: Accessing elements from the end.

Example: skills[-1]

------------------------------------------------

Q7. How do you find List Length?

Answer: len(list_name)

------------------------------------------------

Q8. Can Lists store different
data types?

Answer: Yes.

Example: ["Alex", 25, True]
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Create a list of 5 skills.

2. Print first element.

3. Print last element.

4. Find length of list.

5. Modify second element.

6. Check if Python exists in list.

7. Find sum of all numbers.

8. Find maximum element.

9. Find minimum element.

10. Reverse a list.

11. Create a nested list.

12. Access nested list element.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Concepts:

1. List
2. Indexing
3. Negative Indexing
4. Mutable
5. Ordered
6. Duplicates Allowed
7. Slicing
8. Nested Lists

Lists are used heavily in:

Python Programming
DSA
Backend Development
APIs
Data Processing
Machine Learning
"""