-- Question:
-- Which countries generate the highest revenue?

SELECT
    SUM(t.SalesYTD) AS total_sales,
    c.Name AS country_name,
    t.CountryRegionCode
FROM Sales.SalesTerritory AS t
INNER JOIN Person.CountryRegion AS c
    ON c.CountryRegionCode = t.CountryRegionCode
GROUP BY
    t.CountryRegionCode,
    c.Name
ORDER BY total_sales DESC;
