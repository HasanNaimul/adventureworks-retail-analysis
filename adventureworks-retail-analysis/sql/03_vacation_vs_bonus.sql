-- Question:
-- Is there a relationship between vacation hours and bonus?

SELECT
    e.BusinessEntityID,
    e.VacationHours,
    sp.Bonus
FROM HumanResources.Employee AS e
INNER JOIN Sales.SalesPerson AS sp
    ON e.BusinessEntityID = sp.BusinessEntityID;
