# JSON HANDLING IN PYTHON

## What is JSON?

JSON stands for:

```text id="ahc0qv"
JavaScript Object Notation
```

JSON is the most common format used for data exchange between applications.

Example:

```json id="i8w6gq"
{
    "name": "Alex",
    "age": 25,
    "city": "Mumbai"
}
```

---

# Why JSON is Important?

JSON is used everywhere:

* REST APIs
* Django REST Framework
* Frontend ↔ Backend Communication
* Mobile Applications
* Microservices
* Configuration Files

If you become a backend developer, you will work with JSON every day.

---

# JSON VS PYTHON DICTIONARY

JSON:

```json id="axjzj0"
{
    "name": "Alex",
    "age": 25
}
```

Python Dictionary:

```python id="4d40nz"
{
    "name": "Alex",
    "age": 25
}
```

Looks similar.

Main difference:

JSON is text.

Dictionary is a Python object.

---

# JSON MODULE

Python provides:

```python id="tz2mfr"
import json
```

No installation required.

---

# PYTHON DICTIONARY TO JSON

Convert Python object into JSON.

Example:

```python id="f8grq9"
import json

student = {

    "name": "Alex",

    "age": 25
}

json_data = json.dumps(
    student
)

print(json_data)
```

Output:

```json id="p5d50x"
{"name": "Alex", "age": 25}
```

---

# UNDERSTANDING dumps()

```python id="izutcz"
json.dumps()
```

Means:

```text id="jh31ij"
Dictionary → JSON String
```

Important interview question.

---

# CHECK DATA TYPE

Example:

```python id="hj2rb8"
import json

student = {

    "name": "Alex"
}

json_data = json.dumps(
    student
)

print(type(json_data))
```

Output:

```text id="6zhkfd"
<class 'str'>
```

JSON becomes string.

---

# JSON TO PYTHON DICTIONARY

Example:

```python id="gmk2h4"
import json

json_data = '''

{

    "name": "Alex",

    "age": 25

}
'''

student = json.loads(
    json_data
)

print(student)
```

Output:

```python id="n6o4ml"
{
    'name': 'Alex',
    'age': 25
}
```

---

# UNDERSTANDING loads()

```python id="1cr40g"
json.loads()
```

Means:

```text id="gcrjlwm"
JSON String → Python Object
```

Very important interview question.

---

# CHECK TYPE

```python id="1g0rk0"
import json

json_data = '''

{

    "name": "Alex"

}
'''

data = json.loads(
    json_data
)

print(type(data))
```

Output:

```text id="2uked8"
<class 'dict'>
```

---

# PRETTY PRINT JSON

Example:

```python id="u5m2wv"
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
```

Output:

```json id="w9o2v5"
{
    "name": "Alex",
    "age": 25,
    "city": "Mumbai"
}
```

Much more readable.

---

# SORT JSON KEYS

Example:

```python id="drg6jc"
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
```

Output:

```json id="8m0d61"
{
    "a": 2,
    "m": 3,
    "z": 1
}
```

---

# WRITING JSON FILE

Example:

```python id="8fd47m"
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
```

Generated File:

```json id="f1g0s3"
{
    "name": "Alex",
    "age": 25
}
```

---

# UNDERSTANDING dump()

```python id="9xwwpb"
json.dump()
```

Means:

```text id="2yv4ps"
Write JSON To File
```

---

# READING JSON FILE

Example:

```python id="gjr18d"
import json

with open(

    "student.json",

    "r"

) as file:

    data = json.load(
        file
    )

print(data)
```

Output:

```python id="6s8z63"
{
    'name': 'Alex',
    'age': 25
}
```

---

# UNDERSTANDING load()

```python id="b72w8m"
json.load()
```

Means:

```text id="qq61nz"
Read JSON File
```

---

# JSON DATA TYPES

JSON Supports:

```json id="l2lsp4"
String
Number
Boolean
Array
Object
Null
```

---

Example:

```json id="b4lx4m"
{
    "name": "Alex",
    "age": 25,
    "is_active": true,
    "skills": [
        "Python",
        "Django"
    ]
}
```

---

# NESTED JSON

Example:

```json id="jzbsy6"
{
    "user": {
        "name": "Alex",
        "age": 25
    }
}
```

---

Access:

```python id="m5l5lq"
data["user"]["name"]
```

Output:

```text id="79p0hs"
Alex
```

---

# JSON ARRAY

Example:

```json id="fq5pmr"
[
    {
        "name": "Alex"
    },

    {
        "name": "John"
    }
]
```

---

Access:

```python id="yrglkr"
data[0]["name"]
```

Output:

```text id="y8ntx6"
Alex
```

---

# REAL WORLD API RESPONSE

Most APIs return:

```json id="f4u70d"
{
    "id": 1,
    "name": "Alex",
    "email": "alex@gmail.com"
}
```

Python:

```python id="jlwmg1"
response.json()
```

returns:

```python id="smb5to"
dict
```

---

# DJANGO REST FRAMEWORK EXAMPLE

API Response:

```python id="9a3o0x"
return Response({

    "name": "Alex",

    "age": 25
})
```

Output:

```json id="ej91j2"
{
    "name": "Alex",
    "age": 25
}
```

JSON is the standard format.

---

# SAVING API DATA

Example:

```python id="o4kn5j"
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
```

---

# CONVERTING LIST TO JSON

Example:

```python id="0we1mb"
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
```

Output:

```json id="qujbxz"
[
    "Alex",
    "John",
    "Emma"
]
```

---

# JSON ERROR HANDLING

Bad JSON:

```python id="r3x0z4"
import json

data = '''

{

    name: Alex

}
'''

json.loads(data)
```

Output:

```text id="mfrp9w"
JSONDecodeError
```

---

Handle Exception:

```python id="dkh2n2"
import json

try:

    json.loads(data)

except json.JSONDecodeError:

    print("Invalid JSON")
```

---

# COMMON MISTAKES

## Using Single Quotes

Bad JSON:

```json id="w26f6c"
{
    'name': 'Alex'
}
```

Good JSON:

```json id="mjlwmq"
{
    "name": "Alex"
}
```

JSON requires double quotes.

---

# dump vs dumps

### dump

Writes to file.

```python id="25vg8i"
json.dump()
```

---

### dumps

Returns JSON string.

```python id="1j2vq0"
json.dumps()
```

---

# load vs loads

### load

Reads JSON file.

```python id="tqvd1l"
json.load()
```

---

### loads

Reads JSON string.

```python id="f3u30r"
json.loads()
```

---

# INTERVIEW QUESTIONS

### Q1. What is JSON?

Answer:

JavaScript Object Notation used for data exchange.

---

### Q2. Which Module Handles JSON?

Answer:

```python id="bgbg5u"
json
```

---

### Q3. What Does dumps() Do?

Answer:

Converts Python object into JSON string.

---

### Q4. What Does loads() Do?

Answer:

Converts JSON string into Python object.

---

### Q5. Difference Between dump and dumps?

Answer:

dump → file

dumps → string

---

### Q6. Difference Between load and loads?

Answer:

load → file

loads → string

---

### Q7. Which Data Type Does JSON Become in Python?

Answer:

Usually dictionary.

---

### Q8. Why Is JSON Important?

Answer:

Used in APIs and web applications.

---

### Q9. Can JSON Store Lists?

Answer:

Yes.

Using arrays.

---

### Q10. Django Use Case?

Answer:

API request and response handling.

---

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

---

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
