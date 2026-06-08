"""
================================================
STRINGS IN PYTHON
================================================

What is a String?

A string is a sequence of characters enclosed
inside single quotes (' ') or double quotes (" ").

Examples:

"Alex"
'Python'
"Google"

Data Type:
str

================================================
1. CREATING STRINGS
================================================
"""

name = "Alex"
company = 'Google'

print(name)
print(company)

"""
Output:
Alex
Google
"""

# ------------------------------------------------

"""
================================================
2. CHECK STRING DATA TYPE
================================================
"""

language = "Python"

print(type(language))

"""
Output:
<class 'str'>
"""

# ------------------------------------------------

"""
================================================
3. STRING INDEXING
================================================

Each character has an index position.

String:

P  Y  T  H  O  N
0  1  2  3  4  5

Negative Index:

P   Y   T   H   O   N
-6 -5 -4 -3 -2 -1
"""

text = "PYTHON"

print(text[0])
print(text[1])
print(text[5])

"""
Output:
P
Y
N
"""

# ------------------------------------------------

"""
Negative Indexing
"""

print(text[-1])
print(text[-2])

"""
Output:
N
O
"""

# ------------------------------------------------

"""
================================================
4. STRING LENGTH
================================================

len() returns number of characters.
"""

name = "Alex"

print(len(name))

"""
Output:
4
"""

# ------------------------------------------------

"""
================================================
5. STRING CONCATENATION
================================================

Joining strings together.
"""

first_name = "Alex"
last_name = "Smith"

full_name = first_name + " " + last_name

print(full_name)

"""
Output:
Alex Smith
"""

# ------------------------------------------------

"""
================================================
6. STRING REPETITION
================================================
"""

print("Python " * 3)

"""
Output:
Python Python Python
"""

# ------------------------------------------------

"""
================================================
7. STRING SLICING
================================================

Extract part of a string.

Syntax:

string[start:end]
"""

text = "PYTHON"

print(text[0:3])

"""
Output:
PYT
"""

# ------------------------------------------------

print(text[2:5])

"""
Output:
THO
"""

# ------------------------------------------------

print(text[:4])

"""
Output:
PYTH
"""

# ------------------------------------------------

print(text[2:])

"""
Output:
THON
"""

# ------------------------------------------------

"""
================================================
8. COMMON STRING METHODS
================================================
"""

name = "python"

print(name.upper())

"""
Output:
PYTHON
"""

# ------------------------------------------------

name = "PYTHON"

print(name.lower())

"""
Output:
python
"""

# ------------------------------------------------

name = "   Alex   "

print(name.strip())

"""
Output:
Alex
"""

# ------------------------------------------------

language = "Python"

print(language.replace("Python", "Java"))

"""
Output:
Java
"""

# ------------------------------------------------

"""
================================================
9. CHECKING CONTENT
================================================
"""

text = "Python"

print("Py" in text)

"""
Output:
True
"""

# ------------------------------------------------

print("Java" in text)

"""
Output:
False
"""

# ------------------------------------------------

"""
================================================
10. LOOPING THROUGH STRING
================================================
"""

word = "Alex"

for char in word:
    print(char)

"""
Output:
A
l
e
x
"""

# ------------------------------------------------

"""
================================================
11. COUNT VOWELS
================================================
"""

text = "Alex"

count = 0

for char in text:
    if char.lower() in "aeiou":
        count += 1

print(count)

"""
Output:
2
"""

# ------------------------------------------------

"""
================================================
12. REVERSE A STRING
================================================
"""

text = "Python"

reverse = ""

for i in range(len(text)-1, -1, -1):
    reverse += text[i]

print(reverse)

"""
Output:
nohtyP
"""

# ------------------------------------------------

"""
================================================
13. STRINGS ARE IMMUTABLE
================================================

Strings cannot be modified after creation.
"""

name = "Alex"

# name[0] = "B"

"""
This will give an error.

Reason:

Strings are immutable.
"""

# ------------------------------------------------

"""
================================================
REAL WORLD EXAMPLES
================================================

1. Login Validation

username = "admin"

2. Email Verification

email = "alex@gmail.com"

3. Search Feature

product = "Laptop"

4. API Responses

{
   "name": "Alex"
}

Most backend applications work heavily
with strings.
"""

# ------------------------------------------------

"""
================================================
INTERVIEW QUESTIONS
================================================

Q1. What is a String?

Answer:
A string is a sequence of characters
enclosed within quotes.

------------------------------------------------

Q2. What is the data type of a String?

Answer:

str

------------------------------------------------

Q3. Are Strings mutable or immutable?

Answer:

Immutable

------------------------------------------------

Q4. What is indexing?

Answer:

Accessing characters using positions.

Example:

text[0]

------------------------------------------------

Q5. What is slicing?

Answer:

Extracting a portion of a string.

Example:

text[0:3]

------------------------------------------------

Q6. How do you find length of a string?

Answer:

len(string)

------------------------------------------------

Q7. Difference between indexing and slicing?

Answer:

Indexing:
Returns a single character.

Example:
text[0]

Slicing:
Returns multiple characters.

Example:
text[0:3]

------------------------------------------------

Q8. How do you convert a string to uppercase?

Answer:

upper()

------------------------------------------------

Q9. How do you convert a string to lowercase?

Answer:

lower()

------------------------------------------------

Q10. Why are strings important?

Answer:

Strings are used in:

User Input
Authentication
APIs
Databases
Web Applications
Logging
Search Systems
"""

# ------------------------------------------------

"""
================================================
PRACTICE QUESTIONS
================================================

1. Print first character of a string.

2. Print last character of a string.

3. Find length of a string.

4. Concatenate first name and last name.

5. Convert string to uppercase.

6. Convert string to lowercase.

7. Count vowels in a string.

8. Reverse a string.

9. Check whether a word exists in a string.

10. Print every character using a loop.
"""

# ------------------------------------------------

"""
================================================
SUMMARY
================================================

String Data Type -> str

Important Concepts:

1. Indexing
2. Negative Indexing
3. Slicing
4. Concatenation
5. Repetition
6. String Methods
7. Looping Through Strings
8. Count Vowels
9. Reverse String
10. Immutability

Strings are heavily used in real-world
backend and software development.
"""