"""
================================================
LIST METHODS IN PYTHON
================================================

What are List Methods?

List methods are built-in functions
used to perform operations on lists.

Why Important?

Lists are one of the most used
data structures in Python.

================================================
1. APPEND()
================================================

Adds element at the end of list.
"""

skills = ["Python", "SQL"]

skills.append("AWS")

print(skills)

"""
Output:

['Python', 'SQL', 'AWS']
"""

# ------------------------------------------------

"""
================================================
2. INSERT()
================================================

Adds element at a specific position.
"""

skills = ["Python", "SQL"]

skills.insert(1, "Docker")

print(skills)

"""
Output:

['Python', 'Docker', 'SQL']
"""

# ------------------------------------------------

"""
================================================
3. REMOVE()
================================================

Removes specific value.
"""

skills = ["Python", "SQL", "AWS"]

skills.remove("SQL")

print(skills)

"""
Output:

['Python', 'AWS']
"""

# ------------------------------------------------

"""
================================================
4. POP()
================================================

Removes element using index.

Default:
Removes last element.
"""

skills = ["Python", "SQL", "AWS"]

skills.pop()

print(skills)

"""
Output:

['Python', 'SQL']
"""

# ------------------------------------------------

"""
POP WITH INDEX
================================================
"""

skills = ["Python", "SQL", "AWS"]

skills.pop(1)

print(skills)

"""
Output:

['Python', 'AWS']
"""

# ------------------------------------------------

"""
================================================
5. CLEAR()
================================================

Removes all elements.
"""

skills = ["Python", "SQL", "AWS"]

skills.clear()

print(skills)

"""
Output:

[]
"""

# ------------------------------------------------

"""
================================================
6. SORT()
================================================

Sorts list in ascending order.
"""

numbers = [40, 10, 80, 20]

numbers.sort()

print(numbers)

"""
Output:

[10, 20, 40, 80]
"""

# ------------------------------------------------

"""
================================================
7. SORT DESCENDING
================================================
"""

numbers = [40, 10, 80, 20]

numbers.sort(reverse=True)

print(numbers)

"""
Output:

[80, 40, 20, 10]
"""

# ------------------------------------------------

"""
================================================
8. REVERSE()
================================================

Reverses list order.
"""

skills = ["Python", "SQL", "AWS"]

skills.reverse()

print(skills)

"""
Output:

['AWS', 'SQL', 'Python']
"""

# ------------------------------------------------

"""
================================================
9. COUNT()
================================================

Counts occurrences of value.
"""

numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))

"""
Output:

3
"""

# ------------------------------------------------

"""
================================================
10. INDEX()
================================================

Returns position of value.
"""

skills = ["Python", "SQL", "AWS"]

print(skills.index("SQL"))

"""
Output:

1
"""

# ------------------------------------------------

"""
================================================
11. COPY()
================================================

Creates copy of list.
"""

skills = ["Python", "SQL", "AWS"]

new_skills = skills.copy()

print(new_skills)

"""
Output:

['Python', 'SQL', 'AWS']
"""

# ------------------------------------------------

"""
================================================
12. EXTEND()
================================================

Adds elements from another list.
"""

skills = ["Python", "SQL"]

more_skills = ["AWS", "Docker"]

skills.extend(more_skills)

print(skills)

"""
Output:

['Python', 'SQL', 'AWS', 'Docker']
"""

# ------------------------------------------------

"""
================================================
13. APPEND VS EXTEND
================================================
"""

skills = ["Python", "SQL"]

skills.append(["AWS", "Docker"])

print(skills)

"""
Output:

['Python', 'SQL', ['AWS', 'Docker']]

append() adds entire list as one element.
"""

# ------------------------------------------------

skills = ["Python", "SQL"]

skills.extend(["AWS", "Docker"])

print(skills)

"""
Output:

['Python', 'SQL', 'AWS', 'Docker']

extend() adds individual elements.
"""

# ------------------------------------------------

"""
================================================
14. REAL WORLD EXAMPLE
================================================

Employee Skills Tracker
"""

employee_skills = ["Python", "SQL"]

employee_skills.append("AWS")
employee_skills.append("Docker")

print(employee_skills)

"""
Output:

['Python', 'SQL', 'AWS', 'Docker']
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What does append() do?

Answer: Adds element at end of list.

------------------------------------------------

Q2. Difference between append()
and insert()?

Answer: append()
Adds at end.

insert()
Adds at specific position.

------------------------------------------------

Q3. Difference between remove()
and pop()?

Answer: remove()
Removes by value.

pop()
Removes by index.

------------------------------------------------

Q4. What does sort() do?

Answer: Sorts elements in ascending order.

------------------------------------------------

Q5. What does reverse() do?

Answer: Reverses list order.

------------------------------------------------

Q6. What does count() do?

Answer: Counts occurrences of value.

------------------------------------------------

Q7. What does index() do?

Answer: Returns position of value.

------------------------------------------------

Q8. Difference between append()
and extend()?

Answer: append()
Adds entire object.

extend()
Adds individual elements.

------------------------------------------------

Q9. What does clear() do?

Answer: Removes all elements from list.

------------------------------------------------

Q10. What does copy() do?

Answer: Creates a duplicate list.
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Create a list of skills.

2. Add AWS using append().

3. Insert Docker at position 1.

4. Remove SQL.

5. Remove last element using pop().

6. Sort numbers.

7. Reverse list.

8. Count occurrences of 20.

9. Find index of AWS.

10. Create copy of list.

11. Merge two lists using extend().

12. Empty a list using clear().
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important List Methods:

append()
insert()
remove()
pop()
clear()
sort()
reverse()
count()
index()
copy()
"""