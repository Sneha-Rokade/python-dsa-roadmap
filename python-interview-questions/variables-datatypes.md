"""

## 1. What is a variable in Python?

Answer: A variable is a name used to store data in memory. In Python, variables are dynamically typed, so you don’t need to declare the type explicitly.

x = 10
name = "Sam"

👉 Interview Tip:
“Python variables are references to objects, not containers.”

## 2. How is Python different from Java in variable declaration?

Answer: Python → No type declaration needed (dynamic typing)
Java → Requires explicit type declaration (static typing)
x = 10       # Python
x = "hello"  # same variable, different type

## 3. What is dynamic typing?

Answer: Dynamic typing means the type of a variable is determined at runtime.

x = 5       # int
x = "Sam"   # now string

## 4. What is type casting in Python?

Answer: Converting one data type to another.

x = "10"
y = int(x)   # 10

## 5. Difference between is and ==?

Answer:

Operator	Meaning
==	compares values
is	compares memory location
a = [1,2]
b = [1,2]

print(a == b)  # True
print(a is b)  # False

👉 Interview Gold Line:
“== checks equality, is checks identity.”

## 6. What is multiple assignment?
a, b, c = 1, 2, 3
a, b, c = 145

## 8. What are rules for naming variables?
Must start with letter or _
Cannot start with number
Case-sensitive
Cannot use keywords (if, for, etc.)

🔥 PYTHON DATA TYPES – INTERVIEW Q&A
❓ 9. What are Python data types?

Answer:
Built-in types:

🔹 Numeric
int
float
complex
🔹 Sequence
list
tuple
string
🔹 Set
set
🔹 Mapping
dict
🔹 Boolean
bool
🔹 None
NoneType

## 10. Difference between List and Tuple?
Feature	        List	Tuple
Mutable	        Yes	    No
Syntax	        []	    ()
Performance	    Slower	Faster
l = [1,2,3]
t = (1,2,3)

## 11. What is mutability?

Answer:
Mutable → can change
Immutable → cannot change

# Mutable
l = [1,2]
l.append(3)

# Immutable
s = "hi"
# s[0] = 'H' ❌

## 12. List all mutable and immutable types
Mutable:
list
dict
set
Immutable:
int, float, complex
str
tuple

## 13. What is None?

Answer: Represents absence of value.

x = None

👉 Not 0, not empty — it's a special type.

## 14. What is a dictionary?

Answer: Key-value pair collection.

d = {"name": "Sam", "age": 25}

## 15. Difference between set and list?
Feature	        List	    Set
Duplicate	    Allowed	    Not allowed
Order	        Ordered	    Unordered

## 16. What is type() function?
print(type(10))   # int

## 17. What is id() function?

Returns memory address.

x = 10
print(id(x))

## 18. What is bool type?
True / False

## 19. What is complex number?
x = 2 + 3j

## 20. Difference between shallow and deep understanding (IMPORTANT)

👉 Interview expects:

Not just types
But behavior (mutability, memory, reference)

## Q1: Why list is mutable but tuple is immutable?

Answer: Lists are designed for dynamic data (add/remove), tuples are optimized for fixed data → faster and safer.

## Q2: What happens here?
a = 10
b = a
b = 20
print(a)

👉 Output: 10 (because integers are immutable)

⚡ Why didn’t a change?
Step-by-step understanding:
✅ Step 1:
a = 10
Variable a points to an object 10 in memory

✅ Step 2:
b = a
b now points to the same object as a (value 10)

👉 So:

a ──► 10
b ──► 10

❗ Step 3:
b = 20
This does NOT change 10
Instead, Python creates a new object 20
b is now pointing to 20

👉 Now:

a ──► 10
b ──► 20

Key Insight (VERY IMPORTANT)

👉 Integers are immutable
That means:

You cannot change the value 10 itself

So instead of modifying 10, Python:

creates a new object 20
updates reference of b

⚠️ Your misunderstanding (fixed)

You said:

"value changed from 10 to 20"

❌ Not exactly

✔️ Correct:

“b stopped pointing to 10 and started pointing to a new object 20”

💡 Compare with Mutable Example
a = [1, 2]
b = a
b.append(3)

print(a)

👉 Output: [1, 2, 3]

👉 Why?

List is mutable
Both a and b point to same object
Object itself changed

Python variables store references to objects. In case of immutable types like integers, reassignment creates a new object instead of modifying the existing one.

🧠 Final Memory Trick
Type	                        Behavior
Immutable (int, str, tuple)	    New object created
Mutable (list, dict, set)	    Same object modified
"""