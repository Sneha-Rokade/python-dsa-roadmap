================================================
JOINS IN SQL
================================================

Why Joins?

Data is usually stored
in multiple tables.

Joins combine data.

Example:

employees

id   name   dept_id

departments

dept_id   dept_name

Join combines both tables.

================================================
INNER JOIN
================================================

Returns matching records
from both tables.

Example:

SELECT e.name,
       d.dept_name

FROM employees e

INNER JOIN departments d

ON e.dept_id = d.dept_id;

Only matching rows returned.

================================================
LEFT JOIN
================================================

Returns:

All rows from left table
Matching rows from right table

Example:

SELECT *
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id;

================================================
RIGHT JOIN
================================================

Returns:

All rows from right table
Matching rows from left table

================================================
FULL OUTER JOIN
================================================

Returns:

All rows from both tables.
Matching where possible.
NULL where no match.