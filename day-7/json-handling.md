# JSON HANDLING IN PYTHON

## What is JSON?

JSON stands for: JavaScript Object Notation
JSON is the most common format used for data exchange between applications.

Example:
{
    "name": "Alex",
    "age": 25,
    "city": "Mumbai"
}

# Why JSON is Important?

JSON is used everywhere:

* REST APIs
* Django REST Framework
* Frontend ↔ Backend Communication
* Mobile Applications
* Microservices
* Configuration Files

# JSON VS PYTHON DICTIONARY

JSON:
{
    "name": "Alex",
    "age": 25
}

Python Dictionary:
{
    "name": "Alex",
    "age": 25
}

Looks similar.

Main difference:

JSON is text.
Dictionary is a Python object.

# JSON MODULE

Python provides: import json
No installation required.

# PYTHON DICTIONARY TO JSON

Convert Python object into JSON.

Example: import json

student = {
    "name": "Alex",
    "age": 25
}

json_data = json.dumps(
    student
)

print(json_data)

Output: {"name": "Alex", "age": 25}

# UNDERSTANDING dumps()

json.dumps()

Means: Dictionary → JSON String

# CHECK DATA TYPE

Example:
import json

student = {
    "name": "Alex"
}

json_data = json.dumps(
    student
)

print(type(json_data))

Output: <class 'str'>

JSON becomes string.

# JSON TO PYTHON DICTIONARY

Example:
import json

json_data = '''
{
    "name": "Alex",
    "age": 25
}

student = json.loads(
    json_data
)

print(student)

Output:
{
    'name': 'Alex',
    'age': 25
}

# UNDERSTANDING loads()
json.loads()

Means: JSON String → Python Object

# CHECK TYPE
import json

json_data = '''
{
    "name": "Alex"
}

data = json.loads(
    json_data
)

print(type(data))

Output: <class 'dict'>

# PRETTY PRINT JSON

Example:

import json
student = {
    "name": "Alex",
    "age": 25,
    "city": "Mumbai"
}

print(
    json.dumps(
        student,
        indent=4
    )
)

Output:
{
    "name": "Alex",
    "age": 25,
    "city": "Mumbai"
}

# SORT JSON KEYS

Example:
import json

data = {
    "z": 1,
    "a": 2,
    "m": 3
}

print(
    json.dumps(
        data,
        indent=4,
        sort_keys=True
    )
)

Output:

{
    "a": 2,
    "m": 3,
    "z": 1
}

# WRITING JSON FILE

Example:
import json

student = {
    "name": "Alex",
    "age": 25
}

with open(
    "student.json",
    "w"
) as file:
    json.dump(
        student,
        file,
        indent=4
    )

Generated File:
{
    "name": "Alex",
    "age": 25
}

# UNDERSTANDING dump()
json.dump()

Means: Write JSON To File

# READING JSON FILE

Example:
import json

with open(
    "student.json",
    "r"
) as file:
    data = json.load(
        file
    )

print(data)

Output:
{
    'name': 'Alex',
    'age': 25
}

# UNDERSTANDING load()
json.load()

Means: Read JSON File

# JSON DATA TYPES

JSON Supports:
String
Number
Boolean
Array
Object
Null

Example:

{
    "name": "Alex",
    "age": 25,
    "is_active": true,
    "skills": [
        "Python",
        "Django"
    ]
}

# NESTED JSON

Example:
{
    "user": {
        "name": "Alex",
        "age": 25
    }
}

Access: data["user"]["name"]

Output: Alex

# JSON ARRAY

Example:
[
    {
        "name": "Alex"
    },
    {
        "name": "John"
    }
]

Access: data[0]["name"]

Output: Alex

# REAL WORLD API RESPONSE

Most APIs return:
{
    "id": 1,
    "name": "Alex",
    "email": "alex@gmail.com"
}

Python: response.json()

returns: dict

# DJANGO REST FRAMEWORK EXAMPLE

API Response:
return Response({
    "name": "Alex",
    "age": 25
})

Output:
{
    "name": "Alex",
    "age": 25
}

JSON is the standard format.

# SAVING API DATA

Example:
import json
api_response = {
    "name": "Alex",
    "city": "Mumbai"
}

with open(
    "response.json",
    "w"
) as file:

    json.dump(
        api_response,
        file
    )

# CONVERTING LIST TO JSON

Example:
import json

users = [
    "Alex",
    "John",
    "Emma"
]

print(
    json.dumps(
        users
    )
)

Output:
[
    "Alex",
    "John",
    "Emma"
]

# JSON ERROR HANDLING

Bad JSON:
import json

data = '''
{
    name: Alex
}

json.loads(data)

Output: JSONDecodeError

Handle Exception:

import json

try:
    json.loads(data)
except json.JSONDecodeError:
    print("Invalid JSON")

# COMMON MISTAKES

## Using Single Quotes

Bad JSON:
{
    'name': 'Alex'
}

Good JSON:
{
    "name": "Alex"
}

JSON requires double quotes.

# dump vs dumps

### dump

Writes to file.

json.dump()

### dumps

Returns JSON string.
json.dumps()

# load vs loads

### load

Reads JSON file.

json.load()

### loads

Reads JSON string.
json.loads()

# INTERVIEW QUESTIONS

### Q1. What is JSON?

Answer: JavaScript Object Notation used for data exchange.

### Q2. Which Module Handles JSON?

Answer: json

### Q3. What Does dumps() Do?

Answer: Converts Python object into JSON string.

### Q4. What Does loads() Do?

Answer: Converts JSON string into Python object.

### Q5. Difference Between dump and dumps?

Answer: dump write a file
dumps return a json string

### Q6. Difference Between load and loads?

Answer:load write a file
loads → string


### Q7. Which Data Type Does JSON Become in Python?

Answer: Usually dictionary.

### Q8. Why Is JSON Important?

Answer: Used in APIs and web applications.

### Q9. Can JSON Store Lists?

Answer: Yes.
Using arrays.

### Q10. Django Use Case?

Answer: API request and response handling.

# PRACTICE QUESTIONS

1. Convert dictionary to JSON.
2. Convert JSON to dictionary.
3. Write JSON file.
4. Read JSON file.
5. Pretty print JSON.
6. Sort JSON keys.
7. Handle JSONDecodeError.
8. Create nested JSON.
9. Convert list to JSON.
10. Build student management JSON file.

# SUMMARY

Important Functions:

* json.dump()
* json.dumps()
* json.load()
* json.loads()

Used In:

* Django
* REST APIs
* Frontend Development
* Mobile Apps
* Microservices

JSON is one of the most important technologies for backend developers because nearly all modern applications exchange data using JSON.
