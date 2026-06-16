# PATHLIB IN PYTHON

## What is Pathlib?

Pathlib is Python's modern module for working with:

* Files
* Folders
* Directories
* File Paths

Introduced in Python 3.4.

It replaces many older operations done using:

```python
import os
```

---

# Why Pathlib?

Old Way:

```python
import os

path = os.path.join(
    "data",
    "users.txt"
)
```

Modern Way:

```python
from pathlib import Path

path = Path("data") / "users.txt"
```

Cleaner and easier to read.

---

# Import Path

```python
from pathlib import Path
```

---

# Create Path Object

```python
from pathlib import Path

path = Path("students.txt")

print(path)
```

Output:

```text
students.txt
```

---

# Current Working Directory

```python
from pathlib import Path

print(Path.cwd())
```

Output:

```text
C:\Projects\career-platform
```

---

# Home Directory

```python
from pathlib import Path

print(Path.home())
```

Output:

```text
C:\Users\Alex
```

---

# Create Folder Path

```python
from pathlib import Path

folder = Path("documents")

print(folder)
```

Output:

```text
documents
```

---

# Join Paths

Old:

```python
os.path.join(
    "data",
    "users.txt"
)
```

Pathlib:

```python
from pathlib import Path

path = Path("data") / "users.txt"

print(path)
```

Output:

```text
data/users.txt
```

---

# Check File Exists

```python
from pathlib import Path

file = Path("users.txt")

print(
    file.exists()
)
```

Output:

```text
True
```

or

```text
False
```

---

# Check File

```python
file.is_file()
```

Example:

```python
from pathlib import Path

file = Path("users.txt")

print(
    file.is_file()
)
```

---

# Check Directory

```python
folder.is_dir()
```

Example:

```python
from pathlib import Path

folder = Path("data")

print(
    folder.is_dir()
)
```

---

# Create Directory

```python
from pathlib import Path

folder = Path("reports")

folder.mkdir()
```

Creates:

```text
reports/
```

---

# Create Nested Directories

```python
from pathlib import Path

Path(

    "data/reports/2025"

).mkdir(

    parents=True,

    exist_ok=True
)
```

---

# Create File

```python
from pathlib import Path

file = Path("notes.txt")

file.touch()
```

Creates:

```text
notes.txt
```

---

# Write Text File

```python
from pathlib import Path

file = Path("notes.txt")

file.write_text(
    "Hello World"
)
```

---

# Read Text File

```python
from pathlib import Path

file = Path("notes.txt")

content = file.read_text()

print(content)
```

Output:

```text
Hello World
```

---

# Append Text

```python
from pathlib import Path

file = Path("notes.txt")

existing = file.read_text()

file.write_text(

    existing +

    "\nNew Line"
)
```

---

# Delete File

```python
from pathlib import Path

file = Path("notes.txt")

file.unlink()
```

Deletes file.

---

# Delete Empty Folder

```python
from pathlib import Path

folder = Path("reports")

folder.rmdir()
```

---

# Get File Name

```python
from pathlib import Path

file = Path(

    "users.csv"
)

print(
    file.name
)
```

Output:

```text
users.csv
```

---

# File Extension

```python
print(
    file.suffix
)
```

Output:

```text
.csv
```

---

# File Name Without Extension

```python
print(
    file.stem
)
```

Output:

```text
users
```

---

# Parent Folder

```python
print(
    file.parent
)
```

---

# Absolute Path

```python
from pathlib import Path

file = Path(
    "users.csv"
)

print(
    file.resolve()
)
```

Output:

```text
C:\Projects\users.csv
```

---

# Iterate Files

```python
from pathlib import Path

folder = Path(".")

for file in folder.iterdir():

    print(file)
```

---

# Find All TXT Files

```python
from pathlib import Path

for file in Path(".").glob(

    "*.txt"
):

    print(file)
```

---

# Find All Python Files

```python
for file in Path(".").glob(

    "*.py"
):

    print(file)
```

---

# Recursive Search

```python
for file in Path(".").rglob(

    "*.py"
):

    print(file)
```

Searches subfolders too.

---

# Count Files

```python
from pathlib import Path

files = list(

    Path(".").glob("*")
)

print(
    len(files)
)
```

---

# Read CSV Path

```python
from pathlib import Path

csv_file = Path(
    "students.csv"
)

if csv_file.exists():

    print("Found")
```

---

# Django Example

Django settings.py:

```python
from pathlib import Path

BASE_DIR = (

    Path(__file__)

    .resolve()

    .parent

    .parent
)
```

This is used in every modern Django project.

---

# Upload Folder Example

```python
MEDIA_ROOT = (

    BASE_DIR /

    "media"
)
```

---

# Static Files Example

```python
STATIC_ROOT = (

    BASE_DIR /

    "static"
)
```

---

# Environment File Example

```python
ENV_FILE = (

    BASE_DIR /

    ".env"
)
```

---

# Career Accelerator Platform Example

Resume Folder:

```python
RESUME_FOLDER = (

    BASE_DIR /

    "resumes"
)
```

---

Generated Reports Folder:

```python
REPORTS_FOLDER = (

    BASE_DIR /

    "reports"
)
```

---

Student Uploads:

```python
UPLOADS_FOLDER = (

    BASE_DIR /

    "uploads"
)
```

---

# Common Mistakes

## Mixing Strings and Paths

Bad:

```python
path =

"data" +

"users.txt"
```

Good:

```python
Path("data")

/

"users.txt"
```

---

## Not Checking Exists

Bad:

```python
file.read_text()
```

Good:

```python
if file.exists():
```

---

## Using os.path Everywhere

Modern projects prefer:

```python
pathlib
```

---

# Best Practices

### Use Path Objects

Good:

```python
Path()
```

---

### Use resolve()

For absolute paths.

---

### Check Exists

Before reading files.

---

### Use pathlib in Django

Industry standard.

---

# Interview Questions

### Q1. What is Pathlib?

Answer:

Modern Python module for handling file system paths.

---

### Q2. Which Class Is Used?

Answer:

```python
Path
```

---

### Q3. Current Directory?

Answer:

```python
Path.cwd()
```

---

### Q4. Home Directory?

Answer:

```python
Path.home()
```

---

### Q5. Create Folder?

Answer:

```python
mkdir()
```

---

### Q6. Create File?

Answer:

```python
touch()
```

---

### Q7. Delete File?

Answer:

```python
unlink()
```

---

### Q8. Read File?

Answer:

```python
read_text()
```

---

### Q9. Write File?

Answer:

```python
write_text()
```

---

### Q10. Django Uses Pathlib?

Answer:

Yes.

---

# Practice Questions

1. Print current directory.
2. Print home directory.
3. Create reports folder.
4. Create notes.txt.
5. Write text into file.
6. Read file content.
7. Find all .txt files.
8. Find all .py files.
9. Create nested folders.
10. Build file manager utility.

---

# Summary

Important Methods:

```python
Path()

cwd()

home()

exists()

is_file()

is_dir()

mkdir()

touch()

read_text()

write_text()

unlink()

glob()

rglob()

resolve()
```

Used In:

* Django
* Flask
* FastAPI
* Automation Scripts
* Data Engineering
* Enterprise Applications

Pathlib is the modern and recommended way to work with files and directories in Python and is heavily used in professional backend development.
