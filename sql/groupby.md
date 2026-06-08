================================================
GROUP BY IN SQL
================================================

What is GROUP BY?

Groups rows with same values.

================================================
EXAMPLE
================================================

Find employee count by city

SELECT city,
COUNT(*)
FROM employees
GROUP BY city;

Output:

Pune      5
Mumbai    3
Delhi     2

================================================
WHY USE GROUP BY?
================================================

Used with:
COUNT()
SUM()
AVG()
MAX()
MIN()

================================================
INTERVIEW QUESTION
================================================

Q. What is GROUP BY?

Answer: Groups rows and applies
aggregate functions.

================================================
HAVING CLAUSE
================================================

HAVING filters grouped data.
WHERE filters rows.
HAVING filters groups.

================================================
EXAMPLE
================================================

SELECT city,
COUNT(*)
FROM employees
GROUP BY city
HAVING COUNT(*) > 2;

================================================
WHERE VS HAVING
================================================

WHERE
Before grouping.

HAVING
After grouping.

================================================
INTERVIEW QUESTION
================================================

Q. Difference Between WHERE and HAVING?

WHERE -> filters rows
HAVING -> filters groups