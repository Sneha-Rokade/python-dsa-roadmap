# CLASSES AND OBJECTS IN PYTHON

## What is a Class?

A class is a blueprint used to create objects.

Think of a class as a design or template.

Example:

Blueprint: Car

Real Cars:
BMW
Audi
Tesla

Car is a class.

BMW, Audi, Tesla are objects.

## What is an Object?

An object is an instance of a class.

Objects contain actual data.

Example:

Class: Student

Objects:
Alex
John
Emma

All are students but have different information.

## Why Use Classes and Objects?

Benefits:

* Better Organization
* Reusability
* Scalability
* Real World Modeling

Large applications use thousands of objects.

Examples:

* Django User
* Product
* Employee
* Bank Account

## Creating Your First Class

Syntax: class Student:
            pass

Output: Nothing happens because the class is empty.

## Creating an Object

class Student:

    pass

student1 = Student()

print(student1)

Output: <__main__.Student object at memory_address>

An object has been created.

## Adding Attributes

Attributes store data.

Example:
class Student:

    pass

student1 = Student()

student1.name = "Alex"

student1.age = 25

print(student1.name)

print(student1.age)

Output:
Alex
25

## Multiple Objects

class Student:

    pass

student1 = Student()

student1.name = "Alex"

student2 = Student()

student2.name = "John"

print(student1.name)

print(student2.name)

Output:
Alex
John

Each object has its own data.

## Methods in a Class

Methods are functions inside a class.

Example:

class Student:

    def greet(self):

        print("Welcome Student")

student1 = Student()

student1.greet()

Output: Welcome Student

## What is self?

self refers to the current object.

Example:

class Student:

    def show(self):

        print("Inside Object")

student1 = Student()

student1.show()

Python automatically passes the current object to self.

## Using self with Attributes

class Student:

    def show_details(self):

        print(self.name)

        print(self.age)

student1 = Student()

student1.name = "Alex"

student1.age = 25

student1.show_details()

Output:
Alex
25

## Real World Example

Employee System

class Employee:

    def display(self):

        print(self.name)

        print(self.salary)

employee1 = Employee()

employee1.name = "Alex"

employee1.salary = 80000

employee1.display()

Output:
Alex
80000

## Real World Example

Bank Account

class BankAccount:

    def show_balance(self):

        print(self.balance)

account = BankAccount()

account.balance = 50000

account.show_balance()

Output: 50000

## Class Attribute

Shared by all objects.

class Employee:

    company = "Google"

employee1 = Employee()

employee2 = Employee()

print(employee1.company)

print(employee2.company)

Output:
Google
Google

## Object Attribute

Unique for each object.

class Employee:

    company = "Google"

employee1 = Employee()

employee1.name = "Alex"

employee2 = Employee()

employee2.name = "John"

print(employee1.name)

print(employee2.name)

Output:
Alex
John

## Difference Between Class Attribute and Object Attribute

Class Attribute:

Shared by all objects.

Example: company = "Google"

Object Attribute: Unique per object.

Example: name = "Alex"

## Real World Example

Product

class Product:

    category = "Electronics"

product1 = Product()

product1.name = "Laptop"

product1.price = 50000

print(product1.name)

print(product1.price)

print(product1.category)

Output: Laptop
        50000
        Electronics

## Django Example

Django Models are Classes.

class User:

    pass

Django Model:

class User(models.Model):

    name = models.CharField(max_length=100)

Understanding classes makes Django much easier.

## Interview Questions

### Q1. Why Use Classes?

Answer: To organize code and model real-world entities.

### Q2. What is self?

Answer: A reference to the current object.

### Q3. Difference Between Function and Method?

Function: Independent.

Method: Inside a class.

### Q4. What is an Attribute?

Answer: A variable belonging to an object or class.

### Q5. Difference Between Class Attribute and Object Attribute?

Class Attribute: Shared by all objects.

Object Attribute: Unique for each object.

### Q8. Can a Class Have Multiple Objects?

Answer: Yes.
A class can create unlimited objects.

### Q9. What is a Method?

Answer: A function defined inside a class.

### Q10. Why is OOP Important?

Answer: Because large applications are built using classes and objects.

## Practice Questions

1. Create a Student class.
2. Create an Employee class.
3. Create a Product class.
4. Create a BankAccount class.
5. Add attributes to objects.
6. Create methods.
7. Use self keyword.
8. Create multiple objects.
9. Create class attributes.
10. Create object attributes.

## Summary

Important Concepts:

* Class
* Object
* Attribute
* Method
* self
* Class Attribute
* Object Attribute

Real World Usage:

* Django Models
* User Systems
* Banking Applications
* E-Commerce Applications
* Enterprise Software
