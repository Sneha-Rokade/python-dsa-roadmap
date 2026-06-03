================================================
SUBQUERIES
================================================

Query inside another query.

================================================
EXAMPLE
================================================

Find employee with
highest salary.

SELECT *

FROM employees

WHERE salary = (

    SELECT MAX(salary)

    FROM employees

);

================================================
INTERVIEW QUESTION
================================================

Q. What is Subquery?

Answer: A query inside another query.