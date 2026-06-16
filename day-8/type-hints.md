# TYPE HINTS IN PYTHON

## What are Type Hints?

Type hints allow us to specify the expected data types of variables, function parameters, and return values.

Example:

def add(a: int, b: int) -> int:
    return a + b

Here:

```text
a -> int
b -> int
return -> int
```

Type hints improve code readability and maintainability.

---

# Why Use Type Hints?

Benefits:

* Better readability
* Better IDE support
* Easier debugging
* Cleaner code
* Professional codebase standards

Modern Django and FastAPI projects heavily use type hints.

---

# Function Type Hints

Example:

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

Usage:

```python
print(greet("Alex"))
```

Output:

```text
Hello Alex
```

---

# Multiple Parameters

```python
def calculate_total(
    price: float,
    quantity: int
) -> float:

    return price * quantity
```

---

# Return Type

Syntax:

```python
-> return_type
```

Example:

```python
def square(num: int) -> int:
    return num * num
```

---

# Variable Type Hints

```python
name: str = "Alex"

age: int = 25

salary: float = 50000.50
```

---

# List Type Hints

```python
numbers: list[int] = [

    1,
    2,
    3,
    4
]
```

---

# String List

```python
names: list[str] = [

    "Alex",

    "John",

    "Emma"
]
```

---

# Dictionary Type Hints

```python
student: dict[str, int] = {

    "math": 90,

    "science": 95
}
```

---

# Tuple Type Hints

```python
person: tuple[str, int] = (

    "Alex",

    25
)
```

---

# Optional Values

Sometimes a value may be None.

```python
from typing import Optional

def get_user(
    user_id: int
) -> Optional[str]:

    return None
```

Meaning:

```text
str OR None
```

---

# Union Types

```python
from typing import Union

def process(
    value: Union[int, str]
):

    print(value)
```

Can accept:

```python
10
```

or

```python
"Alex"
```

---

# Modern Union Syntax (Python 3.10+)

```python
def process(
    value: int | str
):
    print(value)
```

Preferred modern style.

---

# Any Type

```python
from typing import Any

def process(
    value: Any
):
    print(value)
```

Can accept anything.

Use carefully.

---

# Type Hinting Lists

```python
def get_names() -> list[str]:

    return [

        "Alex",

        "John"
    ]
```

---

# Type Hinting Dictionaries

```python
def get_marks() -> dict[str, int]:

    return {

        "Math": 95,

        "Science": 90
    }
```

---

# Class Type Hints

```python
class Student:

    def __init__(
        self,
        name: str,
        age: int
    ):

        self.name = name

        self.age = age
```

---

# Django Example

Model Method:

```python
class Student:

    def get_name(self) -> str:

        return self.name
```

Professional Django code often uses hints.

---

# API Example

```python
def get_user(
    user_id: int
) -> dict:

    return {

        "id": user_id
    }
```

---

# Benefits in IDEs

When using:

```python
name: str
```

IDE can:

* Autocomplete methods
* Detect mistakes
* Show warnings

---

# Type Hints Do NOT Enforce Types

Example:

```python
def add(
    a: int,
    b: int
) -> int:

    return a + b
```

Still runs:

```python
add(
    "10",
    "20"
)
```

Type hints are guidance.

Not strict validation.

---

# Common Mistakes

## Forgetting Return Type

Bad:

```python
def add(
    a: int,
    b: int
):
```

Good:

```python
def add(
    a: int,
    b: int
) -> int:
```

---

## Using Any Everywhere

Bad:

```python
value: Any
```

Use specific types whenever possible.

---

# Best Practices

### Type Hint All Functions

Good:

```python
def greet(
    name: str
) -> str:
```

---

### Type Hint Important Variables

Good:

```python
age: int = 25
```

---

### Use Modern Syntax

Good:

```python
int | str
```

Instead of:

```python
Union[int, str]
```

when possible.

---

# Interview Questions

### Q1. What are Type Hints?

Answer:

Annotations that indicate expected data types.

---

### Q2. Are Type Hints Mandatory?

Answer:

No.

---

### Q3. Do Type Hints Enforce Types?

Answer:

No.

They improve readability and tooling.

---

### Q4. Return Type Syntax?

Answer:

```python
-> int
```

---

### Q5. List Type Hint?

Answer:

```python
list[int]
```

---

### Q6. Dictionary Type Hint?

Answer:

```python
dict[str, int]
```

---

### Q7. What is Optional?

Answer:

A value that can be a type or None.

---

### Q8. What is Any?

Answer:

Represents any type.

---

### Q9. Why Use Type Hints?

Answer:

Readability, maintenance, and IDE support.

---

### Q10. Are Type Hints Used in Django Projects?

Answer:

Yes, increasingly in modern codebases.

---

# Practice Questions

1. Add type hints to a calculator.
2. Create typed student dictionary.
3. Create typed list of names.
4. Create function returning list[str].
5. Create function returning dict.
6. Use Optional.
7. Use Union.
8. Use Any.
9. Add hints to class.
10. Convert old code to typed code.

---

# Summary

Important Concepts:

* Function Type Hints
* Variable Type Hints
* Optional
* Union
* Any
* Typed Lists
* Typed Dictionaries

Used In:

* Django
* FastAPI
* Enterprise Applications
* Modern Python Codebases

Type hints are considered a professional Python practice and are becoming standard in modern backend development.
