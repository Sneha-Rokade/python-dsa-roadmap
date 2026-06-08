"""
================================================
DICTIONARY ITERATION IN PYTHON
================================================

What is Dictionary Iteration?

Dictionary iteration means traversing
through keys, values, or key-value pairs.

Why Important?

Most API responses, JSON objects,
and database records are dictionaries.

Backend developers use dictionary
iteration daily.

================================================
1. ITERATE THROUGH KEYS
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

for key in employee:

    print(key)

"""
Output:
name
age
role
"""

# ------------------------------------------------

"""
================================================
2. ITERATE USING keys()
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

for key in employee.keys():
    print(key)

"""
Output:
name
age
role
"""

# ------------------------------------------------

"""
================================================
3. ITERATE THROUGH VALUES
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

for value in employee.values():
    print(value)

"""
Output:
Alex
25
Engineer
"""

# ------------------------------------------------

"""
================================================
4. ITERATE THROUGH ITEMS
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

for item in employee.items():
    print(item)

"""
Output:
('name', 'Alex')
('age', 25)
('role', 'Engineer')
"""

# ------------------------------------------------

"""
================================================
5. ITERATE THROUGH KEY-VALUE PAIRS
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

for key, value in employee.items():

    print(key, ":", value)

"""
Output:
name : Alex
age : 25
role : Engineer
"""

# ------------------------------------------------

"""
================================================
6. USING F-STRINGS
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

for key, value in employee.items():
    print(f"{key} -> {value}")

"""
Output:
name -> Alex
age -> 25
role -> Engineer
"""

# ------------------------------------------------

"""
================================================
7. COUNT TOTAL KEYS
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer",
    "city": "Pune"
}

count = 0

for key in employee:

    count += 1

print(count)

"""
Output:

4
"""

# ------------------------------------------------

"""
================================================
8. CHECK IF KEY EXISTS
================================================
"""

employee = {
    "name": "Alex",
    "age": 25
}
for key in employee:

    if key == "name":

        print("Found")

"""
Output: Found
"""

# ------------------------------------------------

"""
================================================
9. PRINT ONLY VALUES GREATER THAN 50
================================================
"""

marks = {
    "Math": 85,
    "Science": 45,
    "English": 75,
    "History": 40
}

for value in marks.values():

    if value > 50:

        print(value)

"""
Output:
85
75
"""

# ------------------------------------------------

"""
================================================
10. PRINT SUBJECTS WITH MARKS > 50
================================================
"""

marks = {
    "Math": 85,
    "Science": 45,
    "English": 75,
    "History": 40
}

for subject, score in marks.items():

    if score > 50:

        print(subject)

"""
Output:
Math
English
"""

# ------------------------------------------------

"""
================================================
11. NESTED DICTIONARY ITERATION
================================================
"""

employee = {
    "name": "Alex",
    "details": {
        "city": "Pune",
        "role": "Engineer"
    }
}

for key, value in employee["details"].items():

    print(key, value)

"""
Output:
city Pune
role Engineer
"""

# ------------------------------------------------

"""
================================================
12. LIST OF DICTIONARIES
================================================
"""

employees = [
    {
        "id": 1,
        "name": "Alex"
    },
    {
        "id": 2,
        "name": "John"
    },
    {
        "id": 3,
        "name": "Emma"
    }
]

for employee in employees:

    print(employee["name"])

"""
Output:
Alex
John
Emma
"""

# ------------------------------------------------

"""
================================================
13. PRINT COMPLETE EMPLOYEE DETAILS
================================================
"""

employees = [
    {
        "id": 1,
        "name": "Alex"
    },
    {
        "id": 2,
        "name": "John"
    }
]

for employee in employees:

    for key, value in employee.items():

        print(key, value)

    print()

"""
Output:
id 1
name Alex

id 2
name John
"""

# ------------------------------------------------

"""
================================================
14. REAL WORLD EXAMPLE
================================================

API Response Processing
"""

response = {
    "id": 101,
    "name": "Alex",
    "email": "alex@gmail.com",
    "active": True
}

for key, value in response.items():

    print(f"{key}: {value}")

"""
Output:
id: 101
name: Alex
email: alex@gmail.com
active: True
"""

# ------------------------------------------------

"""
================================================
15. REAL WORLD EXAMPLE
================================================

Student Marks Report
"""

marks = {
    "Math": 80,
    "Science": 90,
    "English": 85
}

for subject, score in marks.items():

    print(f"{subject}: {score}")

"""
Output:
Math: 80
Science: 90
English: 85
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. How do you iterate through keys?

Answer: for key in dictionary:
or
for key in dictionary.keys()

------------------------------------------------

Q2. How do you iterate through values?

Answer: for value in dictionary.values()

------------------------------------------------

Q3. How do you iterate through
key-value pairs?

Answer: for key, value in dictionary.items()

------------------------------------------------

Q4. What does items() return?

Answer: Key-value pairs.

------------------------------------------------

Q5. What does keys() return?

Answer: All dictionary keys.

------------------------------------------------

Q6. What does values() return?

Answer: All dictionary values.

------------------------------------------------

Q7. Why is dictionary iteration important?

Answer:
Used in APIs,
JSON processing,
Backend development,
Data analysis.

------------------------------------------------

Q8. How do you iterate through
nested dictionaries?

Answer: Use loops on inner dictionaries.

Example: employee["details"].items()
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Print all keys.

2. Print all values.

3. Print all key-value pairs.

4. Count total keys.

5. Find if a key exists.

6. Print marks greater than 60.

7. Print subject names with marks > 60.

8. Iterate through nested dictionary.

9. Print employee names from
   list of dictionaries.

10. Print complete employee details.

11. Process API response dictionary.

12. Create student report generator.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Methods:

keys()
values()
items()

Common Patterns:

for key in dictionary

for value in dictionary.values()

for key, value in dictionary.items()

Used In:

REST APIs
FastAPI
Django
Flask
JSON Processing
Database Records
Backend Development

Interview Favorite:

keys()
values()
items()

Difference Between Them
"""