================================================
DISTINCT IN SQL
================================================

What is DISTINCT?

DISTINCT removes duplicate values
from query results.

Example:

SELECT city
FROM employees;

Output:
Pune
Pune
Mumbai
Delhi

------------------------------------------------

Using DISTINCT

SELECT DISTINCT city
FROM employees;

Output:
Pune
Mumbai
Delhi

================================================
INTERVIEW QUESTION
================================================

Q. What is DISTINCT?

Answer: Used to remove duplicate values
from result set.

================================================
NULL VALUES IN SQL
================================================

What is NULL?

NULL means missing or unknown value.

Example:

name      salary

Alex      50000
John      NULL

================================================
CHECK NULL
================================================

Wrong:

WHERE salary = NULL

Correct:

WHERE salary IS NULL

Example:

SELECT *
FROM employees
WHERE salary IS NULL;

================================================
NOT NULL
================================================

SELECT *
FROM employees
WHERE salary IS NOT NULL;

================================================
INTERVIEW QUESTION
================================================

Q. Difference Between NULL and 0?

NULL = Unknown
0 = Actual Value

================================================
ALIASES IN SQL
================================================

Alias means temporary name.

================================================
COLUMN ALIAS
================================================

SELECT name AS Employee_Name
FROM employees;

================================================
TABLE ALIAS
================================================

SELECT e.name
FROM employees e;

================================================
WHY USE ALIAS?
================================================

1. Better readability
2. Shorter queries
3. Useful in joins

================================================
INTERVIEW QUESTION
================================================

Q. What is Alias?

Answer: Temporary name for column or table.