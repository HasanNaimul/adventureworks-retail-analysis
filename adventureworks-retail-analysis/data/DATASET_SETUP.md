# Database and query exports

Restore an authorised copy of AdventureWorks2019 in SQL Server. The original project used a backup named `AdventureWorks2019 (1).bak`; it is not included here. This guide does not provide a new dataset download or grant redistribution rights.

Select the restored database before running files in `sql/`. Export the query results with headers and no added row-number column. Put the files in the project folder containing `requirements.txt`, then run the Python scripts from that folder.

| Export | Required columns | Separator |
| --- | --- | --- |
| `question1_part1.csv` | `country_name`, `total_sales` | Tab |
| `question1_part2.csv` | `region_name`, `sales_ytd` | Tab |
| `question2.csv` | `VacationHours`, `Bonus` | Tab |
| `avgsickleave.csv` | `Department`, `avg_sick_leave` | Tab |
| `question5.csv` | `store_duration_years`, `AnnualRevenue` | Tab |
| `q6.csv` | `AnnualRevenue`, `SquareFeet`, `NumberEmployees` | Comma |

The query files include additional columns; retaining them is fine. Use query D from `04_sick_leave_analysis.sql` for the department chart. Preserve numeric values without currency symbols or thousands separators. Check for missing values and zero denominators before interpreting the workforce-efficiency ratios.

The [repository introduction](../../README.md) maps each SQL query to its export and plotting script. No source database or exports were supplied for the October 2026 reproduction check, so existing charts remain historical project outputs rather than newly regenerated evidence.
