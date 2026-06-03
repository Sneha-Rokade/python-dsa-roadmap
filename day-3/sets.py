"""
================================================
SETS IN PYTHON
================================================

What is a Set?

A set is an unordered collection
of unique elements.

Why Use Sets?

1. Remove Duplicates
2. Fast Lookup
3. Mathematical Set Operations

================================================
CHARACTERISTICS OF SET
================================================

1. Unordered
2. Mutable
3. No Duplicate Values
4. No Indexing

================================================
1. CREATE A SET
================================================
"""

numbers = {1, 2, 3, 4, 5}

print(numbers)

"""
Output:

{1, 2, 3, 4, 5}
"""

# ------------------------------------------------

"""
================================================
2. DUPLICATES REMOVED AUTOMATICALLY
================================================
"""

numbers = {1, 2, 2, 3, 3, 4, 4, 5}

print(numbers)

"""
Output:

{1, 2, 3, 4, 5}

Duplicates are removed automatically.
"""

# ------------------------------------------------

"""
================================================
3. SET DOES NOT SUPPORT INDEXING
================================================
"""

skills = {"Python", "SQL", "AWS"}

# print(skills[0])

"""
Error: TypeError

Reason: Sets are unordered and do not
support indexing.
"""

# ------------------------------------------------

"""
================================================
4. ITERATE THROUGH A SET
================================================
"""

skills = {"Python", "SQL", "AWS"}

for skill in skills:

    print(skill)

"""
Output: Order may vary.

Python
AWS
SQL
"""

# ------------------------------------------------

"""
================================================
5. ADD()
================================================

Adds a single element.
"""

skills = {"Python", "SQL"}

skills.add("AWS")

print(skills)

"""
Output: {'Python', 'SQL', 'AWS'}
"""

# ------------------------------------------------

"""
================================================
6. REMOVE()
================================================

Removes an element.

Raises error if element
does not exist.
"""

skills = {"Python", "SQL", "AWS"}

skills.remove("SQL")

print(skills)

"""
Output: {'Python', 'AWS'}
"""

# ------------------------------------------------

"""
================================================
7. DISCARD()
================================================

Removes an element.

Does NOT raise error if
element does not exist.
"""

skills = {"Python", "SQL", "AWS"}

skills.discard("Docker")

print(skills)

"""
Output:

{'Python', 'SQL', 'AWS'}
"""

# ------------------------------------------------

"""
================================================
8. POP()
================================================

Removes a random element.
"""

skills = {"Python", "SQL", "AWS"}

removed = skills.pop()

print(removed)
print(skills)

"""
Output: May vary because sets
are unordered.
"""

# ------------------------------------------------

"""
================================================
9. CLEAR()
================================================

Removes all elements.
"""

skills = {"Python", "SQL", "AWS"}

skills.clear()

print(skills)

"""
Output: set()
"""

# ------------------------------------------------

"""
================================================
10. UNION()
================================================

Combines two sets.
"""

set1 = {1, 2, 3}

set2 = {3, 4, 5}

result = set1.union(set2)

print(result)

"""
Output:

{1, 2, 3, 4, 5}
"""

# ------------------------------------------------

"""
================================================
11. INTERSECTION()
================================================

Common elements.
"""

set1 = {1, 2, 3}

set2 = {2, 3, 4}

result = set1.intersection(set2)

print(result)

"""
Output: {2, 3}
"""

# ------------------------------------------------

"""
================================================
12. DIFFERENCE()
================================================

Elements present in first set
but not in second.
"""

set1 = {1, 2, 3}

set2 = {2, 3, 4}

result = set1.difference(set2)

print(result)

"""
Output: {1}
"""

# ------------------------------------------------

"""
================================================
13. CHECK ELEMENT EXISTS
================================================
"""

skills = {"Python", "SQL", "AWS"}

print("Python" in skills)

"""
Output: True
"""

# ------------------------------------------------

"""
================================================
14. LENGTH OF SET
================================================
"""

skills = {"Python", "SQL", "AWS"}

print(len(skills))

"""
Output: 3
"""

# ------------------------------------------------

"""
================================================
15. CONVERT LIST TO SET
================================================

Common way to remove duplicates.
"""

numbers = [1, 2, 2, 3, 3, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)

"""
Output: {1, 2, 3, 4, 5}
"""

# ------------------------------------------------

"""
================================================
REAL WORLD EXAMPLE
================================================

Remove Duplicate Emails
"""

emails = [

    "alex@gmail.com",
    "john@gmail.com",
    "alex@gmail.com",
    "emma@gmail.com"

]

unique_emails = set(emails)

print(unique_emails)

"""
Duplicates removed.
"""

# ------------------------------------------------

"""
================================================
LIST VS SET
================================================

LIST

Ordered
Allows Duplicates
Supports Indexing

Example: [1, 2, 2, 3]

------------------------------------------------

SET

Unordered
No Duplicates
No Indexing

Example: {1, 2, 3}
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. Does Set Allow Duplicates?

Answer: No.
Duplicates are automatically removed.

------------------------------------------------

Q3. Does Set Support Indexing?

Answer: No.
Sets are unordered.

------------------------------------------------

Q4. Why Use Set?

Answer: To remove duplicates and
perform fast lookups.

------------------------------------------------

Q5. Difference Between remove()
and discard()?

Answer: remove()
Raises error if element
does not exist.

discard()
Does not raise error.

------------------------------------------------

Q6. What is Union?

Answer: Combines all elements
from both sets.

------------------------------------------------

Q7. What is Intersection?

Answer: Returns common elements.

------------------------------------------------

Q8. What is Difference?

Answer: Returns elements present
in first set but not second.

------------------------------------------------

Q9. How do you remove duplicates
from a list?

Answer: Convert list into set.

Example: set(my_list)

------------------------------------------------

Q10. Is Set Mutable?

Answer: Yes.
Elements can be added
or removed.
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Create a set of skills.

2. Add AWS.

3. Remove SQL.

4. Find set length.

5. Check if Python exists.

6. Create two sets and
   perform union.

7. Perform intersection.

8. Perform difference.

9. Remove duplicates
   from a list.

10. Compare List vs Set.

11. Find common skills
    between two employees.

12. Store unique email addresses.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Concepts:

1. Set
2. Unique Values
3. Unordered
4. add()
5. remove()
6. discard()
7. pop()
8. clear()
9. union()
10. intersection()
11. difference()

Most Common Use Cases:

Removing Duplicates
Fast Lookup
Comparing Data
Data Cleaning
DSA Problems
Backend Development
"""