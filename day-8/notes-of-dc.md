# DATACLASSES IN PYTHON

## What are Dataclasses?

Dataclasses are a modern Python feature introduced in Python 3.7.

They automatically generate common methods such as:

* **init**()
* **repr**()
* **eq**()

This reduces boilerplate code.

---

# Why Dataclasses?

Normal Class:

```python
class Student:

    def __init__(
        self,
        name,
        age
    ):
        self.name = name
        self.age = age
```

Dataclass:

```python
from dataclasses import dataclass

@dataclass
class Student:

    name: str

    age: int
```

Much cleaner.

---

# Import Dataclass

```python
from dataclasses import dataclass
```

Built into Python.

No installation required.

---

# First Dataclass

```python
from dataclasses import dataclass

@dataclass
class Student:

    name: str

    age: int
```

Create Object:

```python
student = Student(
    "Alex",
    25
)

print(student)
```

Output:

```text
Student(name='Alex', age=25)
```

---

# Automatic Constructor

Dataclasses automatically create:

```python
__init__()
```

Equivalent code:

```python
class Student:

    def __init__(
        self,
        name,
        age
    ):

        self.name = name

        self.age = age
```

---

# Access Values

```python
student = Student(
    "Alex",
    25
)

print(student.name)

print(student.age)
```

Output:

```text
Alex
25
```

---

# Automatic String Representation

Without dataclass:

```python
<__main__.Student object>
```

With dataclass:

```text
Student(name='Alex', age=25)
```

Generated automatically.

---

# Equality Comparison

Example:

```python
from dataclasses import dataclass

@dataclass
class Student:

    name: str

    age: int
```

```python
s1 = Student(
    "Alex",
    25
)

s2 = Student(
    "Alex",
    25
)

print(s1 == s2)
```

Output:

```text
True
```

Without dataclasses:

```text
False
```

---

# Default Values

```python
from dataclasses import dataclass

@dataclass
class Student:

    name: str

    age: int = 18
```

Usage:

```python
student = Student(
    "Alex"
)

print(student)
```

Output:

```text
Student(name='Alex', age=18)
```

---

# Multiple Default Values

```python
@dataclass
class Employee:

    name: str

    salary: int = 30000

    city: str = "Pune"
```

---

# Dataclass Methods

You can still add methods.

```python
from dataclasses import dataclass

@dataclass
class Student:

    name: str

    age: int

    def greet(self):

        print(

            f"Hello {self.name}"
        )
```

Usage:

```python
student = Student(
    "Alex",
    25
)

student.greet()
```

Output:

```text
Hello Alex
```

---

# **post_init**()

Runs after object creation.

Example:

```python
from dataclasses import dataclass

@dataclass
class Student:

    name: str

    age: int

    def __post_init__(self):

        print(
            "Student Created"
        )
```

Output:

```text
Student Created
```

---

# Example Validation

```python
from dataclasses import dataclass

@dataclass
class Employee:

    name: str

    salary: int

    def __post_init__(self):

        if self.salary < 0:

            raise ValueError(
                "Salary cannot be negative"
            )
```

---

# Dataclass with List

Bad:

```python
@dataclass
class Student:

    skills: list = []
```

Problem:

Mutable default values.

---

# Correct Way

```python
from dataclasses import field

@dataclass
class Student:

    skills: list = field(
        default_factory=list
    )
```

---

# Dataclass with Dictionary

```python
from dataclasses import field

@dataclass
class Student:

    marks: dict = field(
        default_factory=dict
    )
```

---

# Frozen Dataclass

Read-only objects.

```python
from dataclasses import dataclass

@dataclass(
    frozen=True
)
class Student:

    name: str

    age: int
```

Usage:

```python
student.age = 30
```

Output:

```text
Error
```

---

# Dataclass to Dictionary

```python
from dataclasses import dataclass
from dataclasses import asdict

@dataclass
class Student:

    name: str

    age: int
```

```python
student = Student(
    "Alex",
    25
)

print(
    asdict(student)
)
```

Output:

```python
{
    'name': 'Alex',
    'age': 25
}
```

---

# Dataclass to Tuple

```python
from dataclasses import astuple
```

```python
print(
    astuple(student)
)
```

Output:

```python
('Alex', 25)
```

---

# Real World API Example

```python
from dataclasses import dataclass

@dataclass
class UserResponse:

    id: int

    name: str

    email: str
```

Used for structured API responses.

---

# Configuration Example

```python
from dataclasses import dataclass

@dataclass
class Settings:

    db_name: str

    db_user: str

    debug: bool
```

---

# Django Example

Although Django Models are not dataclasses:

```python
class Student(models.Model):

    name = models.CharField(
        max_length=100
    )
```

Dataclasses are often used for:

* DTOs
* API Responses
* Service Layer Objects
* Configuration Objects

---

# Dataclass vs Normal Class

Normal Class:

```python
class Student:

    def __init__(
        self,
        name,
        age
    ):
        self.name = name
        self.age = age
```

Dataclass:

```python
@dataclass
class Student:

    name: str

    age: int
```

Less code.

More readable.

---

# Common Mistakes

## Forgetting Decorator

Bad:

```python
class Student:

    name: str
```

Good:

```python
@dataclass
class Student:
```

---

## Mutable Defaults

Bad:

```python
skills: list = []
```

Good:

```python
field(
    default_factory=list
)
```

---

# Best Practices

### Use Type Hints

Good:

```python
name: str

age: int
```

---

### Use Dataclasses for Data Containers

Good for:

* User Data
* Settings
* API Responses

---

### Use **post_init** For Validation

Good:

```python
def __post_init__(self):
```

---

# Career Accelerator Platform Example

Student Profile:

```python
from dataclasses import dataclass

@dataclass
class StudentProfile:

    name: str

    email: str

    course: str
```

---

Resume Data:

```python
@dataclass
class Resume:

    title: str

    skills: list[str]
```

---

Job Application:

```python
@dataclass
class Application:

    student_id: int

    job_id: int
```

---

# Interview Questions

### Q1. What is a Dataclass?

Answer:

A special class used to reduce boilerplate code.

---

### Q2. Which Module Provides Dataclass?

Answer:

```python
dataclasses
```

---

### Q3. Which Decorator Creates Dataclass?

Answer:

```python
@dataclass
```

---

### Q4. What Methods Are Auto Generated?

Answer:

```python
__init__()

__repr__()

__eq__()
```

---

### Q5. What is **post_init**?

Answer:

Runs after initialization.

---

### Q6. How To Create Read-Only Dataclass?

Answer:

```python
@dataclass(
    frozen=True
)
```

---

### Q7. Convert Dataclass To Dictionary?

Answer:

```python
asdict()
```

---

### Q8. Convert Dataclass To Tuple?

Answer:

```python
astuple()
```

---

### Q9. Why Use Dataclasses?

Answer:

Cleaner and more maintainable code.

---

### Q10. Are Dataclasses Used in Backend Projects?

Answer:

Yes, very frequently.

---

# Practice Questions

1. Create Student dataclass.
2. Create Employee dataclass.
3. Add default values.
4. Add custom method.
5. Use **post_init**.
6. Validate salary.
7. Convert to dictionary.
8. Convert to tuple.
9. Create frozen dataclass.
10. Build Resume dataclass.

---

# Summary

Important Concepts:

* @dataclass
* Type Hints
* **post_init**()
* frozen=True
* asdict()
* astuple()

Used In:

* APIs
* DTOs
* Configurations
* Backend Services
* Enterprise Applications

Dataclasses are one of the most useful modern Python features because they provide clean, readable, and maintainable code for data-focused objects.
