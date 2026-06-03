================================================
STRING FUNCTIONS
================================================

UPPER()

SELECT UPPER(name)
FROM employees;

------------------------------------------------

LOWER()

SELECT LOWER(name)
FROM employees;

------------------------------------------------

LENGTH()

SELECT LENGTH(name)
FROM employees;

------------------------------------------------

CONCAT()

SELECT CONCAT(first_name, ' ', last_name)
FROM employees;

================================================
INTERVIEW QUESTION
================================================

Q. Why use String Functions?

Answer: To manipulate text data.

================================================
DATE FUNCTIONS
================================================

Current Date
SELECT CURRENT_DATE;

------------------------------------------------

Current Timestamp
SELECT CURRENT_TIMESTAMP;

------------------------------------------------

Extract Year
SELECT EXTRACT(YEAR FROM CURRENT_DATE);

------------------------------------------------

Extract Month

SELECT EXTRACT(MONTH FROM CURRENT_DATE);

================================================
REAL WORLD USE
================================================

Employee Joining Date
Order Date
Payment Date
Log Analysis

================================================
INTERVIEW QUESTION
================================================

Q. Why are Date Functions important?

Answer: Most applications store
date and time information.