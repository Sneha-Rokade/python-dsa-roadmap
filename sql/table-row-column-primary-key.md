================================================
TABLES, ROWS, COLUMNS & PRIMARY KEY
================================================

## What is a Table?

A table is used to store related data in a database.

Example:

Employee Table

+----+--------+----------+
| ID | Name   | Role     |
+----+--------+----------+
| 1  | Alex   | Engineer |
| 2  | John   | Manager  |
| 3  | Emma   | Tester   |
+----+--------+----------+

A table is similar to an Excel sheet.

------------------------------------------------

## What is a Row?

A row represents a single record.

Example:

| 1 | Alex | Engineer |

This complete entry is one row.

Another row:

| 2 | John | Manager |

Each employee is stored as a separate row.

------------------------------------------------

## What is a Column?

A column represents a specific attribute.

Example:

| ID | Name | Role |

Columns:

ID
Name
Role

Each column stores one type of information.

------------------------------------------------

## Table Terminology

Table Name: Employees

Columns:

ID
Name
Role

Rows:
1, Alex, Engineer
2, John, Manager
3, Emma, Tester

------------------------------------------------

## Real World Example

Student Table

+------------+---------+------+
| StudentID  | Name    | Age  |
+------------+---------+------+
| 101        | Alex    | 25   |
| 102        | John    | 22   |
+------------+---------+------+

Table: Students

Columns: StudentID Name Age

Rows: Each student record

------------------------------------------------

## What is a Primary Key?

A Primary Key uniquely identifies each row in a table.

Example:

Employee Table

+----+--------+----------+
| ID | Name   | Role     |
+----+--------+----------+
| 1  | Alex   | Engineer |
| 2  | John   | Manager  |
| 3  | Emma   | Tester   |
+----+--------+----------+

ID is the Primary Key.

Reason: Every employee has a unique ID.

------------------------------------------------

## Rules of Primary Key

1. Must be Unique

Correct:
1
2
3

Wrong:
1
1
2

------------------------------------------------

2. Cannot be NULL

Correct:
1
2
3

Wrong:
1
NULL
3

------------------------------------------------

3. One Primary Key Per Table

Example: EmployeeID Acts as the Primary Key.

------------------------------------------------

## Why Do We Need a Primary Key?

Without Primary Key:

| Name |
|------|
| Alex |
| Alex |

Which Alex?

Impossible to identify correctly.

------------------------------------------------

With Primary Key:

| ID | Name |
|----|------|
| 1  | Alex |
| 2  | Alex |

Now every record is unique.

------------------------------------------------

## SQL Example

Create Employee Table

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(50)
);

Explanation:
id             -> Column
INT            -> Data Type
PRIMARY KEY    -> Unique Identifier

------------------------------------------------

## Real World Examples

Employees Table

Primary Key:
EmployeeID

------------------------------------------------

Students Table

Primary Key:
StudentID

------------------------------------------------

Orders Table

Primary Key:
OrderID

------------------------------------------------

Customers Table

Primary Key:
CustomerID

------------------------------------------------

## Interview Questions

Q1. What is a Table?

Answer: A table is a collection of related data
organized into rows and columns.

------------------------------------------------

Q2. What is a Row?

Answer: A row represents a single record in a table.

------------------------------------------------

Q3. What is a Column?

Answer: A column represents a specific attribute
or field in a table.

------------------------------------------------

Q4. What is a Primary Key?

Answer: A Primary Key uniquely identifies each row
in a table.

------------------------------------------------

Q5. Can a Primary Key contain NULL values?

Answer:No.
A Primary Key cannot contain NULL values.

------------------------------------------------

Q6. Can duplicate values exist in a Primary Key?

Answer: No.
Primary Key values must be unique.

------------------------------------------------

Q7. Why is a Primary Key important?

Answer: It helps uniquely identify records and
maintains data integrity.

------------------------------------------------

## Summary

Table: Collection of related data.

Row: Single record.

Column: Attribute of a table.

Primary Key: Unique identifier for each row.

Rules:

✓ Unique
✓ Not NULL
✓ One per table