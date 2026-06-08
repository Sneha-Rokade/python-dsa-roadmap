"""
================================================
NESTED DATA STRUCTURES IN PYTHON
================================================

What are Nested Data Structures?

When one data structure is placed
inside another data structure.

Examples:
List inside List
Dictionary inside Dictionary
List inside Dictionary
Dictionary inside List

Why Important?

Real-world applications use nested
data structures everywhere.

Examples:
- REST APIs
- JSON Responses
- MongoDB Documents
- Configuration Files
- Cloud Applications

================================================
1. NESTED LIST
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
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
"""

# ------------------------------------------------

"""
================================================
2. ACCESS NESTED LIST ELEMENT
================================================
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])

"""
Output: 1
"""

print(matrix[2][1])

"""
Output: 8
"""

# ------------------------------------------------

"""
================================================
3. ITERATE NESTED LIST
================================================
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    for value in row:

        print(value)

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
"""

# ------------------------------------------------

"""
================================================
4. DICTIONARY INSIDE DICTIONARY
================================================
"""

employee = {
    "name": "Alex",
    "details": {
        "age": 25,
        "city": "Pune",
        "role": "Engineer"
    }
}

print(employee)

# ------------------------------------------------

"""
================================================
5. ACCESS NESTED DICTIONARY
================================================
"""

employee = {
    "name": "Alex",
    "details": {
        "age": 25,
        "city": "Pune",
        "role": "Engineer"
    }
}

print(employee["details"]["city"])

"""
Output: Pune
"""

# ------------------------------------------------

"""
================================================
6. ITERATE NESTED DICTIONARY
================================================
"""

employee = {
    "name": "Alex",
    "details": {
        "age": 25,
        "city": "Pune",
        "role": "Engineer"
    }
}

for key, value in employee["details"].items():

    print(key, value)

"""
Output:
age 25
city Pune
role Engineer
"""

# ------------------------------------------------

"""
================================================
7. LIST OF DICTIONARIES
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

print(employees)

# ------------------------------------------------

"""
================================================
8. ACCESS LIST OF DICTIONARIES
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

print(employees[0]["name"])

"""
Output: Alex
"""

print(employees[1]["name"])

"""
Output: John
"""

# ------------------------------------------------

"""
================================================
9. ITERATE LIST OF DICTIONARIES
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
10. DICTIONARY WITH LIST
================================================
"""

employee = {
    "name": "Alex",
    "skills": [
        "Python",
        "SQL",
        "AWS"
    ]
}

print(employee)

# ------------------------------------------------

"""
================================================
11. ACCESS LIST INSIDE DICTIONARY
================================================
"""

employee = {
    "name": "Alex",
    "skills": [
        "Python",
        "SQL",
        "AWS"
    ]
}

print(employee["skills"][0])

"""
Output: Python
"""

# ------------------------------------------------

"""
================================================
12. ITERATE LIST INSIDE DICTIONARY
================================================
"""

employee = {
    "name": "Alex",
    "skills": [
        "Python",
        "SQL",
        "AWS"
    ]
}

for skill in employee["skills"]:

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
13. REAL WORLD API RESPONSE
================================================
"""

response = {
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "Alex"
        },
        {
            "id": 2,
            "name": "John"
        }
    ]
}

print(response["data"][0]["name"])

"""
Output: Alex
"""

# ------------------------------------------------

"""
================================================
14. ITERATE API RESPONSE
================================================
"""

response = {
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "Alex"
        },
        {
            "id": 2,
            "name": "John"
        }
    ]
}

for user in response["data"]:

    print(user["name"])

"""
Output:
Alex
John
"""

# ------------------------------------------------

"""
================================================
15. MONGODB STYLE DOCUMENT
================================================
"""

user = {
    "_id": 101,
    "name": "Alex",
    "contact": {
        "email": "alex@gmail.com",
        "phone": "9876543210"
    },
    "skills": [
        "Python",
        "AWS",
        "Docker"
    ]
}

print(user["contact"]["email"])

"""
Output: alex@gmail.com
"""

print(user["skills"][1])

"""
Output: AWS
"""

# ------------------------------------------------

"""
================================================
16. COMPLEX NESTED STRUCTURE
================================================
"""

company = {
    "name": "TechCorp",
    "employees": [
        {
            "id": 1,
            "name": "Alex",
            "skills": [
                "Python",
                "AWS"
            ]
        },
        {
            "id": 2,
            "name": "John",
            "skills": [
                "Java",
                "Docker"
            ]
        }
    ]
}

print(company["employees"][0]["skills"][1])

"""
Output: AWS
"""

# ------------------------------------------------

"""
================================================
17. ITERATE COMPLEX STRUCTURE
================================================
"""

company = {
    "employees": [
        {
            "name": "Alex",
            "skills": [
                "Python",
                "AWS"
            ]
        },
        {
            "name": "John",
            "skills": [
                "Java",
                "Docker"
            ]
        }
    ]
}

for employee in company["employees"]:

    print(employee["name"])

    for skill in employee["skills"]:

        print(skill)

"""
Output:
Alex
Python
AWS

John
Java
Docker
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What are Nested Data Structures?

Answer: A data structure inside another
data structure.

------------------------------------------------

Q2. What is a List of Dictionaries?

Answer: A list containing multiple dictionaries.

------------------------------------------------

Q3. How do APIs usually return data?

Answer: Using nested dictionaries and lists.

------------------------------------------------

Q4. How do you access nested values?

Answer: Use multiple indexes and keys.

Example: employee["details"]["city"]

------------------------------------------------

Q5. How do you access a list inside
a dictionary?

Answer: employee["skills"][0]

------------------------------------------------

Q6. Why are nested structures important?

Used in:
APIs
JSON
MongoDB
Backend Development
Cloud Applications

------------------------------------------------

Q7. What is JSON?

Answer: JavaScript Object Notation.
Data exchange format.
Looks very similar to Python dictionaries.
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Create a nested list.

2. Access nested list values.

3. Create dictionary inside dictionary.

4. Access nested dictionary values.

5. Create list of dictionaries.

6. Print employee names.

7. Create dictionary with skills list.

8. Print all skills.

9. Create API response structure.

10. Extract user names.

11. Create MongoDB-style document.

12. Access email and phone.

13. Create company employee structure.

14. Print all employee skills.

15. Build student management structure.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Structures:

List inside List

Dictionary inside Dictionary

List inside Dictionary

Dictionary inside List
"""