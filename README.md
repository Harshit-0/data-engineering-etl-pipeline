# Data Engineering ETL Pipeline – Netflix Dataset

## Overview
This project demonstrates a simple end-to-end ETL (Extract, Transform, Load) pipeline using Python.

## Data Source
Netflix Movies and TV Shows dataset in CSV format.

## ETL Workflow
- Extract: Read raw CSV data using Pandas
- Transform:
  - Standardized column names
  - Removed duplicate records
  - Handled missing values
  - Filtered invalid records
- Load:
  - Stored cleaned data into a SQLite database for analysis

## Tech Stack
- Python
- Pandas
- SQLite

## How to Run
```bash
python scripts/etl.py
