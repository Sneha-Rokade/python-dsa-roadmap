# ABSTRACTION IN PYTHON

## What is Abstraction?

Abstraction means: Showing only essential details
and hiding implementation details.

Simple definition:

The user knows what an object does, but does not need to know how it does it.

## Real World Example

Think about a Car.

You know:

Start Car
Stop Car
Accelerate Car

But you don't need to know:

Engine Internals
Fuel Injection
Gear Mechanism

Those details are hidden.
This is Abstraction.

## Another Example

ATM Machine

You know:

Withdraw Money
Check Balance
Deposit Money

You don't know:

Database Queries
Network Calls
Bank Server Logic

Those details are hidden.

## Why Use Abstraction?

Benefits:

* Reduces Complexity
* Improves Security
* Easier Maintenance
* Cleaner Code

Large applications rely heavily on abstraction.

## Abstraction in Python

Python provides abstraction using: ABC and abstractmethod

from: abc module

## Importing ABC Module

from abc import ABC, abstractmethod

## Creating Abstract Class

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):

        pass

Animal becomes an abstract class.

## What is an Abstract Method?

A method declared but not implemented.

Example: 
@abstractmethod
def sound(self):

    pass

No implementation.
Child classes must implement it.

## Creating Child Class

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):

        pass


class Dog(Animal):

    def sound(self):

        print("Bark")

## Using Abstract Class

dog = Dog()
dog.sound()

Output: Bark

## Cannot Create Abstract Class Object

animal = Animal()

Output: TypeError

Reason: Abstract classes are incomplete.

## Child Must Implement Abstract Method

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):

        pass

class Dog(Animal):

    pass

Output: TypeError

Dog must implement: sound()

## Real World Example

Payment System

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):

        pass

## Credit Card Implementation

class CreditCard(Payment):

    def pay(self):

        print("Payment Through Credit Card")

## UPI Implementation

class UPI(Payment):

    def pay(self):

        print("Payment Through UPI")

Usage:

payment = UPI()

payment.pay()

Output: Payment Through UPI

## Real World Example

Employee System

from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def work(self):

        pass

## Developer

class Developer(Employee):

    def work(self):

        print("Writing Code")

## Tester

class Tester(Employee):

    def work(self):

        print("Testing Application")

Usage:
developer = Developer()

developer.work()

Output: Writing Code

## Abstraction vs Encapsulation

Encapsulation: Hides Data

Example:__salary

Abstraction: Hides Implementation

Example: withdraw()

User knows what it does.
Not how it works internally.

## Abstraction in Django

Django Developers use:

models.Model

Example:

class User(models.Model):

    name = models.CharField(max_length=100)

You use:

save()
delete()
filter()

without knowing internal implementation.
This is abstraction.

## Advantages of Abstraction

* Cleaner Design
* Better Security
* Easier Maintenance
* Better Scalability
* Reduced Complexity

## Interview Questions

### Q1. What is Abstraction?

Answer: Abstraction hides implementation details and exposes only essential functionality.

### Q2. Why Use Abstraction?

Answer: To reduce complexity and improve maintainability.

### Q3. How is Abstraction Achieved in Python?

Answer:

Using: ABC
and
@abstractmethod

### Q4. What is an Abstract Class?

Answer: A class containing one or more abstract methods.

### Q5. Can We Create an Object of an Abstract Class?

Answer: No.

### Q6. What is an Abstract Method?

Answer: A method declared but not implemented.

### Q7. Must Child Classes Implement Abstract Methods?

Answer: Yes.

### Q8. Which Module Provides Abstraction?

Answer: abc

### Q9. Why is Abstraction Important?

Answer: It simplifies complex systems and provides a clean interface.

## Practice Questions

1. Create Animal abstract class.
2. Create Dog implementation.
3. Create Cat implementation.
4. Create Payment system.
5. Create Employee hierarchy.
6. Create Vehicle abstraction.
7. Create Notification abstraction.
8. Create Banking abstraction.
9. Create Shape abstraction.
10. Create Report Generator abstraction.

## Summary

Important Concepts:

* Abstraction
* Abstract Class
* Abstract Method
* ABC
* @abstractmethod

Real World Usage:

* Django ORM
* Payment Gateways
* Banking Systems
* Enterprise Applications
* APIs

Abstraction allows developers to work with complex systems through simple interfaces while hiding internal implementation details.
