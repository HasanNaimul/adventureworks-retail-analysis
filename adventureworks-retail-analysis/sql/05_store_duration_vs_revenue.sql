-- Question:
-- Does store age predict revenue?
--
-- Duration is estimated as 2019 - YearOpened because the dataset is AdventureWorks2019.

SELECT
    AnnualRevenue,
    (2019 - YearOpened) AS store_duration_years
FROM Sales.vStoreWithDemographics
ORDER BY AnnualRevenue DESC;
