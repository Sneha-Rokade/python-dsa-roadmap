# ENVIRONMENT VARIABLES IN PYTHON

## What are Environment Variables?

Environment Variables are values stored outside your code.

Examples:

```text
SECRET_KEY
DATABASE_PASSWORD
EMAIL_PASSWORD
API_KEY
DEBUG
```

Instead of writing sensitive information directly inside your code, you store it in environment variables.

---

# Why Use Environment Variables?

Bad:

```python
SECRET_KEY = "my-secret-key"

DATABASE_PASSWORD = "admin123"
```

Problems:

* Security risk
* Password leakage
* GitHub exposure
* Difficult configuration management

---

# Good Approach

```python
import os

SECRET_KEY = os.getenv(
    "SECRET_KEY"
)
```

Now secrets are not stored in source code.

---

# Real World Usage

Used in:

* Django
* Flask
* FastAPI
* Docker
* Kubernetes
* AWS
* Azure

Every production application uses environment variables.

---

# Import os Module

```python
import os
```

Built into Python.

---

# Reading Environment Variable

Example:

```python
import os

name = os.getenv(
    "NAME"
)

print(name)
```

---

# Setting Variable (Temporary)

Windows:

```cmd
set NAME=Alex
```

Linux/Mac:

```bash
export NAME=Alex
```

Run program:

```python
import os

print(
    os.getenv("NAME")
)
```

Output:

```text
Alex
```

---

# Default Values

Example:

```python
import os

debug = os.getenv(

    "DEBUG",

    "False"
)

print(debug)
```

Output:

```text
False
```

If variable doesn't exist, default value is returned.

---

# os.getenv() Syntax

```python
os.getenv(

    "VARIABLE_NAME",

    default_value
)
```

---

# Checking Variable Exists

```python
import os

if os.getenv("API_KEY"):

    print("Found")

else:

    print("Missing")
```

---

# Using Environment Variables in Django

Bad:

```python
SECRET_KEY =

"super-secret-key"
```

Good:

```python
import os

SECRET_KEY = os.getenv(
    "SECRET_KEY"
)
```

---

# Installing python-dotenv

Most projects use:

```bash
pip install python-dotenv
```

This loads variables from:

```text
.env
```

file.

---

# What is .env File?

Example:

```env
SECRET_KEY=mysecretkey

DEBUG=True

DATABASE_NAME=career_db

DATABASE_USER=postgres

DATABASE_PASSWORD=admin123
```

---

# Why .env?

Benefits:

* Cleaner configuration
* Better security
* Easier deployment

---

# Loading .env File

Install:

```bash
pip install python-dotenv
```

Import:

```python
from dotenv import load_dotenv
```

Load:

```python
load_dotenv()
```

---

# Example

```python
from dotenv import load_dotenv

import os

load_dotenv()

secret_key = os.getenv(
    "SECRET_KEY"
)

print(secret_key)
```

---

# Project Structure

```text
project/

├── .env

├── app.py

└── requirements.txt
```

---

# Example .env

```env
NAME=Alex

AGE=25

CITY=Pune
```

---

# Read Variables

```python
from dotenv import load_dotenv

import os

load_dotenv()

print(
    os.getenv("NAME")
)

print(
    os.getenv("CITY")
)
```

Output:

```text
Alex
Pune
```

---

# Database Configuration Example

.env

```env
DB_NAME=career_db

DB_USER=postgres

DB_PASSWORD=admin123
```

Python:

```python
import os

db_name = os.getenv(
    "DB_NAME"
)

db_user = os.getenv(
    "DB_USER"
)
```

---

# Django Database Example

```python
DATABASES = {

    "default": {

        "NAME":

        os.getenv(
            "DB_NAME"
        ),

        "USER":

        os.getenv(
            "DB_USER"
        ),

        "PASSWORD":

        os.getenv(
            "DB_PASSWORD"
        )
    }
}
```

---

# API Key Example

.env

```env
OPENAI_API_KEY=abc123
```

