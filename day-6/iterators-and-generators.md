# ITERATORS AND GENERATORS IN PYTHON

## What is an Iterator?

An iterator is an object that allows us to traverse elements one at a time.

Python uses iterators internally for:

* Lists
* Tuples
* Sets
* Dictionaries
* Strings

Example: numbers = [10, 20, 30]

for num in numbers:

    print(num)

Output:
10
20
30

Behind the scenes, Python uses an iterator.

# Iterable vs Iterator

## Iterable

An object that can produce an iterator.

Examples:
list
tuple
set
string
dictionary

Example: numbers = [1, 2, 3]
List is iterable.

## Iterator

An object that remembers its current position.

Created using: iter()

Example: numbers = [1, 2, 3]

iterator = iter(numbers)

print(iterator)

Output: <list_iterator object>

# next()

Used to get the next value.

Example: numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

Output:
10
20
30

## What Happens After Last Element?

Example: print(next(iterator))

Output: StopIteration

Iterator has no more values.

# How for Loop Works Internally

This:
for num in numbers:

    print(num)

Internally becomes:
iterator = iter(numbers)

while True:

    try:
        print(next(iterator))
    except StopIteration:
        break

Very common interview question.

# Creating Custom Iterator

Example:

class Counter:

    def __init__(self):

        self.current = 1

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= 5:

            value = self.current

            self.current += 1

            return value

        raise StopIteration

Usage: counter = Counter()
for num in counter:

    print(num)

Output:
1
2
3
4
5

# Problems with Iterators

Custom iterators require:

__iter__()
__next__()

More code.
Less readable.

Solution: Generators

# What is a Generator?

A generator is a simpler way to create iterators.

Instead of: return

Generators use: yield

# First Generator Example

def numbers():

    yield 1
    yield 2
    yield 3

Usage: gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))

Output:
1
2
3

# Understanding yield

Normal Function:

def greet():

    return "Hello"

Returns once and ends.

Generator:
def greet():

    yield "Hello"
    yield "World"

Pauses execution after every yield.

# Generator with Loop

Example:

def count():

    for i in range(1, 6):
        yield i

Usage:

for num in count():

    print(num)

Output:
1
2
3
4
5

# Generator vs List

List: numbers = [1, 2, 3, 4, 5]

Stores all values in memory.

Generator:
def numbers():

    yield 1
    yield 2
    yield 3

Generates values when needed.
Memory efficient.

# Memory Advantage

List: numbers = list(range(1000000))

Consumes memory immediately.

Generator:
def generate_numbers():

    for i in range(1000000):

        yield i

Values created only when needed.

# Real World Example

Reading Large Files

Bad: data = file.readlines()

Loads entire file.

Better:
for line in file:

    print(line)

Uses iteration.
Efficient.

# Generator Expression

Like list comprehension.

List: squares = [x*x for x in range(5)]

Generator: squares = (x*x for x in range(5))

Usage:

for num in squares:

    print(num)

Output:
0
1
4
9
16

# Real World Example

API Data Streaming

def stream_data():

    while True:

        yield get_next_record()

Large applications stream data using generators.

# Django Example

Django QuerySets are lazy.

Example: users = User.objects.all()
Data is not immediately loaded.
This concept is similar to generators.

# Advantages of Generators

* Memory Efficient
* Faster for Large Data
* Lazy Evaluation
* Cleaner Code

# Interview Questions

### Q1. What is an Iterator?

Answer: An object that allows sequential traversal of data.

### Q2. Which Functions Create and Use Iterators?

Answer:
iter()
next()

### Q3. What is StopIteration?

Answer: Exception raised when iterator has no more elements.

### Q4. What is a Generator?

Answer: A function that uses yield to produce values one at a time.

### Q5. Difference Between return and yield?

Answer:
return: Ends function.

yield: Pauses function.

### Q6. Why Use Generators?

Answer: To save memory and process large datasets efficiently.

### Q7. Are Generators Iterators?

Answer: Yes.

Every generator is an iterator.

### Q8. What is Lazy Evaluation?

Answer: Values are generated only when needed.

### Q9. What is a Generator Expression?

Answer: Generator version of list comprehension.

### Q10. Where Are Generators Used?

Answer:

* Data Processing
* File Reading
* APIs
* Django QuerySets
* Streaming Systems

# Practice Questions

1. Create custom iterator.
2. Use iter().
3. Use next().
4. Create number generator.
5. Create square generator.
6. Create even number generator.
7. Create countdown generator.
8. Create generator expression.
9. Read file using iteration.
10. Build mini data stream generator.

# Summary

Important Concepts:

* Iterable
* Iterator
* iter()
* next()
* StopIteration
* Generator
* yield
* Generator Expressions

Used In:

* Django
* APIs
* Data Engineering
* Large File Processing
* Streaming Applications

Generators are one of Python's most powerful features for writing memory-efficient and scalable applications.
