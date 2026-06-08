# CLASS METHODS IN PYTHON

## What are Class Methods?

A class method is a method that belongs to the class rather than an object.

Normal methods work with: self

Class methods work with: cls

where:
cls = current class

## Why Do We Need Class Methods?

Sometimes we need to access class-level data instead of object-level data.

Example: company = "Google"

This belongs to the class.
Not to individual employees.

# Normal Method Example

class Employee:

    company = "Google"

    def show_company(self):

        print(self.company)

Usage:

employee = Employee()

employee.show_company()

Output: Google
Works.
But this method requires an object.

# Creating a Class Method

Use: @classmethod

Example:

class Employee:

    company = "Google"

    @classmethod
    def show_company(cls):
        print(cls.company)

Usage:

Employee.show_company()

Output: Google
No object required.

# Understanding cls

Example:

class Employee:

    company = "Google"

    @classmethod
    def show_company(cls):

        print(cls)

Output: <class '__main__.Employee'>

cls refers to the current class.

# Accessing Class Variables

class Employee:

    company = "Google"

    @classmethod
    def get_company(cls):

        return cls.company

print(Employee.get_company())

Output: Google

# Modifying Class Variables

class Employee:

    company = "Google"

    @classmethod
    def change_company(cls, name):

        cls.company = name

Usage:

Employee.change_company("Microsoft")

print(Employee.company)

Output: Microsoft

# Multiple Objects Example

class Employee:

    company = "Google"

    @classmethod
    def change_company(cls, company):

        cls.company = company

e1 = Employee()

e2 = Employee()

Employee.change_company("Amazon")

print(e1.company)

print(e2.company)

Output:
Amazon
Amazon

Class variable changed for all objects.

# Factory Method Example

Class methods are often used as alternative constructors.

Example:

class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age

    @classmethod
    def create_default_student(cls):

        return cls("Alex", 25)

Usage:

student = Student.create_default_student()

print(student.name)

Output: Alex

# Real World Example

Employee

class Employee:

    company = "Google"

    def __init__(self, name):

        self.name = name

    @classmethod
    def company_info(cls):

        print(cls.company)

Usage: Employee.company_info()

Output: Google

# Bank Example

class Bank:

    bank_name = "HDFC"

    @classmethod
    def show_bank_name(cls):

        print(cls.bank_name)

Usage: Bank.show_bank_name()

Output: HDFC

# Class Method vs Instance Method

Instance Method: def show(self):

Needs object.
Works with object data.

Class Method: @classmethod

def show(cls):

No object required.
Works with class data.

# Django Example

Django uses class methods extensively.

Example: User.objects.create_user()

Internally many manager methods are implemented using class-level logic.

Another example: MyModel.objects.all()

These patterns rely on class-based behavior.

# Advantages of Class Methods

* Access Class Variables
* Modify Class Variables
* Alternative Constructors
* Cleaner Design

# Interview Questions

### Q1. Which Decorator Creates a Class Method?

Answer: @classmethod

### Q2. What is cls?

Answer: A reference to the current class.

### Q3. Difference Between self and cls?

Answer: self → current object
        cls → current class

### Q4. Can Class Methods Access Class Variables?

Answer: Yes.

### Q5. Can Class Methods Modify Class Variables?

Answer: Yes.

### Q6. Do Class Methods Need Objects?

Answer: No.

### Q7. Why Use Class Methods?

Answer: To work with class-level data and create alternative constructors.

### Q8. What is an Alternative Constructor?

Answer: A class method that creates and returns objects.

### Q9. Where Are Class Methods Used?

Answer: Frameworks like Django, Flask, and enterprise applications.

# Practice Questions

1. Create Employee class with company variable.
2. Create class method to display company.
3. Create class method to update company.
4. Create Bank class.
5. Create School class.
6. Create alternative constructor.
7. Create Product class.
8. Modify class variables using class method.
9. Create Student factory method.
10. Build a company management example.

# Summary

Important Concepts:

* @classmethod
* cls
* Class Variables
* Alternative Constructors

Difference:

Instance Method: self

Class Method: cls

Used In:

* Django Managers
* ORM Operations
* Enterprise Applications
* Framework Development

Class methods allow operations that belong to the class itself rather than individual objects.