Python:

```python
api_key = os.getenv(
    "OPENAI_API_KEY"
)
```

---

# Email Credentials Example

.env

```env
EMAIL_USER=admin@gmail.com

EMAIL_PASSWORD=password123
```

Python:

```python
email_user = os.getenv(
    "EMAIL_USER"
)
```

---

# Boolean Values

.env

```env
DEBUG=True
```

Python:

```python
debug = os.getenv(
    "DEBUG"
)
```

Output:

```text
True
```

Remember:

It is still a string.

---

# Convert to Boolean

```python
debug = (

    os.getenv(

        "DEBUG",

        "False"

    ) == "True"
)
```

---

# Integer Values

.env

```env
PORT=8000
```

Python:

```python
port = int(

    os.getenv(
        "PORT",
        8000
    )
)
```

---

# Never Push .env to GitHub

Create:

```text
.gitignore
```

Add:

```gitignore
.env
```

Very important.

---

# Why Ignore .env?

Contains:

* Passwords
* API Keys
* Database Credentials
* Tokens

Never commit secrets.

---

# Common Mistakes

## Hardcoding Secrets

Bad:

```python
SECRET_KEY =

"secret123"
```

Good:

```python
SECRET_KEY = os.getenv(
    "SECRET_KEY"
)
```

---

## Pushing .env to GitHub

Bad:

```text
.env
```

inside repository.

---

## Forgetting load_dotenv()

Bad:

```python
os.getenv("NAME")
```

without:

```python
load_dotenv()
```

---

# Best Practices

### Store Secrets in .env

Good:

```env
DATABASE_PASSWORD=
```

---

### Use os.getenv()

Good:

```python
os.getenv()
```

---

### Add .env to .gitignore

Always.

---

### Provide Defaults

Example:

```python
os.getenv(
    "PORT",
    8000
)
```

---

# Career Accelerator Platform Example

.env

```env
SECRET_KEY=my-secret-key

DEBUG=True

DB_NAME=career_db

DB_USER=postgres

DB_PASSWORD=postgres123

EMAIL_USER=admin@gmail.com

EMAIL_PASSWORD=password
```

settings.py

```python
from dotenv import load_dotenv

import os

load_dotenv()

SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

DEBUG = (

    os.getenv(
        "DEBUG"
    ) == "True"
)
```

Professional setup.

---

# Interview Questions

### Q1. What is an Environment Variable?

Answer:

A value stored outside the application code.

---

### Q2. Why Use Environment Variables?

Answer:

Security and configuration management.

---

### Q3. Which Function Reads Environment Variables?

Answer:

```python
os.getenv()
```

---

### Q4. Which Module Handles Environment Variables?

Answer:

```python
os
```

---

### Q5. What is .env?

Answer:

A file storing environment variables.

---

### Q6. Which Package Loads .env Files?

Answer:

```python
python-dotenv
```

---

### Q7. Function Used To Load .env?

Answer:

```python
load_dotenv()
```

---

### Q8. Should .env Be Pushed To GitHub?

Answer:

No.

---

### Q9. Why Not Hardcode Secrets?

Answer:

Security risks.

---

### Q10. Is This Used In Django?

Answer:

Yes, in almost every professional Django project.

---

# Practice Questions

1. Read NAME variable.
2. Create .env file.
3. Load .env using dotenv.
4. Read database credentials.
5. Read API key.
6. Convert DEBUG to boolean.
7. Convert PORT to integer.
8. Configure Django SECRET_KEY.
9. Add .env to .gitignore.
10. Build project configuration loader.

---

# Summary

Important Concepts:

* Environment Variables
* os.getenv()
* .env Files
* python-dotenv
* load_dotenv()

Important Security Rule:

```text
Never hardcode secrets.
Never push .env to GitHub.
```

Used In:

* Django
* Flask
* FastAPI
* Docker
* Cloud Deployments
* Enterprise Applications

Environment variables are a mandatory skill for backend developers because every production application depends on secure configuration management.
