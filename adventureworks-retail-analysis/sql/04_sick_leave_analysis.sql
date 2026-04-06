-- Question:
-- Does sick leave vary by job title or department?

-- A. Average sick leave by job title
SELECT
    JobTitle,
    COUNT(*) AS employee_count,
    AVG(SickLeaveHours) AS avg_sick_leave
FROM HumanResources.Employee
GROUP BY JobTitle
ORDER BY avg_sick_leave DESC;

-- B. Min / max / average sick leave by job title
SELECT
    JobTitle,
    MIN(SickLeaveHours) AS min_sick_leave,
    MAX(SickLeaveHours) AS max_sick_leave,
    AVG(SickLeaveHours) AS avg_sick_leave
FROM HumanResources.Employee
GROUP BY JobTitle
ORDER BY avg_sick_leave DESC;

-- C. Company-wide average sick leave
SELECT
    AVG(SickLeaveHours) AS company_avg_sick_leave
FROM HumanResources.Employee
WHERE CurrentFlag = 1;

-- D. Average sick leave by department
SELECT
    d.Department,
    AVG(e.SickLeaveHours) AS avg_sick_leave
FROM HumanResources.Employee AS e
INNER JOIN HumanResources.vEmployeeDepartment AS d
    ON e.BusinessEntityID = d.BusinessEntityID
GROUP BY d.Department
ORDER BY avg_sick_leave DESC;
