-- Question:
-- How do store size and number of employees relate to revenue?

SELECT
    BusinessEntityID,
    Name,
    AnnualRevenue,
    SquareFeet,
    NumberEmployees
FROM Sales.vStoreWithDemographics
ORDER BY AnnualRevenue DESC;
