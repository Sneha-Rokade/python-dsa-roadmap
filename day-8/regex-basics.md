# REGEX BASICS IN PYTHON

## What is Regex?

Regex (Regular Expression) is a powerful pattern matching technique used to search, validate, and manipulate text.

Regex is commonly used for:

* Email Validation
* Phone Number Validation
* Password Validation
* Search Features
* Data Cleaning
* Log Analysis

---

# Why Learn Regex?

Imagine checking if an email is valid.

Without regex:

```python
if "@" in email:
    print("Valid")
```

Not reliable.

Regex provides professional validation.

---

# Import Regex Module

```python
import re
```

Built into Python.

No installation required.

---

# First Regex Example

```python
import re

text = "Python"

result = re.search(
    "Python",
    text
)

print(result)
```

Output:

```text
<re.Match object>
```

Meaning:

```text
Pattern Found
```

---

# Search Pattern

```python
re.search()
```

Searches entire string.

Example:

```python
import re

text = "I love Python"

result = re.search(
    "Python",
    text
)

print(result)
```

Output:

```text
Match Found
```

---

# No Match Example

```python
import re

text = "I love Java"

result = re.search(
    "Python",
    text
)

print(result)
```

Output:

```python
None
```

---

# Match From Beginning

```python
re.match()
```

Checks only beginning.

Example:

```python
import re

text = "Python Programming"

result = re.match(
    "Python",
    text
)

print(result)
```

Output:

```text
Match Found
```

---

# Find All Matches

```python
re.findall()
```

Example:

```python
import re

text = "Python Java Python"

result = re.findall(
    "Python",
    text
)

print(result)
```

Output:

```python
['Python', 'Python']
```

---

# Replace Text

```python
re.sub()
```

Example:

```python
import re

text = "I love Java"

result = re.sub(
    "Java",
    "Python",
    text
)

print(result)
```

Output:

```text
I love Python
```

---

# Split Text

```python
re.split()
```

Example:

```python
import re

text = "Python,Java,C++"

result = re.split(
    ",",
    text
)

print(result)
```

Output:

```python
['Python', 'Java', 'C++']
```

---

# Regex Metacharacters

Special symbols:

```text
.
^
$
*
+
?
[]
{}
|
\
```

Very important.

---

# Dot (.)

Matches any character.

Example:

```python
import re

print(

    re.findall(
        "P.thon",
        "Python"
    )
)
```

Output:

```python
['Python']
```

---

# Caret (^)

Starts with.

Example:

```python
import re

text = "Python"

print(

    re.search(
        "^Python",
        text
    )
)
```

Output:

```text
Match Found
```

---

# Dollar ($)

Ends with.

Example:

```python
import re

text = "Learn Python"

print(

    re.search(
        "Python$",
        text
    )
)
```

Output:

```text
Match Found
```

---

# Star (*)

Zero or more occurrences.

Example:

```python
import re

print(

    re.findall(
        "ab*",
        "abbb"
    )
)
```

Output:

```python
['abbb']
```

---

# Plus (+)

One or more occurrences.

Example:

```python
import re

print(

    re.findall(
        "ab+",
        "abbb"
    )
)
```

Output:

```python
['abbb']
```

---

# Question Mark (?)

Optional character.

Example:

```python
import re

print(

    re.findall(
        "colou?r",
        "color colour"
    )
)
```

Output:

```python
['color', 'colour']
```

---

# Character Sets []

Example:

```python
import re

print(

    re.findall(
        "[aeiou]",
        "python programming"
    )
)
```

Output:

```python
['o', 'o', 'a', 'i']
```

---

# Number Matching

```python
\d
```

Means:

```text
Any digit
```

Example:

```python
import re

text = "Age: 25"

print(

    re.findall(
        r"\d",
        text
    )
)
```

Output:

```python
['2', '5']
```

---

# Multiple Digits

```python
\d+
```

Example:

```python
import re

text = "Age: 25"

print(

    re.findall(
        r"\d+",
        text
    )
)
```

Output:

```python
['25']
```

---

# Letters Only

```python
[a-z]
```

Lowercase.

```python
[A-Z]
```

