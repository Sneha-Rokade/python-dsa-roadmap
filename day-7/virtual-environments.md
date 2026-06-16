# VIRTUAL ENVIRONMENTS IN PYTHON

## What is a Virtual Environment?

A Virtual Environment is an isolated Python environment.

It allows each project to have:
* Its own packages
* Its own dependencies
* Its own Python libraries
Without affecting other projects.

# Why Do We Need Virtual Environments?

Suppose:

Project A uses: Django 4.2
Project B uses: Django 5.0
Installing both globally can create conflicts.
Virtual environments solve this problem.

# Real World Example

Imagine:
Laptop
│
├── Project A
│   └── Django 4.2
│
├── Project B
│   └── Django 5.0
│
└── Project C
    └── Flask
Each project remains isolated.

# Check Python Version

Before creating environment: python --version

Output: Python 3.12.0

# Create Virtual Environment

Syntax: python -m venv venv

Explanation:

python      -> Python Interpreter
-m venv     -> Virtual Environment Module
venv        -> Environment Name

# Project Structure

After creation:
project/

├── venv/
│
├── app.py
│
└── requirements.txt

# Activate Virtual Environment

## Windows

venv\Scripts\activate
Output: (venv) C:\project>
Notice: (venv)
This means environment is active.

## Linux / Mac

source venv/bin/activate`
Output: (venv) user@machine

# Verify Environment

Check Python path: where python
Windows Output: project\venv\Scripts\python.exe
Linux: which python

# Install Package

Example: pip install django
Installed only inside virtual environment.
Not globally.

# Check Installed Packages

pip list

Output:
Django
asgiref
sqlparse

# Deactivate Environment

Command: deactivate
Output: C:\project>
No: (venv)
Environment deactivated.

# Create Environment with Custom Name

Example: python -m venv myenv

Structure:
project/

├── myenv/
│
└── app.py

# Multiple Virtual Environments

Example:

project/

├── backend-env/
│
├── testing-env/
│
└── production-env/

Possible but not common.

Usually: venv/
is preferred.

# Installing Multiple Packages

Example: pip install django requests
Installed inside current environment.

# Why Not Install Globally?

Bad: pip install django
outside virtual environment.

Problems:

* Version conflicts
* Dependency issues
* Difficult maintenance

# REQUIREMENTS FILE

Export installed packages:
pip freeze > requirements.txt

Generated:
Django==5.0.7
asgiref==3.8.1
sqlparse==0.5.1

Very important.

# Install from requirements.txt

Another developer can run: pip install -r requirements.txt
All packages installed automatically.

# Real World Team Workflow

Developer A: pip freeze > requirements.txt
Pushes to GitHub.

Developer B: git clone project
pip install -r requirements.txt

Same setup.

# Django Project Setup

Step 1: python -m venv venv

Step 2: venv\Scripts\activate

Step 3: pip install django

Step 4: django-admin startproject config .
This is how every Django project starts.

# Git Ignore Virtual Environment

Never push: venv/
to GitHub.

Add: venv/
to: .gitignore

# Correct GitHub Structure

project/

├── app/
├── config/
├── requirements.txt
├── .gitignore
└── README.md

No: venv/
inside repository.

# Common Commands

Create: python -m venv venv
Activate: venv\Scripts\activate
Deactivate: deactivate
Install: pip install django
Freeze: pip freeze > requirements.txt

Install Requirements: pip install -r requirements.txt

# Common Mistakes

## Forgetting Activation

Bad: pip install django
before activating.
Packages install globally.

## Pushing venv to GitHub

Bad: venv/
inside repository.
Huge repository size.

## Forgetting requirements.txt

Team members cannot install dependencies.

# Best Practices

### Use One Environment Per Project

Good:
career-accelerator-platform/
│
└── venv/

### Keep requirements.txt Updated

Run: pip freeze > requirements.txt
after new installations.

### Add venv to .gitignore

Always.

# Career Accelerator Platform Example

Structure: career-accelerator-platform/

├── backend/
│
├── frontend/
│
├── venv/
│
├── requirements.txt
│
└── README.md

During development: python -m venv venv
venv\Scripts\activate
pip install django

# Interview Questions

### Q1. What is a Virtual Environment?

Answer: An isolated Python environment for managing project dependencies.

### Q2. Why Use Virtual Environments?

Answer: To avoid dependency conflicts.

### Q3. Command to Create Environment?

Answer: python -m venv venv

### Q4. Command to Activate?

Windows: venv\Scripts\activate

### Q5. Command to Deactivate?

Answer: deactivate

### Q6. Why Use requirements.txt?

Answer: To share project dependencies.

### Q7. Command to Generate requirements.txt?

Answer: pip freeze > requirements.txt

### Q8. Should venv Be Pushed to GitHub?

Answer: No.

### Q9. Which Tool Creates Virtual Environments?

Answer: venv

### Q10. Is Virtual Environment Required for Django?

Answer: Strongly recommended and used in almost every professional project.

# Practice Questions

1. Create virtual environment.
2. Activate environment.
3. Install Django.
4. Install Requests.
5. Generate requirements.txt.
6. Remove environment.
7. Create custom environment name.
8. Install requirements from file.
9. Configure .gitignore.
10. Setup Django project using virtual environment.

# Summary

Important Concepts:

* Virtual Environment
* Dependency Isolation
* Package Management
* requirements.txt
* pip

Important Commands:

python -m venv venv
venv\Scripts\activate
deactivate
pip install package
pip freeze > requirements.txt
pip install -r requirements.txt

Used In:

* Django
* Flask
* FastAPI
* Enterprise Projects
* Team Development

Virtual environments are a mandatory skill for professional Python development because every real-world project depends on dependency isolation and reproducible setups.
