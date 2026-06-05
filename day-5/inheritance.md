# INHERITANCE IN PYTHON

## What is Inheritance?

Inheritance is an OOP feature that allows one class to acquire properties and methods from another class.

It promotes:

* Code Reusability
* Maintainability
* Scalability

## Real World Example

Think of: Animal

Animals can:

* Eat
* Sleep

Now:
Dog
Cat
Lion

All can:

* Eat
* Sleep

Instead of writing the same code repeatedly, we inherit it.

## Parent and Child Class

Parent Class: Animal

Child Class: Dog

Dog inherits properties from Animal.

## Basic Inheritance Syntax

class Parent:

    pass


class Child(Parent):

    pass

## Example 1

class Animal:

    def eat(self):

        print("Animal is eating")


class Dog(Animal):

    pass


dog = Dog()

dog.eat()

Output: Animal is eating

Dog inherited the eat() method.

## Why Inheritance?

Without Inheritance:

class Dog:

    def eat(self):

        print("Animal is eating")


class Cat:

    def eat(self):

        print("Animal is eating")

Code duplication.

With inheritance:

class Animal:

    def eat(self):

        print("Animal is eating")

Reuse everywhere.

## Parent Class Attributes

class Animal:

    species = "Mammal"


class Dog(Animal):

    pass


dog = Dog()

print(dog.species)

Output: Mammal

Child class inherits attributes too.

## Parent Constructor

class Animal:

    def __init__(self):

        print("Animal Created")


class Dog(Animal):

    pass


dog = Dog()

Output: Animal Created

Parent constructor is inherited.

## Child Class with Its Own Method

class Animal:

    def eat(self):

        print("Eating")


class Dog(Animal):

    def bark(self):

        print("Barking")


dog = Dog()

dog.eat()

dog.bark()

Output: Eating
Barking

Dog can use both methods.

## Method Overriding

Child class can replace parent method.

class Animal:
    def sound(self):

        print("Animal Sound")


class Dog(Animal):

    def sound(self):

        print("Bark")


dog = Dog()

dog.sound()

Output: Bark

This is called Method Overriding.

## Using super()

super() allows access to parent class methods.

Example:

class Animal:

    def sound(self):

        print("Animal Sound")


class Dog(Animal):

    def sound(self):

        super().sound()

        print("Bark")


dog = Dog()
dog.sound()

Output:
Animal Sound
Bark

## Parent Constructor with super()

class Animal:

    def __init__(self, name):

        self.name = name


class Dog(Animal):

    def __init__(self, name):

        super().__init__(name)


dog = Dog("Rocky")

print(dog.name)

Output: Rocky

Very important interview topic.

## Single Inheritance

One parent.

class Animal:

    pass


class Dog(Animal):
    pass

Most common type.

## Multilevel Inheritance

class Animal:

    pass


class Mammal(Animal):

    pass


class Dog(Mammal):

    pass

Hierarchy:

Animal
   ↓
Mammal
   ↓
Dog

## Multiple Inheritance

class Father:

    pass


class Mother:

    pass


class Child(Father, Mother):

    pass

Child inherits from multiple parents.

## Hierarchical Inheritance

class Animal:

    pass


class Dog(Animal):

    pass


class Cat(Animal):

    pass

One parent.
Multiple children.

## Real World Example

Employee System

class Employee:

    def work(self):

        print("Employee Working")


class Developer(Employee):

    pass


dev = Developer()

dev.work()

Output: Employee Working

## Real World Example

Vehicle System

class Vehicle:

    def start(self):

        print("Vehicle Started")


class Car(Vehicle):

    pass


car = Car()

car.start()

Output: Vehicle Started

## Django Example

Django uses inheritance extensively.

Example:

class BaseModel(models.Model):

    created_at = models.DateTimeField()

    updated_at = models.DateTimeField()

Then:

class User(BaseModel):

    name = models.CharField(max_length=100)

User inherits fields from BaseModel.

## Advantages of Inheritance

* Code Reusability
* Less Duplication
* Easier Maintenance
* Better Organization

## Interview Questions

### Q1. What is Inheritance?

Answer: Inheritance allows one class to acquire properties and methods from another class.

### Q2. Why Use Inheritance?

Answer: To promote code reusability and reduce duplication.

### Q3. What is a Parent Class?

Answer: The class whose properties are inherited.

### Q4. What is a Child Class?

Answer: The class that inherits from another class.

### Q5. What is Method Overriding?

Answer: Replacing a parent method in the child class.

### Q6. What is super()?

Answer: Used to access parent class methods and constructors.

### Q7. Types of Inheritance?

Answer:

* Single
* Multilevel
* Multiple
* Hierarchical

### Q8. Can Child Access Parent Methods?

Answer: Yes.

### Q9. Can Child Override Parent Methods?

Answer: Yes.

## Practice Questions

1. Create Animal and Dog classes.
2. Create Vehicle and Car classes.
3. Create Employee and Developer classes.
4. Override a method.
5. Use super().
6. Create multilevel inheritance.
7. Create multiple inheritance.
8. Create hierarchical inheritance.
9. Inherit constructor.
10. Build a mini employee hierarchy.

## Summary

Important Concepts:

* Parent Class
* Child Class
* Inheritance
* Method Overriding
* super()
* Single Inheritance
* Multiple Inheritance
* Multilevel Inheritance

Used In:

* Django Models
* Django Views
* Django Forms
* REST APIs
* Enterprise Applications

