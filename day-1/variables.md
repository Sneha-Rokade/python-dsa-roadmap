
# PYTHON VARIABLES - DAY 1 NOTES

## What is a Variable?
-------------------
In Python, a variable is a name given to a memory location where data is stored. It allows us to store, manage, and use data in a program. Python is dynamically typed, so we do not need to declare the type of a variable; it is decided automatically based on the value assigned.

Example:
name = "Sneha"

Here:
Variable Name = name
Value = "Sneha"

Python automatically determines the data type.
This is called Dynamic Typing.

=========================================
VARIABLE CREATION
=========================================

name = "Sneha"
age = 31
salary = 4000000

print(name)
print(age)
print(salary)

Output:
Sneha
31
4000000

As we can see, we did not declare their types explicitly; Python automatically assigns their data types at runtime.

# --------------------------------------

## VARIABLE REASSIGNMENT

Variables can be changed after creation.

city = "Pune"
print(city)

city = "Mumbai"
print(city)

Output:
Pune
Mumbai

# --------------------------------------

## Rules and Naming Conventions for Python Variables
Python follows certain rules for naming variables:

We can define a variable name using alphabets (A-Z or a-z), numbers (0-9), and underscore (_). (Example: var_one, var1)
The names of the variables can start with an alphabet or underscore, but not with a number.
Valid: _var_1
Invalid: 1var
No Spacing is allowed.
Valid: var_one
Invalid: var one
Variable names are case-sensitive. (car, Car, and CAR are three different variables)
We cannot use reserved Python keywords as variable names (Example: class, def, return, if, break etc.)

# --------------------------------------

## DYNAMIC TYPING

Python variables are dynamically typed, meaning that we can store different types of value in the same variable.

var_one = 82
print(var_one)

var_one = "Alex"
print(var_one)

Output:
82
Alex

# --------------------------------------

## Multiple Assignments

The multiple assignments allow us to assign values to more than one variable in a single line. We can assign the same value to multiple variables or assign different values at the same time. This makes the code shorter, cleaner, and easier to read.

# Assigning Same Value to Multiple Variables

var_one = var_two = var_three = 85

print("variable 1: ", var_one)
print("variable 2: ", var_two)
print("variable 3: ", var_three)

output:
variable 1:  85
variable 2:  85
variable 3:  85

# Assigning Different Values to Multiple Variables

Python also provides us with accessibility to assign the different values to multiple variables simultaneously.

var1, var2, var3 = 20, "Alex", 85.9

print("variable 1: ", var1)
print("variable 2: ", var2)
print("variable 3: ", var3)

output:
variable 1:  20
variable 2:  Alex
variable 3:  85.9

# --------------------------------------

## TypeCasting a variable
Type Casting is the process of converting the value of one data type into another. In some cases, Python automatically converts types. However, there are few built-in functions like int(), float(), str() and more, in order to ease type casting.

# type casting  
var_1 = 9     # int  
  
# implicit type casting  
var_2 = var_1 / 4  
print(var_2)  # int -> float  
  
# explicit type casting  
var_2 = int(var_2)  
print(var_2)  # float -> int  

output:
2.25
2

Explanation:

In the above example, we have initialized an 'int' variable and perform a simple mathematical division resulting in a floating-point value and storing it another variable. In this case, Python has automatically assigned it as a 'float' variable.
In next case, we have used the int() method to convert the 'float' variable into 'int' variable explicitly.

## Getting the Type of Variable
We are allowed to determine the data type of a variable. Python provides a built-in function called type() that returns the type of the object passed to it.

# initializing variables of different data types  
var_w = 18            # int  
var_v = 82.6          # float  
var_x = 'Tpoint Tech' # string  
var_y = True          # boolean  
var_z = [4, 1, 8, -5] # list  
  
# printing their types using type() function  
print(var_w, '->', type(var_w))  
print(var_v, '->', type(var_v))  
print(var_x, '->', type(var_x))  
print(var_y, '->', type(var_y))  
print(var_z, '->', type(var_z))  

output:

18 -> <class 'int'>
82.6 -> <class 'float'>
Tpoint Tech -> <class 'str'>
True -> <class 'bool'>
[4, 1, 8, -5] -> <class 'list'>

---

## Scope of a Variable
The scope of a variable is the region in the code where it is accessible. Variables declared outside any function have global scope; whereas variables declared inside a function have local scope, accessible only within that function.

# global variable  
var_x = 15  
  
# defining a function to add numbers  
def add_num():  
  # local variable     
  var_y = 12  
    
  print(f'{var_x} + {var_y} = {var_x + var_y}')  
  
# calling the add_num() fuction  
add_num()  
  
# printing details  
print("var_x =", var_x)  
# print("var_y =", var_y)   # accessing local variable outside the scope will raise error  

"""
COMMON DATA TYPES
"""

name = "Sneha"       # string
age = 31             # integer
cgpa = 8.5           # float
is_placed = True     # boolean

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_placed))

# --------------------------------------

"""
MULTIPLE VARIABLES
"""

company = "Google"
location = "Pune"
package = 4000000

print(company, location, package)

# --------------------------------------

"""
F-STRING FORMATTING

Modern and preferred way.
"""

name = "Sneha"
age = 31

print(f"My name is {name}")
print(f"My age is {age}")

"""
Output:
My name is Sneha
My age is 31
"""

# --------------------------------------

"""
VARIABLE NAMING RULES

Allowed:
"""

student_name = "Sneha"
studentAge = 31
_age = 31

# --------------------------------------

"""
Not Allowed:

2name = "Sneha"
student-name = "Sneha"
class = "Python"

Reason:
Variable cannot start with number.
Hyphen not allowed.
Keywords not allowed.
"""

# --------------------------------------

"""
MEMORY BASICS

When:

name = "Sneha"

Python creates an object in memory
and variable 'name' points to it.

name ----> "Sneha"

When:

name = "Rohit"

name now points to new value.

name ----> "Rohit"
"""

# --------------------------------------

"""
INTERVIEW QUESTIONS

Q1. What is a variable?

Answer:
A variable is a named memory location
used to store data.

--------------------------------------

Q2. Is Python statically typed?

Answer:
No.
Python is dynamically typed.

--------------------------------------

Q3. What is dynamic typing?

Answer:
The data type is automatically determined
during runtime.

--------------------------------------

Q4. Can variable values be changed?

Answer:
Yes.
Variables can be reassigned.

--------------------------------------

Q5. What is the difference between:

age = 25

and

age = "25"

Answer:

25      -> Integer
"25"    -> String

=========================================
PRACTICE QUESTIONS
=========================================

1. Create variables:
   name, city, salary

2. Print using f-string

3. Change city value

4. Print type of:
   int
   str
   float
   bool

5. Create:
   name = "Alex"
   role = "Software Enginner"

   Print:
   "I want 4000000 package at Google"
