# Dataset Setup

This repository uses the AdventureWorks2019 database.

## Restore the database

Use SQL Server Management Studio to restore the backup file:

- source backup file: `AdventureWorks2019 (1).bak`
- target database name: `AdventureWorks2019`

## Important GitHub note

The `.bak` file is around 200 MB and is intentionally excluded from the GitHub-ready zip because large binary backups are not ideal for a portfolio repository and may exceed GitHub-friendly limits and workflows.

Recommended approach:

- keep the `.bak` file locally
- mention it in the README
- optionally upload it separately to cloud storage and link it from the repo

## Workflow

1. Restore the database.
2. Run the SQL scripts in the `sql/` folder.
3. Export results to CSV.
4. Run the matching Python script in the `python/` folder.