Uppercase.

```python
[a-zA-Z]
```

Any letter.

---

# Word Characters

```python
\w
```

Matches:

```text
letters
numbers
underscore
```

Example:

```python
re.findall(
    r"\w",
    "Python123"
)
```

---

# Whitespace

```python
\s
```

Matches:

```text
space
tab
newline
```

---

# Email Validation

Simple Example:

```python
import re

email = "test@gmail.com"

pattern =

r"^[a-zA-Z0-9._%+-]+"

r"@[a-zA-Z0-9.-]+"

r"\.[a-zA-Z]{2,}$"

result = re.match(
    pattern,
    email
)

print(
    bool(result)
)
```

Output:

```text
True
```

---

# Phone Number Validation

```python
import re

phone = "9876543210"

pattern =

r"^[0-9]{10}$"

print(

    bool(

        re.match(
            pattern,
            phone
        )
    )
)
```

Output:

```text
True
```

---

# Password Validation

Example:

```python
import re

password = "Admin123"

pattern =

r"^(?=.*[A-Z])"

r"(?=.*[a-z])"

r"(?=.*\d).+$"

print(

    bool(

        re.match(
            pattern,
            password
        )
    )
)
```

Output:

```text
True
```

---

# Extract Numbers

```python
import re

text =

"Order 123 Amount 500"

numbers = re.findall(

    r"\d+",

    text
)

print(numbers)
```

Output:

```python
['123', '500']
```

---

# Extract Emails

```python
import re

text =

"alex@gmail.com"

emails = re.findall(

    r"\S+@\S+",

    text
)

print(emails)
```

---

# Django Example

Email Validation:

```python
import re

def validate_email(
    email
):

    pattern =

    r"^[\w\.-]+"

    r"@"

    r"[\w\.-]+"

    r"\.\w+$"

    return bool(

        re.match(
            pattern,
            email
        )
    )
```

---

# Career Accelerator Platform Example

Resume Email Extraction:

```python
emails = re.findall(

    r"\S+@\S+",

    resume_text
)
```

---

Phone Number Extraction:

```python
phones = re.findall(

    r"\d{10}",

    resume_text
)
```

---

Skill Matching:

```python
re.findall(

    "Python",

    resume_text
)
```

---

# Common Mistakes

## Forgetting Raw String

Bad:

```python
"\d+"
```

Good:

```python
r"\d+"
```

---

## Overcomplicated Patterns

Keep regex readable.

---

## Using Regex for Everything

Simple checks may not need regex.

---

# Best Practices

### Use Raw Strings

Good:

```python
r"\d+"
```

---

### Test Patterns

Always verify results.

---

### Keep Patterns Readable

Add comments for complex regex.

---

# Interview Questions

### Q1. What is Regex?

Answer:

Pattern matching technique used for searching and validating text.

---

### Q2. Which Module Supports Regex?

Answer:

```python
re
```

---

### Q3. Search Function?

Answer:

```python
re.search()
```

---

### Q4. Find All Matches?

Answer:

```python
re.findall()
```

---

### Q5. Replace Text?

Answer:

```python
re.sub()
```

---

### Q6. Split Text?

Answer:

```python
re.split()
```

---

### Q7. Meaning of \d?

Answer:

Digit.

---

### Q8. Meaning of \w?

Answer:

Word character.

---

### Q9. Meaning of \s?

Answer:

Whitespace.

---

### Q10. Why Use Raw Strings?

Answer:

To avoid escaping issues.

---

# Practice Questions

1. Search word Python.
2. Find all vowels.
3. Extract numbers.
4. Extract emails.
5. Validate email.
6. Validate phone number.
7. Validate password.
8. Replace text.
9. Split CSV string.
10. Build registration validator.

---

# Summary

Important Functions:

```python
re.search()

re.match()

re.findall()

re.sub()

re.split()
```

Important Patterns:

```python
\d

\w

\s

^

$

+

*

?
```

Used In:

* Django Forms
* APIs
* Data Cleaning
* Resume Parsing
* Email Validation
* Password Validation

Regex is one of the most practical Python skills because it is heavily used in backend development, automation, and data processing.
