# PACKAGES IN PYTHON

## What is a Package?

A package is a collection of related modules organized inside a folder.

Think of it like:

* Function → Small reusable code
* Module → Python file
* Package → Folder containing modules

Example:

project/

├── calculator/
│   ├── __init__.py
│   ├── addition.py
│   ├── subtraction.py
│   └── multiplication.py

calculator is a package.

addition.py is a module.

add() is a function.

## Why Use Packages?

Benefits:

* Better Organization
* Scalability
* Easier Maintenance
* Code Reusability

Large projects use packages extensively.

Django itself is built using packages.

## Creating Your First Package

Folder Structure:

utilities/

├── __init__.py
├── email_utils.py
└── math_utils.py

The file:

__init__.py

tells Python that this folder is a package.

## Module 1

email_utils.py

def generate_email(name):

    return f"{name.lower()}@company.com"

## Module 2

math_utils.py

def add(a, b):

    return a + b

## Importing From Package

main.py

from utilities.email_utils import generate_email

print(generate_email("Alex"))

Output: alex@company.com

## Import Another Module

from utilities.math_utils import add

print(add(10, 20))

Output: 30

## Import Multiple Modules

from utilities.email_utils import generate_email

from utilities.math_utils import add

print(generate_email("Alex"))

print(add(10, 20))

Output: alex@company.com
30

## Package Alias

import utilities.math_utils as mu

print(mu.add(10, 20))

Output: 30

## What is **init**.py?

Example:

utilities/

├── __init__.py
├── email_utils.py
└── math_utils.py

Historically:

Python uses **init**.py to identify packages.

Modern Python can work without it in many cases.

Still used in professional projects.

Django uses it everywhere.

## Using **init**.py

utilities/**init**.py

from .math_utils import add

from .email_utils import generate_email

Now:
from utilities import add

print(add(10, 20))

Output: 30

## Nested Packages

Large projects use packages inside packages.

Example:

career_accelerator/

├── users/
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── auth_service.py
│   │
│   └── views/
│       ├── __init__.py
│       └── user_view.py

Very common in enterprise projects.

## Real World Example

Email Package

Structure:

communication/

├── __init__.py
├── email.py
├── sms.py
└── whatsapp.py

email.py

def send_email():

    print("Email Sent")

sms.py

def send_sms():

    print("SMS Sent")

main.py

from communication.email import send_email

send_email()

Output: Email Sent

## Real World Example

Employee Package

Structure:

employee/

├── __init__.py
├── profile.py
└── salary.py

profile.py

def employee_name():

    return "Alex"

salary.py

def calculate_salary():

    return 80000

main.py

from employee.salary import calculate_salary

print(calculate_salary())

Output: 80000

## Packages in Django

Django Project:

career_accelerator/

├── manage.py

├── career_accelerator/

│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py

├── users/

│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── apps.py

Everything is organized as packages.

This is why packages are important.

## Difference Between Module and Package

Module: math_utils.py

Single Python file.

Package:

utilities/

├── math_utils.py
├── email_utils.py
└── __init__.py

Folder containing modules.

## Interview Questions

### Q1. Difference Between Module and Package?

Module: Single Python file.

Package: Folder containing modules.

### Q2. What is **init**.py?

Answer: Special file used to identify and initialize packages.

### Q5. Can Packages Contain Other Packages?

Answer: Yes.

Called Nested Packages.

### Q6. Why Are Packages Important?

Answer: Large applications contain hundreds of modules.

Packages help organize them properly.

## Practice Questions

1. Create utilities package.
2. Create employee package.
3. Create email module.
4. Create salary module.
5. Import functions from package.
6. Use alias while importing.
7. Create nested package.
8. Create **init**.py.
9. Import using **init**.py.
10. Build a mini communication package.

## Summary

Important Concepts:

* Package
* Module
* **init**.py
* Nested Packages
* Package Imports

Used In:

* Django
* Flask
* FastAPI
* Automation
* Enterprise Applications
* Cloud Applications

Every professional Python project uses packages.
