================================================
WHERE CLAUSE IN SQL
================================================

What is WHERE?

WHERE is used to filter records.

Without WHERE:

SELECT * FROM employees;

Returns all rows.

With WHERE:

SELECT * FROM employees
WHERE age > 25;

Returns only matching rows.

================================================
COMPARISON OPERATORS
================================================

=   Equal

!=  Not Equal

>   Greater Than

<   Less Than

>=  Greater Than Equal To

<=  Less Than Equal To

================================================
EXAMPLES
================================================

Find employee with id 1

SELECT *
FROM employees
WHERE id = 1;

------------------------------------------------

Find employees older than 25

SELECT *
FROM employees
WHERE age > 25;

------------------------------------------------

Find employees younger than 30

SELECT *
FROM employees
WHERE age < 30;

------------------------------------------------

Find employees not from Pune

SELECT *
FROM employees
WHERE city != 'Pune';

================================================
INTERVIEW QUESTIONS
================================================

Q. What is WHERE clause?

Answer: Used to filter records based on conditions.