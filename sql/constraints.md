================================================
PRIMARY KEY
================================================

What is Primary Key?

A column that uniquely identifies
each row in a table.

Rules:

1. Must be unique
2. Cannot be NULL
3. One primary key per table

Example:

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

================================================
EXAMPLE
================================================

id    name

1     Alex
2     John

Valid

1     Alex
1     John

Invalid
Duplicate primary key.

================================================
FOREIGN KEY
================================================

What is Foreign Key?

A column that references the
primary key of another table.

================================================
EXAMPLE
================================================

Departments

dept_id
1
2

Employees

id    dept_id

101      1
102      2

dept_id in employees
references departments table.

================================================
SQL
================================================

CREATE TABLE employees (

    id INT PRIMARY KEY,

    dept_id INT,

    FOREIGN KEY (dept_id)
    REFERENCES departments(dept_id)

);

================================================
INTERVIEW QUESTION
================================================

Q. Why use Foreign Keys?

Answer: To maintain relationships
between tables.

================================================
SQL CONSTRAINTS
================================================

Constraints enforce rules.

================================================
NOT NULL
================================================

name VARCHAR(100) NOT NULL

================================================
UNIQUE
================================================

email VARCHAR(100) UNIQUE

================================================
PRIMARY KEY
================================================

id INT PRIMARY KEY

================================================
DEFAULT
================================================

status VARCHAR(20)
DEFAULT 'ACTIVE'

================================================
CHECK
================================================

salary INT CHECK (salary > 0)

================================================
INTERVIEW QUESTION
================================================

Q. Why use constraints?

Answer: To maintain data integrity.