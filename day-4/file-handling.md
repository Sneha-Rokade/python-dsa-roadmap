# FILE HANDLING IN PYTHON

## What is File Handling?

File handling is the process of:

* Creating files
* Reading files
* Writing files
* Updating files
* Deleting files

Files allow data to persist even after the program stops.

## Why is File Handling Important?

Real-world applications use files for:

* Logs
* Reports
* Configuration Files
* Resume Uploads
* CSV Data
* User Documents

Examples:

* Django media uploads
* Server logs
* Configuration settings
* Data exports

## Opening a File

Syntax: open(file_name, mode)

Example: file = open("data.txt", "r")

## File Modes

| Mode | Meaning      |
| ---- | ------------ |
| r    | Read         |
| w    | Write        |
| a    | Append       |
| x    | Create       |
| rb   | Read Binary  |
| wb   | Write Binary |

## Read File

Suppose data.txt contains:

Hello Python
Welcome to File Handling

Code: file = open("data.txt", "r")

content = file.read()

print(content)

file.close()

Output:

Hello Python
Welcome to File Handling

## Read One Line

file = open("data.txt", "r")

print(file.readline())

file.close()

Output: Hello Python

## Read All Lines

file = open("data.txt", "r")

lines = file.readlines()

print(lines)

file.close()

Output: ['Hello Python\n', 'Welcome to File Handling']

## Write File

Creates new file or overwrites existing file.

file = open("notes.txt", "w")

file.write("Python File Handling")

file.close()

Result: notes.txt

Python File Handling

## Append File

Adds content without removing existing data.

file = open("notes.txt", "a")

file.write("\nLearning Python")

file.close()

Output:

Python File Handling
Learning Python

## Create New File

file = open("newfile.txt", "x")

file.close()

Creates file only if it doesn't already exist.

## Using with Statement

Best Practice.

Instead of:

file = open("data.txt", "r")

print(file.read())

file.close()

Use:

with open("data.txt", "r") as file:

    print(file.read())

Advantages:

* Cleaner code
* Automatically closes file
* Prevents memory leaks

Professional developers always prefer this approach.


## File Exists Example

import os

if os.path.exists("data.txt"):

    print("File Exists")

else:

    print("File Not Found")


## Delete File

import os

os.remove("data.txt")

Deletes file permanently.

## Real World Example

Save User Feedback.

feedback = "Application is awesome"

with open("feedback.txt", "a") as file:

    file.write(feedback + "\n")

Output: feedback.txt

Application is awesome

## Real World Example

Store Application Logs

with open("logs.txt", "a") as file:

    file.write("User Logged In\n")

Very common in backend systems.

## Real World Example

Resume Upload Simulation

resume_content = "Alex Resume Data"

with open("resume.txt", "w") as file:

    file.write(resume_content)

Similar concept used in Django file uploads.

## Exception Handling with Files

try:

    with open("data.txt", "r") as file:

        print(file.read())

except FileNotFoundError:

    print("File Not Found")

Output: File Not Found

## Reading Large Files

Instead of: file.read()

Use:

with open("data.txt", "r") as file:

    for line in file:

        print(line)

Efficient for large files.

## Working with CSV Files

Example:

import csv

with open("employees.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        print(row)

Used in:

* Data Engineering
* Reporting Systems
* Analytics

## Common File Methods

### read()

file.read()

Reads entire file.

### readline()

file.readline()

Reads one line.

### readlines()

file.readlines()

Reads all lines.

### write()

file.write("Hello")

Writes content.

### close()

file.close()

Closes file.

## Interview Questions

### Q1. What is File Handling?

Answer: The process of reading, writing, creating, updating, and deleting files.

### Q2. Why Use Files?

Answer: To store data permanently.

### Q3. Difference Between r and w?

r: Read mode.

w: Write mode and overwrite file.

### Q4. Difference Between w and a?

w: Overwrite existing content.

a: Append new content.

### Q5. Why Use with Statement?

Answer: Automatically closes file and prevents resource leaks.

### Q6. What is FileNotFoundError?

Answer: Occurs when attempting to open a file that doesn't exist.

### Q7. What is the Safest Way to Open Files?

Answer: with open(...)

### Q8. How Do You Delete a File?

Answer: os.remove(filename)

### Q9. What is CSV?

Answer: Comma Separated Values.

Common format for storing tabular data.

### Q10. Where is File Handling Used?

Answer:

* Django Uploads
* Logs
* Reports
* CSV Processing
* Data Engineering
* Cloud Applications

## Practice Questions

1. Create a file.
2. Write data into file.
3. Read file content.
4. Append new content.
5. Read line by line.
6. Use with statement.
7. Check file existence.
8. Delete a file.
9. Handle FileNotFoundError.
10. Create simple log file.

## Summary

Important Concepts:

* open()
* read()
* write()
* append()
* close()
* with
* File Modes

Modes:

r
w
a
x

Common Uses:

* Resume Uploads
* Logs
* Reports
* CSV Files
* Configuration Files
* Backend Applications
