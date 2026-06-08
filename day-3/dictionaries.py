"""
================================================
DICTIONARIES IN PYTHON
================================================

What is a Dictionary?

A dictionary stores data in
key-value pairs.

Example:

{
    "name": "Alex",
    "age": 25
}

Why Dictionaries?

Dictionaries help store structured
data efficiently.

Used heavily in:

- APIs
- JSON
- Backend Development
- Database Records
- Configuration Files

================================================
CHARACTERISTICS OF DICTIONARY
================================================

1. Key-Value Pairs
2. Mutable
3. Ordered (Python 3.7+)
4. Keys Must Be Unique
5. Values Can Repeat

================================================
1. CREATE A DICTIONARY
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

print(employee)

"""
Output:

{
    'name': 'Alex',
    'age': 25,
    'role': 'Engineer'
}
"""

# ------------------------------------------------

"""
================================================
2. ACCESS VALUES
================================================
"""
employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

print(employee["name"])
print(employee["role"])

"""
Output:
Alex
Engineer
"""

# ------------------------------------------------

"""
================================================
3. MODIFY VALUE
================================================
"""

employee = {
    "name": "Alex",
    "age": 25
}

employee["age"] = 26

print(employee)

"""
Output:
{
    'name': 'Alex',
    'age': 26
}
"""

# ------------------------------------------------

"""
================================================
4. ADD NEW KEY
================================================
"""

employee = {
    "name": "Alex",
    "age": 25
}

employee["city"] = "Mumbai"

print(employee)

"""
Output:
{
    'name': 'Alex',
    'age': 25,
    'city': 'Mumbai'
}
"""

# ------------------------------------------------

"""
================================================
5. DELETE KEY
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "city": "Mumbai"
}

del employee["city"]

print(employee)

"""
Output:
{
    'name': 'Alex',
    'age': 25
}
"""

# ------------------------------------------------

"""
================================================
6. GET METHOD
================================================

Safer than direct access.
"""

employee = {
    "name": "Alex",
    "age": 25
}

print(employee.get("name"))

"""
Output: Alex
"""

print(employee.get("salary"))

"""
Output: None

No error occurs.
"""

# ------------------------------------------------

"""
================================================
7. KEYS()
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

print(employee.keys())

"""
Output: dict_keys(['name', 'age', 'role'])
"""

# ------------------------------------------------

"""
================================================
8. VALUES()
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

print(employee.values())

"""
Output: dict_values(['Alex', 25, 'Engineer'])
"""

# ------------------------------------------------

"""
================================================
9. ITEMS()
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

print(employee.items())

"""
Output: dict_items([
    ('name', 'Alex'),
    ('age', 25),
    ('role', 'Engineer')
])
"""

# ------------------------------------------------

"""
================================================
10. LOOP THROUGH KEYS
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
11. LOOP THROUGH VALUES
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
12. LOOP THROUGH KEY VALUE PAIRS
================================================
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

for key, value in employee.items():

    print(key, value)

"""
Output:
name Alex
age 25
role Engineer
"""

# ------------------------------------------------

"""
================================================
13. POP()
================================================

Removes specified key.
"""

employee = {
    "name": "Alex",
    "age": 25,
    "role": "Engineer"
}

employee.pop("role")

print(employee)

"""
Output:
{
    'name': 'Alex',
    'age': 25
}
"""

# ------------------------------------------------

"""
================================================
14. UPDATE()
================================================

Updates dictionary values.
"""

employee = {
    "name": "Alex",
    "age": 25
}

employee.update({
    "age": 26,
    "city": "Pune"
})

print(employee)

"""
Output:
{
    'name': 'Alex',
    'age': 26,
    'city': 'Pune'
}
"""

# ------------------------------------------------

"""
================================================
15. NESTED DICTIONARY
================================================
"""

employee = {
    "name": "Alex",
    "details": {
        "city": "Pune",
        "role": "Engineer"
    }
}

print(employee["details"]["role"])

"""
Output: Engineer
"""

# ------------------------------------------------

"""
================================================
16. REAL WORLD API RESPONSE
================================================
"""

response = {
    "id": 101,
    "name": "Alex",
    "email": "alex@gmail.com",
    "active": True
}

print(response["email"])

"""
Output: alex@gmail.com
"""

# ------------------------------------------------

"""
================================================
LIST OF DICTIONARIES
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

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is a Dictionary?

Answer: A collection of key-value pairs.

------------------------------------------------

Q2. Are Dictionaries Mutable?

Answer: Yes.
Values can be modified.

------------------------------------------------

Q3. Can Keys Repeat?

Answer: No.
Keys must be unique.

------------------------------------------------

Q4. Can Values Repeat?

Answer: Yes.

------------------------------------------------

Q5. Difference Between
dict["key"] and get()?

Answer: dict["key"]
Raises error if key not found.

get()
Returns None.

------------------------------------------------

Q6. What does keys() return?

Answer: All keys.

------------------------------------------------

Q7. What does values() return?

Answer: All values.

------------------------------------------------

Q8. What does items() return?

Answer: Key-value pairs.

------------------------------------------------

Q9. What is a Nested Dictionary?

Answer: Dictionary inside another dictionary.

------------------------------------------------

Q10. Where are Dictionaries Used?

Answer:
APIs
JSON
Backend Development
Database Records
Configuration Files
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Create employee dictionary.

2. Print employee name.

3. Update age.

4. Add city key.

5. Delete role key.

6. Print all keys.

7. Print all values.

8. Loop through dictionary.

9. Create nested dictionary.

10. Access nested value.

11. Create list of dictionaries.

12. Print employee names.

13. Update multiple values.

14. Use get() safely.

15. Remove key using pop().
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

Important Concepts:

1. Dictionary
2. Key-Value Pair
3. Mutable
4. keys()
5. values()
6. items()
7. get()
8. pop()
9. update()
10. Nested Dictionary

Most Important Python
Data Structure for:

REST APIs
FastAPI
Django
Flask
JSON Processing
Backend Development
Database Results
Cloud Applications
"""