# PROPERTY DECORATORS IN PYTHON

## What is a Property Decorator?

Property decorators allow methods to be accessed like attributes.

Without property: person.get_name()

With property: person.name

Cleaner and more Pythonic.

## Why Use Property Decorators?

Benefits:

* Encapsulation
* Data Validation
* Cleaner Syntax
* Better Control Over Attributes

Used heavily in professional Python applications.

## Problem Without Property

Example:

class Person:

    def __init__(self, name):

        self._name = name

    def get_name(self):

        return self._name


person = Person("Alex")

print(person.get_name())

Output: Alex
Works, but looks like Java-style code.

## Using @property

Example:

class Person:

    def __init__(self, name):

        self._name = name

    @property
    def name(self):

        return self._name

Usage:

person = Person("Alex")
print(person.name)

Output: Alex

Notice: person.name

instead of: person.get_name()

# Read-Only Property

Example:

class Employee:

    def __init__(self, salary):

        self._salary = salary

    @property
    def salary(self):

        return self._salary

Usage:
employee = Employee(50000)

print(employee.salary)

Output: 50000

## Problem

Trying to modify: employee.salary = 80000

Output: AttributeError

Because property is read-only.

# Property Setter

Use: @property_name.setter

Example:

class Employee:

    def __init__(self, salary):

        self._salary = salary

    @property
    def salary(self):

        return self._salary

    @salary.setter
    def salary(self, value):

        self._salary = value

Usage:
employee = Employee(50000)
employee.salary = 80000
print(employee.salary)

Output: 80000

# Property Validation

Very common interview example.

class Employee:

    def __init__(self, salary):

        self._salary = salary

    @property
    def salary(self):

        return self._salary

    @salary.setter
    def salary(self, value):

        if value > 0:

            self._salary = value

Usage:
employee = Employee(50000)
employee.salary = -100

Salary will not update.
Invalid data is prevented.

# Property Deleter

Use: @property_name.deleter

Example: class Employee:

    def __init__(self, name):

        self._name = name

    @property
    def name(self):

        return self._name

    @name.deleter
    def name(self):

        del self._name

Usage:
employee = Employee("Alex")
del employee.name

Property deleted.

# Full Property Example

class Student:

    def __init__(self, marks):

        self._marks = marks

    @property
    def marks(self):

        return self._marks

    @marks.setter
    def marks(self, value):

        if 0 <= value <= 100:

            self._marks = value

    @marks.deleter
    def marks(self):

        del self._marks

Usage:
student = Student(85)
student.marks = 90
print(student.marks)

Output: 90

# Real World Example

Temperature Converter

class Temperature:

    def __init__(self, celsius):

        self._celsius = celsius

    @property
    def fahrenheit(self):

        return (self._celsius * 9/5) + 32

Usage:
temp = Temperature(25)
print(temp.fahrenheit)

Output: 77.0

Method behaves like attribute.

# Real World Example

User Age Validation

class User:

    def __init__(self):

        self._age = 0

    @property
    def age(self):

        return self._age

    @age.setter
    def age(self, value):

        if value >= 18:

            self._age = value

Usage:
user = User()
user.age = 25
print(user.age)

Output: 25

# Why Use Underscore?

Example: self._salary

Convention: Internal Variable

Property exposes: salary
to users.

# Property vs Getter/Setter Methods

Traditional:
employee.get_salary()
employee.set_salary()

Pythonic:
employee.salary
Cleaner and preferred.

# Django Example

Django models often use properties.

Example:

class User(models.Model):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    @property
    def full_name(self):

        return f"{self.first_name} {self.last_name}"

Usage: user.full_name

Looks like an attribute.
Actually executes code.

# Advantages of Property Decorators

* Cleaner Syntax
* Encapsulation
* Validation
* Read-Only Fields
* Computed Attributes

# Interview Questions

### Q1. What is @property?

Answer: A decorator that allows methods to be accessed like attributes.

### Q2. Why Use @property?

Answer: To provide controlled access to object data.

### Q3. What is a Property Setter?

Answer: A method that controls updates to a property.

### Q4. What is a Property Deleter?

Answer: A method that controls deletion of a property.

### Q5. Can Properties Be Read-Only?

Answer: Yes.
If no setter is defined.

### Q6. Why Use Underscore Variables?

Answer: To indicate internal/private data.

### Q7. Difference Between Property and Method?

Answer:

Property: person.name

Method: person.get_name()

### Q8. Can Properties Validate Data?

Answer: Yes.
Using setters.

### Q9. Where Are Properties Used?

Answer: Django models, APIs, enterprise applications.

### Q10. Why Are Properties Important?

Answer: They combine encapsulation with clean syntax.

# Practice Questions

1. Create Employee salary property.
2. Create Student marks property.
3. Create User age validation.
4. Create Temperature converter.
5. Create Product price validation.
6. Create BankAccount balance property.
7. Create read-only property.
8. Create property deleter.
9. Create full_name property.
10. Build mini employee system.

# Summary

Important Concepts:

* @property
* @setter
* @deleter
* Read-Only Properties
* Validation

Used In:

* Django Models
* APIs
* Enterprise Applications
* Validation Systems

Property decorators allow methods to behave like attributes while maintaining full control over data access and validation.
