# PIP AND REQUIREMENTS.TXT IN PYTHON

## What is pip?

pip stands for: Pip Installs Packages
It is Python's package manager.

pip is used to:
* Install packages
* Upgrade packages
* Remove packages
* Manage project dependencies

# Why Do We Need pip?

Python comes with built-in modules.

Examples:
import math
import json
import csv
But many libraries are developed by the community.

Examples:
Django
Requests
NumPy
Pandas
Flask
pip installs these libraries.

# Check pip Version

Command: pip --version
Output: pip 24.x.x

# Install a Package

Example: pip install django
Output: Successfully installed Django

# Install Specific Version

Example: pip install django==5.0
Very common in professional projects.

# Install Multiple Packages

Example: pip install django requests

Installs:
Django
Requests
Together.

# View Installed Packages

Command: pip list

Output:
Django
requests
sqlparse
asgiref

# Package Information

Example: pip show django

Output:
Name: Django
Version: 5.0
Location: ...
Useful for debugging.

# Upgrade Package

Example: pip install --upgrade django
Upgrades package to latest version.

# Uninstall Package

Example: pip uninstall django
Output: Successfully uninstalled Django

# Search Package (Legacy)

Historically: pip search django
This is no longer commonly used.
Instead use: https://pypi.org
to search packages.

# What is PyPI?

PyPI stands for: Python Package Index
Official repository for Python packages.

Examples:
Django
Requests
NumPy
Pandas
FastAPI
All hosted on PyPI.

# REQUIREMENTS.TXT

A file that stores project dependencies.

Example: Django==5.0.7
requests==2.32.3
Very important in real projects.

# Why requirements.txt?

Imagine:

Developer A installs: Django
Requests

Developer B clones repository.
How does Developer B know required packages?
Answer: requirements.txt

# Generate requirements.txt

Command: pip freeze > requirements.txt

Generated File:
asgiref==3.8.1
Django==5.0.7
requests==2.32.3
sqlparse==0.5.1

# Understanding pip freeze

Command: pip freeze
Shows all installed packages.

Example:
Django==5.0.7
requests==2.32.3

# Install Dependencies from requirements.txt

Command: pip install -r requirements.txt
Installs all packages automatically.
Very common.

# Real World Workflow

Developer A:
pip install django
pip install requests
pip freeze > requirements.txt
Pushes to GitHub.

Developer B:
git clone project
pip install -r requirements.txt
Project works immediately.

# Example Django Project

Create Environment: python -m venv venv
Activate: venv\Scripts\activate
Install Django: pip install django
Generate: pip freeze > requirements.txt

# Example requirements.txt

Django==5.0.7
requests==2.32.3
python-dotenv==1.0.1
Very common backend stack.

# Updating requirements.txt

After installing new package: pip install pillow
Regenerate: pip freeze > requirements.txt
Always keep file updated.

# Install Package in Virtual Environment

Correct Workflow: python -m venv venv
venv\Scripts\activate
pip install django
Never install globally.

# Common Commands

Install: pip install django
Upgrade: pip install --upgrade django
Uninstall: pip uninstall django
List: pip list
Show: pip show django
Freeze: pip freeze
Requirements: pip freeze > requirements.txt
Install Requirements: pip install -r requirements.txt

# Common Mistakes

## Installing Outside Virtual Environment

Bad: pip install django
without activating venv.

## Forgetting requirements.txt

Team members cannot recreate project.

## Forgetting Version Numbers

Bad: Django
Good: Django==5.0.7
Version consistency matters.

# Best Practices

## Use Virtual Environment

Always.

## Keep requirements.txt Updated

After every package installation.

## Pin Versions

Good: Django==5.0.7
Bad: Django

## Install from requirements.txt

For team projects.

# Career Accelerator Platform Example

Dependencies:
Django
djangorestframework
requests
python-dotenv
Pillow
Generate: pip freeze > requirements.txt
Push to GitHub.

# Interview Questions

### Q1. What is pip?

Answer: Python package manager used to install and manage packages.

### Q2. What is PyPI?

Answer: Python Package Index, the official repository for Python packages.

### Q3. Command to Install Package?

Answer: pip install package_name

### Q4. Command to Upgrade Package?

Answer: pip install --upgrade package_name

### Q5. Command to Uninstall Package?

Answer: pip uninstall package_name

### Q6. What is requirements.txt?

Answer: A file containing project dependencies.

### Q7. Command to Generate requirements.txt?

Answer: pip freeze > requirements.txt

### Q8. Command to Install From requirements.txt?

Answer: pip install -r requirements.txt

### Q9. Why Pin Versions?

Answer: To ensure consistent environments.

### Q10. Is pip Used in Django Projects?

Answer: Yes, every Django project uses pip.

# Practice Questions

1. Install Django.
2. Install Requests.
3. Upgrade Django.
4. Uninstall Requests.
5. View installed packages.
6. Generate requirements.txt.
7. Install packages from requirements.txt.
8. Create Django environment.
9. Add Pillow package.
10. Build project dependency file.

# Summary

Important Commands:
pip install
pip uninstall
pip list
pip show
pip freeze
pip install -r requirements.txt
Important Files: requirements.txt

Used In:

* Django
* Flask
* FastAPI
* Enterprise Applications
* Team Projects

Understanding pip and requirements.txt is essential because every professional Python project depends on package management and reproducible environments.
