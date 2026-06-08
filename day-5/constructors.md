# CONSTRUCTORS IN PYTHON

## What is a Constructor?

A constructor is a special method that automatically executes when an object is created.

In Python, the constructor is: __init__()

The word init stands for: Initialization

## Why Do We Need Constructors?

Without Constructor:

class Student:

    pass

student1 = Student()

student1.name = "Alex"

student1.age = 25

Problem: We must manually assign values every time.

## Constructor Solution

class Student:

    def __init__(self):

        print("Student Object Created")

student1 = Student()

Output: Student Object Created

The constructor runs automatically.

## Constructor Syntax

class ClassName:

    def __init__(self):

        pass

Rules:

* Must be named **init**
* First parameter must be self
* Executes automatically

## Constructor with Attributes

class Student:

    def __init__(self):

        self.name = "Alex"

        self.age = 25

student1 = Student()

print(student1.name)

print(student1.age)

Output:
Alex
25

## Constructor with Parameters

Most common usage.

class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age

student1 = Student("Alex", 25)

print(student1.name)

print(student1.age)

Output:
Alex
25

## Multiple Objects

class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age

student1 = Student("Alex", 25)

student2 = Student("John", 30)

print(student1.name)

print(student2.name)

Output:
Alex
John

Each object stores different data.

## Understanding self

Example:

class Student:

    def __init__(self, name):

        self.name = name

When: student1 = Student("Alex")

Python internally does: student1.__init__("Alex")

self refers to: student1

## Constructor + Method

class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def display(self):

        print(self.name)

        print(self.age)

student1 = Student("Alex", 25)

student1.display()

Output:
Alex
25

## Real World Example

Employee

class Employee:

    def __init__(self, name, salary):

        self.name = name

        self.salary = salary

employee1 = Employee("Alex", 80000)

print(employee1.name)

print(employee1.salary)

Output:
Alex
80000

## Real World Example

Bank Account

class BankAccount:

    def __init__(self, account_holder, balance):

        self.account_holder = account_holder

        self.balance = balance

account = BankAccount("Alex", 50000)

print(account.account_holder)

print(account.balance)

Output:
Alex
50000

## Default Values in Constructor

class Employee:

    def __init__(self, name, salary=30000):

        self.name = name
        self.salary = salary

employee1 = Employee("Alex")

print(employee1.salary)

Output: 30000

## Constructor with Multiple Parameters

class Product:

    def __init__(self, name, price, quantity):

        self.name = name

        self.price = price

        self.quantity = quantity

product = Product(
    "Laptop",
    50000,
    10
)

print(product.name)

Output: Laptop

## What Happens If We Don't Create Constructor?

Python provides a default constructor.

Example:

class Student:

    pass

student1 = Student()

Works successfully.

Python automatically creates a simple constructor.

## Types of Constructors

### Default Constructor

class Student:

    def __init__(self):

        print("Student Created")

No parameters.

### Parameterized Constructor

class Student:

    def __init__(self, name):

        self.name = name

Accepts parameters.
Most common type.

## Constructor vs Method

Constructor: __init__()

Runs automatically.

Method: display()

Must be called manually.

Example: student.display()

## Real Django Example

Django internally creates model objects.

Example:

user = User(

    username="alex",

    email="alex@gmail.com"
)

This uses constructors behind the scenes.

## Interview Questions

### Q1. What is a Constructor?

Answer: A special method that automatically executes when an object is created.

### Q2. What is the Name of Constructor in Python?

Answer: __init__()

### Q3. Why Use Constructors?

Answer: To initialize object attributes automatically.

### Q4. Does Constructor Return Anything?

Answer: No.

Constructors initialize objects.

### Q5. Can Constructor Accept Parameters?

Answer: Yes.

Parameterized constructors are very common.

### Q6. What is self?

Answer: Reference to the current object.

### Q7. Difference Between Constructor and Method?

Constructor: Runs automatically.

Method: Called manually.

### Q8. Can a Class Exist Without Constructor?

Answer: Yes.
Python provides a default constructor.

### Q9. Types of Constructors?

Answer:

1. Default Constructor
2. Parameterized Constructor

### Q10. When Does Constructor Execute?

Answer: Automatically during object creation.

## Practice Questions

1. Create Student class with constructor.
2. Create Employee class with constructor.
3. Create Product class.
4. Create BankAccount class.
5. Use multiple parameters.
6. Use default values.
7. Create display method.
8. Create multiple objects.
9. Print object details.
10. Create Library class with constructor.

## Summary

Important Concepts:

* Constructor
* **init**()
* self
* Initialization
* Default Constructor
* Parameterized Constructor

Used In:

* Django Models
* APIs
* Backend Applications
* Enterprise Software
* AI/ML Projects
