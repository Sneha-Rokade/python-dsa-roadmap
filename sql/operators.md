================================================
SQL OPERATORS
================================================

AND

Both conditions must be true.

Example:

SELECT *
FROM employees
WHERE age > 25
AND city = 'Pune';

------------------------------------------------

OR

At least one condition true.

Example:

SELECT *
FROM employees
WHERE city = 'Pune'
OR city = 'Mumbai';

------------------------------------------------

NOT

Reverses condition.

Example:

SELECT *
FROM employees
WHERE NOT city = 'Pune';

================================================
LIKE OPERATOR
================================================

Used for pattern matching.

Starts with A

SELECT *
FROM employees
WHERE name LIKE 'A%';

Ends with n

SELECT *
FROM employees
WHERE name LIKE '%n';

Contains oh

SELECT *
FROM employees
WHERE name LIKE '%oh%';

================================================
IN OPERATOR
================================================

SELECT *
FROM employees
WHERE city IN ('Pune','Mumbai');

================================================
BETWEEN OPERATOR
================================================

SELECT *
FROM employees
WHERE age BETWEEN 20 AND 30;