================================================
CREATE DATABASE & CREATE TABLE
================================================

## What is a Database?

A database is a collection of related tables.

Example: Company Database

Tables:

Employees
Departments
Projects
Salaries

All these tables together form a database.

------------------------------------------------

## CREATE DATABASE

Used to create a new database.

Syntax: CREATE DATABASE database_name;

Example: CREATE DATABASE company_db;

Explanation: CREATE DATABASE -> SQL Command
             company_db -> Database Name

------------------------------------------------

## View Databases

Syntax: SHOW DATABASES;

Output:

company_db
school_db
bank_db

------------------------------------------------

## Select a Database

Before creating tables, we must choose
which database to use.

Syntax: USE database_name;

Example: USE company_db;

------------------------------------------------

## What is a Table?

A table stores data in rows and columns.

Example: Employees Table

+----+--------+----------+
| ID | Name   | Role     |
+----+--------+----------+
| 1  | Alex   | Engineer |
| 2  | John   | Manager  |
+----+--------+----------+

------------------------------------------------

## CREATE TABLE

Used to create a table.

Syntax: CREATE TABLE table_name (
    column_name datatype,
    column_name datatype
);

------------------------------------------------

Example: CREATE TABLE employees (
    id INT,
    name VARCHAR(50),
    role VARCHAR(50)
);

Explanation: employees -> Table Name
id -> Column
INT -> Integer Data Type
name -> Column
VARCHAR(50) -> String up to 50 characters
role -> Column
VARCHAR(50) -> String up to 50 characters

------------------------------------------------

## Table Structure

CREATE TABLE employees (

    id INT,
    name VARCHAR(50),
    age INT,
    salary INT
);

Table:

+----+--------+-----+--------+
| id | name   | age | salary |
+----+--------+-----+--------+

------------------------------------------------

## Primary Key Example

CREATE TABLE employees (

    id INT PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(50)

);

Explanation:

PRIMARY KEY

✓ Unique
✓ Cannot be NULL

------------------------------------------------

## Common SQL Data Types

1. INT

Stores whole numbers.

Example:

25
100
500

------------------------------------------------

2. VARCHAR(n)

Stores text.

Example:

Alex
Engineer
Google

VARCHAR(50)

Maximum 50 characters.

------------------------------------------------

3. FLOAT

Stores decimal numbers.

Example:

99.99
75.50

------------------------------------------------

4. DATE

Stores dates.

Example:

2026-06-02

------------------------------------------------

Example Table

CREATE TABLE students (

    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    percentage FLOAT
);

------------------------------------------------

Real World Example

Employee Management System

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    role VARCHAR(50),
    salary INT
);

------------------------------------------------

Banking Application

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    account_balance FLOAT
);

------------------------------------------------

Interview Questions

Q1. What is a Database?

Answer: A database is a collection of related tables
used to store and manage data.

------------------------------------------------

Q2. Which SQL command creates a database?

Answer: CREATE DATABASE

Example: CREATE DATABASE company_db;

------------------------------------------------

Q3. Which SQL command creates a table?

Answer: CREATE TABLE

Example: CREATE TABLE employees (
    id INT,
    name VARCHAR(50)
);

------------------------------------------------

Q4. What is VARCHAR?

Answer: VARCHAR stores variable-length text.

Example: VARCHAR(50)
Can store up to 50 characters.

------------------------------------------------

Q5. Difference Between INT and VARCHAR?

INT
Stores numbers.

Example: 25

VARCHAR
Stores text.

Example: Alex

------------------------------------------------

Q7. Can two rows have the same PRIMARY KEY?

Answer: No.
PRIMARY KEY values must be unique.

------------------------------------------------

Summary

CREATE DATABASE
Creates a new database.
CREATE TABLE
Creates a new table.
Important Data Types:

INT
VARCHAR
FLOAT
DATE
