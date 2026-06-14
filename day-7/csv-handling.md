# CSV HANDLING IN PYTHON

## What is CSV?

CSV stands for: Comma Separated Values
It is one of the most common file formats used for storing tabular data.

Example:

id,name,age
1,Alex,25
2,John,30
3,Emma,28

Looks similar to Excel data.

# Why CSV is Important?

CSV files are used in:

* Data Migration
* Reports
* Analytics
* Excel Export/Import
* Django Admin Exports
* Database Backups

Almost every company uses CSV files.

# CSV MODULE

Python provides built-in support through: import csv
No installation required.

# READING A CSV FILE

Suppose we have: employees.csv

id,name,salary
1,Alex,50000
2,John,60000
3,Emma,70000

## Example
import csv

with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.reader(file)
    for row in reader:
        print(row)
Output:
['id', 'name', 'salary']
['1', 'Alex', '50000']
['2', 'John', '60000']
['3', 'Emma', '70000']

# Understanding csv.reader()
csv.reader(file)
Returns rows one by one.

Each row becomes: list

# SKIPPING HEADER

Example: import csv

with open(
    "employees.csv",
    "r"
) as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

Output:
['1', 'Alex', '50000']
['2', 'John', '60000']
['3', 'Emma', '70000']

Header removed.

# ACCESSING COLUMNS

Example:
import csv
with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[1])

Output:
Alex
John
Emma

# WRITING CSV FILE

Example:
import csv
with open(
    "students.csv",
    "w",
    newline=""
) as file:
    writer = csv.writer(file)
    writer.writerow(
        ["id", "name", "marks"]
    )
    writer.writerow(
        [1, "Alex", 90]
    )
    writer.writerow(
        [2, "John", 85]
    )

Generated File:
id,name,marks
1,Alex,90
2,John,85

# WRITING MULTIPLE ROWS

Instead of:
writer.writerow(...)
writer.writerow(...)

Use: writer.writerows(data)

Example: import csv

data = [
    [1, "Alex", 90],
    [2, "John", 85],
    [3, "Emma", 95]
]

with open(
    "students.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)
    writer.writerow(
        ["id", "name", "marks"]
    )
    writer.writerows(data)

# APPENDING CSV DATA

Existing file:
id,name
1,Alex

Append:

import csv

with open(
    "students.csv",
    "a",
    newline=""
) as file:

    writer = csv.writer(file)
    writer.writerow(
        [2, "John"]
    )

Result:
id,name
1,Alex
2,John

# DICTIONARY READER

CSV can be read as dictionaries.

Example:
import csv

with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.DictReader(file)
    for row in reader:
        print(row)

Output:
{
 'id': '1',
 'name': 'Alex',
 'salary': '50000'
}

# ACCESSING COLUMN BY NAME

import csv

with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])

Output:
Alex
John
Emma

Much cleaner than:
row[1]

# DICTIONARY WRITER

Example:
import csv

with open(
    "employees.csv",
    "w",
    newline=""
) as file:

    fields = [
        "id",
        "name",
        "salary"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fields
    )

    writer.writeheader()

    writer.writerow({
        "id": 1,
        "name": "Alex",
        "salary": 50000
    })

# REAL WORLD EXAMPLE

Employee Report

import csv

total_salary = 0

with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.DictReader(file)
    for row in reader:
        total_salary += int(
            row["salary"]
        )

print(total_salary)

Output: 180000

# FILTERING CSV DATA

Example:
import csv

with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.DictReader(file)
    for row in reader:
        if int(row["salary"]) > 55000:
            print(row["name"])

Output:
John
Emma

# CSV TO LIST

Example:
import csv
data = []

with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)
print(data)

Useful in APIs.

# CSV TO DICTIONARY

Example:
import csv

employees = {}

with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.DictReader(file)
    for row in reader:
        employees[
            row["id"]
        ] = row["name"]
print(employees)
Output:
{
 '1': 'Alex',
 '2': 'John'
}

# DJANGO USE CASE

Bulk User Import

CSV:
name,email
alex@gmail.com
john@gmail.com

Read CSV:
for row in reader:
    User.objects.create(
        name=row["name"],
        email=row["email"]
    )

Very common interview example.

# EXPORTING DATA TO CSV

Example:
import csv
users = [
    ["Alex", 25],
    ["John", 30]
]

with open(
    "users.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)
    writer.writerow(
        ["Name", "Age"]
    )

    writer.writerows(users)

# COMMON MISTAKES

## Forgetting newline=""

Bad:

open(
    "file.csv",
    "w"
)

Good:
open(
    "file.csv",
    "w",
    newline=""
)

## Forgetting int Conversion

Bad: salary += row["salary"]

Good:
salary += int(
    row["salary"]
)

CSV values are strings.

# BEST PRACTICES

### Use DictReader

Good: row["salary"]
Bad: row[2]

### Use with Statement

Automatically closes file.

### Validate Data

Before database insertion: if email:
Always validate.

# INTERVIEW QUESTIONS

### Q1. Which Module Handles CSV?

Answer: csv

### Q3. Difference Between reader and DictReader?

Answer: reader: Returns list.
DictReader: Returns dictionary.

### Q4. Which Function Writes One Row?

Answer: writer.writerow()

### Q5. Which Function Writes Multiple Rows?

Answer: writer.writerows()

### Q6. Why Use DictReader?

Answer: Access columns by name.

### Q7. Why Use newline=""?

Answer: To avoid blank lines.

### Q8. Are CSV Values Strings?

Answer: Yes.
Need conversion:
int()
float()

### Q9. Where Are CSV Files Used?

Answer:

* Reports
* Analytics
* Excel Exports
* Data Migration

### Q10. Django Use Case?

Answer: Bulk import/export operations.

# PRACTICE QUESTIONS

1. Read CSV file.
2. Skip header row.
3. Print names column.
4. Calculate total salary.
5. Filter employees above 50000 salary.
6. Write CSV file.
7. Append CSV row.
8. Use DictReader.
9. Use DictWriter.
10. Build employee report generator.

# SUMMARY

Important Concepts:

* csv module
* csv.reader()
* csv.writer()
* DictReader
* DictWriter
* writerow()
* writerows()

Used In:

* Django Projects
* Data Migration
* Reports
* Analytics
* Enterprise Applications

