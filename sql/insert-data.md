================================================
INSERT INTO STATEMENT
================================================

## What is INSERT INTO?

INSERT INTO is used to add records (rows)
into a table.

Without INSERT INTO:

Table exists but contains no data.

With INSERT INTO:

Data is stored inside the table.

------------------------------------------------

Employee Table

+----+--------+----------+
| id | name   | role     |
+----+--------+----------+

Currently Empty

------------------------------------------------

Syntax

INSERT INTO table_name
(column1, column2, column3)

VALUES
(value1, value2, value3);

------------------------------------------------

Example

INSERT INTO employees
(id, name, role)

VALUES
(1, 'Alex', 'Engineer');

------------------------------------------------

After Insert

+----+--------+----------+
| id | name   | role     |
+----+--------+----------+
| 1  | Alex   | Engineer |
+----+--------+----------+

------------------------------------------------

Insert Multiple Records

INSERT INTO employees
(id, name, role)

VALUES
(1, 'Alex', 'Engineer'),
(2, 'John', 'Manager'),
(3, 'Emma', 'Tester');

------------------------------------------------

Table Data

+----+--------+----------+
| id | name   | role     |
+----+--------+----------+
| 1  | Alex   | Engineer |
| 2  | John   | Manager  |
| 3  | Emma   | Tester   |
+----+--------+----------+

------------------------------------------------

Student Table Example

CREATE TABLE students (

    student_id INT PRIMARY KEY,

    name VARCHAR(50),

    age INT

);

------------------------------------------------

Insert Records

INSERT INTO students
(student_id, name, age)

VALUES

(101, 'Alex', 25),

(102, 'John', 22),

(103, 'Emma', 24);

------------------------------------------------

Result

+------------+--------+-----+
| student_id | name   | age |
+------------+--------+-----+
| 101        | Alex   | 25  |
| 102        | John   | 22  |
| 103        | Emma   | 24  |
+------------+--------+-----+

------------------------------------------------

Rules for INSERT INTO

1. Number of columns and values
   must match.

Correct:

INSERT INTO employees
(id, name)

VALUES
(1, 'Alex');

------------------------------------------------

Wrong:

INSERT INTO employees
(id, name)

VALUES
(1);

Reason:

Two columns but only one value.

------------------------------------------------

2. Data Types Must Match

Correct:

age INT

INSERT INTO students
(age)

VALUES
(25);

------------------------------------------------

Wrong:

INSERT INTO students
(age)

VALUES
('Alex');

Reason:

age expects INT.

------------------------------------------------

3. Primary Key Must Be Unique

Correct:

1
2
3

------------------------------------------------

Wrong:

1
1
2

Duplicate Primary Key Error

------------------------------------------------

Real World Example

Employee Management System

INSERT INTO employees

(employee_id,
 employee_name,
 role,
 salary)

VALUES

(1, 'Alex', 'Software Engineer', 50000),

(2, 'John', 'Manager', 80000);

------------------------------------------------

Banking System

INSERT INTO customers

(customer_id,
 customer_name,
 balance)

VALUES

(101, 'Alex', 50000),

(102, 'John', 75000);

------------------------------------------------

Interview Questions

Q1. What is INSERT INTO?

Answer:

INSERT INTO is used to add records
into a database table.

------------------------------------------------

Q2. What is the syntax of INSERT INTO?

Answer:

INSERT INTO table_name
(column1, column2)

VALUES
(value1, value2);

------------------------------------------------

Q3. Can we insert multiple rows at once?

Answer:

Yes.

Example:

INSERT INTO employees
(id, name)

VALUES

(1, 'Alex'),

(2, 'John'),

(3, 'Emma');

------------------------------------------------

Q4. What happens if PRIMARY KEY
values are duplicated?

Answer:

Database throws an error because
PRIMARY KEY values must be unique.

------------------------------------------------

Q5. What happens if column count
and value count do not match?

Answer:

Database throws an error.

------------------------------------------------

Summary

INSERT INTO

Purpose:
Add records into a table.

Syntax:

INSERT INTO table_name
(columns)

VALUES
(values);

Important Rules:

✓ Columns and values count must match

✓ Data types must match

✓ PRIMARY KEY must be unique