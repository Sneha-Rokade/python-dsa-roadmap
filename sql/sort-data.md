================================================
ORDER BY IN SQL
================================================

Used to sort records.
Ascending Order:

SELECT *
FROM employees
ORDER BY age ASC;

Descending Order:

SELECT *
FROM employees
ORDER BY age DESC;

================================================
MULTIPLE COLUMN SORTING
================================================

SELECT *
FROM employees
ORDER BY city ASC, age DESC;

================================================
LIMIT
================================================

Used to restrict records.

Top 5 employees:

SELECT *
FROM employees
LIMIT 5;

================================================
INTERVIEW QUESTION
================================================

Q. Difference between ASC and DESC?

ASC: Ascending order

DESC: Descending order