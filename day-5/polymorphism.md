# POLYMORPHISM IN PYTHON

## What is Polymorphism?

The word Polymorphism comes from:

Poly = Many
Morph = Forms

Meaning:
One Interface
Multiple Forms

Polymorphism allows the same method or operation to behave differently depending on the object.

## Real World Example

Think about: Sound()

Dog: Bark

Cat: Meow

Lion: Roar

Same method: sound()

Different behavior.
This is Polymorphism.

## Why Use Polymorphism?

Benefits:

* Flexibility
* Reusability
* Cleaner Code
* Easier Maintenance

Used heavily in large applications.

## Example 1

class Dog:

    def sound(self):

        print("Bark")

class Cat:

    def sound(self):

        print("Meow")


dog = Dog()

cat = Cat()

dog.sound()

cat.sound()

Output:
Bark
Meow

Same method name.
Different behavior.

## Example 2

class Car:

    def move(self):

        print("Driving")


class Plane:

    def move(self):

        print("Flying")


car = Car()

plane = Plane()

car.move()

plane.move()

Output:
Driving
Flying

## Polymorphism with Inheritance

Most common interview example.

class Animal:

    def sound(self):

        print("Animal Sound")


class Dog(Animal):

    def sound(self):

        print("Bark")


class Cat(Animal):

    def sound(self):

        print("Meow")

## Calling Methods

dog = Dog()
cat = Cat()
dog.sound()
cat.sound()

Output:
Bark
Meow

This happens because of method overriding.

## Polymorphism Using Loop

class Dog:

    def sound(self):

        print("Bark")


class Cat:

    def sound(self):

        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:

    animal.sound()

Output:
Bark
Meow

Python automatically calls the correct method.

## Polymorphism with Functions

class Dog:

    def sound(self):

        print("Bark")

class Cat:

    def sound(self):

        print("Meow")

def make_sound(animal):

    animal.sound()

make_sound(Dog())

make_sound(Cat())

Output:
Bark
Meow

Same function.
Different behavior.

## Built-in Polymorphism

Python already uses polymorphism.

Example: print(len("Alex"))

Output: 4

Example: print(len([1, 2, 3, 4]))

Output: 4

Same function: len()

Works differently for strings and lists.

## Another Built-in Example

print(10 + 20)

Output: 30

print("Hello" + " Python")

Output: Hello Python

Same operator: +

Different behavior.
This is polymorphism.

## Real World Example

Employee System

class Developer:

    def work(self):

        print("Writing Code")

class Tester:

    def work(self):

        print("Testing Application")

employees = [
    Developer(),
    Tester()
]

for employee in employees:

    employee.work()

Output:
Writing Code
Testing Application

## Real World Example

Payment Gateway

class CreditCard:

    def pay(self):
        print("Payment Through Credit Card")

class UPI:

    def pay(self):
        print("Payment Through UPI")

Function:

def process_payment(method):

    method.pay()

Usage:

process_payment(CreditCard())
process_payment(UPI())

Output:
Payment Through Credit Card
Payment Through UPI

## Method Overriding and Polymorphism

Example:

class Animal:

    def sound(self):

        print("Animal Sound")

class Dog(Animal):

    def sound(self):

        print("Bark")

Dog overrides parent method.
This creates runtime polymorphism.

## Polymorphism in Django

Django uses polymorphism extensively.

Example:

class APIView:

    def get(self):

        pass

Child Class:

class UserView(APIView):

    def get(self):

        return "User Data"

Different views implement: get()

in different ways.

## Advantages of Polymorphism

* Reusable Code
* Flexible Design
* Easy Extension
* Less Conditional Logic
* Cleaner Architecture

## Interview Questions

### Q1. What is Polymorphism?

Answer: One interface with multiple implementations.

### Q2. Why Use Polymorphism?

Answer: To improve flexibility and code reusability.

### Q3. What is Runtime Polymorphism?

Answer: Method behavior decided during execution.

Example: Method overriding.

### Q4. How is Polymorphism Achieved in Python?

Answer:

Using:

* Method Overriding
* Duck Typing
* Inheritance

### Q5. What is Method Overriding?

Answer: Replacing parent class method in child class.

### Q6. Is len() an Example of Polymorphism?

Answer: Yes.

It behaves differently for different objects.

### Q7. Is + Operator Polymorphic?

Answer: Yes.

Works differently for:

* Numbers
* Strings
* Lists

### Q8. Difference Between Inheritance and Polymorphism?

Inheritance: Acquiring features.

Polymorphism: Using same interface differently.

### Q9. What is Duck Typing?

Answer: If an object behaves like expected, Python accepts it.

Example: If it has: sound()

it can be used.

### Q10. Why is Polymorphism Important?

Answer: It makes systems extensible and maintainable.

## Practice Questions

1. Create Dog and Cat classes.
2. Create Vehicle hierarchy.
3. Create Payment methods.
4. Create Employee hierarchy.
5. Override methods.
6. Use polymorphism in loop.
7. Use polymorphism with function.
8. Demonstrate len().
9. Demonstrate + operator.
10. Build mini notification system.

## Summary

Important Concepts:

* Polymorphism
* Method Overriding
* Runtime Polymorphism
* Duck Typing

Real World Usage:

* Django Views
* REST APIs
* Payment Systems
* Notification Systems
* Enterprise Applications

Polymorphism allows the same interface to support multiple behaviors, making software flexible and scalable.
