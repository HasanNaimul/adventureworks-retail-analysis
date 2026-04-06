-- Question:
-- What are the regional sales patterns in the best-performing country?
-- Assumption based on prior analysis: US is the highest-performing country.

SELECT
    t.Name AS region_name,
    t.SalesYTD AS sales_ytd
FROM Sales.SalesTerritory AS t
WHERE t.CountryRegionCode = 'US'
ORDER BY sales_ytd DESC;
