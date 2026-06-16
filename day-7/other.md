# ARGPARSE BASICS IN PYTHON

## What is Argparse?

Argparse is Python's built-in module for handling command-line arguments.
It allows users to pass values when running Python programs.

Example: python app.py Alex

Here: Alex
is a command-line argument.

# Why Use Argparse?

Without argparse:
import sys
print(sys.argv)

Works, but becomes difficult for large applications.

Argparse provides:

* Cleaner code
* Automatic help messages
* Validation
* Optional arguments
* Professional CLI applications

# Real World Usage

Used in:

* Automation Scripts
* DevOps Tools
* Data Processing Scripts
* Machine Learning Projects
* Django Management Commands
* Enterprise Utilities

# Import Argparse
import argparse
Built into Python.
No installation required.

# First Example

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")
args = parser.parse_args()
print(args.name)

Run: python app.py Alex
Output: Alex
# Understanding the Flow

Create parser: parser = argparse.ArgumentParser()
Add arguments: parser.add_argument()
Read values: args = parser.parse_args()
Use values: args.name

# Multiple Arguments

Example:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("age")
args = parser.parse_args()
print(args.name)
print(args.age)

Run: python app.py Alex 25

Output:
Alex
25

# Integer Arguments

Example:

import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "age",
    type=int
)
args = parser.parse_args()
print(args.age + 5)
Run: python app.py 20

Output: 25

# Optional Arguments

Syntax: --argument_name

Example:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "--name"
)
args = parser.parse_args()
print(args.name)

Run: python app.py --name Alex

Output: Alex

# Difference Between Positional and Optional

Positional: python app.py Alex
Required.

Optional: python app.py --name Alex
Not required.

# Default Values

Example:

import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "--country",
    default="India"
)

args = parser.parse_args()
print(args.country)

Run: python app.py
Output: India

# Required Optional Argument

Example:
parser.add_argument(
    "--email",
    required=True
)
Run: python app.py

Output:
error:
the following arguments
are required: --email

# Help Messages

Example:
parser.add_argument(
    "--name",
    help="Enter user name"
)
Run: python app.py --help
Output: Enter user name

# Automatic Help

Every argparse program supports: python app.py --help
Automatically generated.
Very useful.

# Short Arguments

Example:
parser.add_argument(
    "-n",
    "--name"
)

Run: python app.py -n Alex
or
python app.py --name Alex
Both work.

# Multiple Values

Example:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "numbers",
    nargs="+",
    type=int
)
args = parser.parse_args()
print(args.numbers)

Run: python app.py 1 2 3 4
Output: [1, 2, 3, 4]

# Sum Calculator

Example:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "numbers",
    nargs="+",
    type=int
)
args = parser.parse_args()
print(
    sum(args.numbers)
)

Run: python app.py 10 20 30
Output: 60

# Boolean Flags

Example:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "--debug",
    action="store_true"
)
args = parser.parse_args()
print(args.debug)

Run: python app.py --debug
Output: True
Run: python app.py
Output: False

# Choices Validation

Example:
parser.add_argument(
    "--role",
    choices=[
        "admin",
        "user"
    ]
)

Run: python app.py --role admin
Valid.
Run: python app.py --role manager
Error.

# Real World Example

Employee Script:

import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "--name",
    required=True
)
parser.add_argument(
    "--salary",
    type=int,
    required=True
)

args = parser.parse_args()
print(
    f"{args.name}"
    f" earns "
    f"{args.salary}"
)

Run: python app.py
--name Alex
--salary 50000
Output: Alex earns 50000

# Mini Calculator

import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "num1",
    type=int
)

parser.add_argument(
    "num2",
    type=int
)

args = parser.parse_args()

print(
    args.num1 +
    args.num2
)

Run: python app.py 10 20
Output: 30

# File Processing Example

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--file",
    required=True
)
args = parser.parse_args()
print(
    f"Processing "
    f"{args.file}"
)

Run: python app.py
--file users.csv

# Common Mistakes

## Forgetting parse_args()

Bad: parser.add_argument(
    "--name"
)

Good: args = parser.parse_args()

## Wrong Data Type

Bad: age = "20"
age + 5
Error.
Use: type=int

## No Help Messages

Always add: help=
for better usability.

# Best Practices

### Use Descriptive Names

Good: --username
Bad: --u

### Add Help Text

Good: help="User email"

### Validate Inputs

Use: choices=
and
type=

### Provide Defaults

When possible.

# Django Example

Management Commands internally use argument parsing.

Example: python manage.py
createsuperuser
Django uses argument parsing behind the scenes.

# Interview Questions

### Q1. What is Argparse?

Answer: A Python module used for command-line argument parsing.

### Q2. Why Use Argparse?

Answer: To build professional command-line applications.

### Q3. Which Module Provides Argparse?

Answer: argparse

### Q4. What Does parse_args() Do?

Answer: Reads command-line arguments.

### Q5. What is a Positional Argument?

Answer: Required argument based on position.

### Q6. What is an Optional Argument?

Answer: Argument prefixed with: --

### Q7. How To Set Default Values?

Answer: default=

### Q8. How To Make Optional Argument Required?

Answer: required=True

### Q9. How To Create Boolean Flag?

Answer: action="store_true"

### Q10. How To Show Help?

Answer: python app.py --help

# Practice Questions

1. Print name from CLI.
2. Print age from CLI.
3. Add two numbers.
4. Create calculator.
5. Add default country.
6. Create required email argument.
7. Add boolean debug flag.
8. Use choices validation.
9. Process CSV filename argument.
10. Build employee management CLI.

# Summary

Important Concepts:

* ArgumentParser
* add_argument()
* parse_args()
* Positional Arguments
* Optional Arguments
* Default Values
* Help Messages
* Boolean Flags

Important Features:
required=True
default=
choices=
type=
action="store_true"

Used In:

* Automation Scripts
* DevOps Tools
* Data Processing
* Django Commands
* Enterprise Utilities

Argparse is essential for building professional command-line applications and automation tools.
