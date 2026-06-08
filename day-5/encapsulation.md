# ENCAPSULATION IN PYTHON

## What is Encapsulation?

Encapsulation is the process of bundling:
* Data (Variables)
* Methods (Functions)

into a single unit (Class) and controlling access to that data.

Simple definition:

Protect object data from direct modification.

## Real World Example

Think of a Bank Account.

You cannot directly modify: Bank Balance

Instead, you use:
Deposit()
Withdraw()
CheckBalance()

The data is protected.

This is Encapsulation.

## Why Use Encapsulation?

Benefits:

* Data Security
* Controlled Access
* Better Maintainability
* Cleaner Code

Used heavily in enterprise applications.

## Without Encapsulation

class Employee:

    def __init__(self):

        self.salary = 50000

employee = Employee()
employee.salary = -100000

print(employee.salary)

Output: -100000

Problem: Invalid data can be assigned.

## With Encapsulation

Instead of modifying directly: employee.salary

Use methods.

class Employee:

    def __init__(self):

        self.salary = 50000

    def set_salary(self, salary):

        if salary > 0:

            self.salary = salary

    def get_salary(self):

        return self.salary

## Accessing Through Methods

employee = Employee()

employee.set_salary(80000)

print(employee.get_salary())

Output: 80000

Now data is controlled.

# Access Modifiers in Python

Python provides:

1. Public
2. Protected
3. Private

# Public Members

Accessible from anywhere.

Example:

class Student:

    def __init__(self):

        self.name = "Alex"

student = Student()

print(student.name)

Output: Alex

Public members are the default.

# Protected Members

Single underscore: _name

Example:

class Student:

    def __init__(self):

        self._age = 25

student = Student()

print(student._age)

Output: 25

Protected means:

Use internally
Not intended for direct access

Still accessible.

# Private Members

Double underscore:__salary

Example:

class Employee:

    def __init__(self):

        self.__salary = 50000

## Accessing Private Variable

employee = Employee()

print(employee.__salary)

Output: AttributeError

Private members cannot be accessed directly.

## Accessing Private Data Through Method

class Employee:

    def __init__(self):

        self.__salary = 50000

    def get_salary(self):

        return self.__salary

employee = Employee()

print(employee.get_salary())

Output: 50000

This is proper encapsulation.

## Updating Private Variable

class Employee:

    def __init__(self):

        self.__salary = 50000

    def set_salary(self, salary):

        if salary > 0:

            self.__salary = salary

    def get_salary(self):

        return self.__salary

Usage:

employee = Employee()

employee.set_salary(90000)

print(employee.get_salary())

Output: 90000

## Private Methods

Methods can also be private.

class Employee:

    def __private_method(self):

        print("Private Method")

Calling directly:

employee.__private_method()

Output: AttributeError

## Real World Example

Bank Account

class BankAccount:

    def __init__(self):

        self.__balance = 10000

    def deposit(self, amount):

        self.__balance += amount

    def get_balance(self):

        return self.__balance

Usage:

account = BankAccount()

account.deposit(5000)

print(account.get_balance())

Output: 15000

Balance is protected.

## Real World Example

Student Marks

class Student:

    def __init__(self):

        self.__marks = 0

    def set_marks(self, marks):

        if 0 <= marks <= 100:

            self.__marks = marks

    def get_marks(self):

        return self.__marks

Usage:

student = Student()

student.set_marks(85)

print(student.get_marks())

Output: 85

## Name Mangling

Python internally changes: __salary

to:_Employee__salary

This is called: Name Mangling

Example:

class Employee:

    def __init__(self):

        self.__salary = 50000


employee = Employee()

print(employee._Employee__salary)

Output: 50000

Possible but not recommended.

## Encapsulation in Django

Example:

class User:

    def __init__(self):

        self.__password = "secret"

Password should never be exposed publicly.

Encapsulation protects sensitive information.

## Advantages of Encapsulation

* Data Hiding
* Security
* Controlled Access
* Reduced Complexity
* Better Maintenance

## Interview Questions

### Q1. What is Encapsulation?

Answer: Encapsulation is wrapping data and methods into a class while controlling access to the data.

### Q2. Why Use Encapsulation?

Answer: To protect data and prevent unauthorized access.

### Q3. What Are Access Modifiers?

Answer:

* Public
* Protected
* Private

### Q4. What is a Public Variable?

Answer: Accessible from anywhere.

### Q5. What is a Protected Variable?

Answer: Variable prefixed with: _variable Intended for internal use.

### Q6. What is a Private Variable?

Answer: Variable prefixed with: __variable Cannot be accessed directly.

### Q7. What is Name Mangling?

Answer: Python internally changes private variable names to avoid accidental access.

### Q8. How Do You Access Private Data?

Answer: Using getter and setter methods.

### Q9. Can Methods Be Private?

Answer: Yes.

Using:__method()

### Q10. Why is Encapsulation Important?

Answer: Because it improves security and maintainability.

## Practice Questions

1. Create Employee class with private salary.
2. Create Student class with private marks.
3. Create BankAccount class.
4. Create getter method.
5. Create setter method.
6. Use protected variable.
7. Use public variable.
8. Create private method.
9. Validate data using setter.
10. Build mini ATM system.

## Summary

Important Concepts:

* Encapsulation
* Data Hiding
* Public Members
* Protected Members
* Private Members
* Getter Methods
* Setter Methods
* Name Mangling

Real World Usage:

* Banking Applications
* Authentication Systems
* Django Models
* APIs
* Enterprise Applications

Encapsulation protects data and ensures that objects are modified in a controlled and secure manner.
