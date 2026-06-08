================================================
VIEWS
================================================

Virtual table based on query.

================================================
EXAMPLE
================================================

CREATE VIEW active_employees AS

SELECT *

FROM employees

WHERE status = 'ACTIVE';

================================================
WHY USE VIEWS?
================================================

1. Security
2. Reusable Queries
3. Simpler Reporting