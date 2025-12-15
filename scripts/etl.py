import pandas as pd
import sqlite3
import os

# ----------------------------
# EXTRACT
# ----------------------------
DATA_PATH = os.path.join("data", "netflix_raw.csv")
df = pd.read_csv(DATA_PATH)

# ----------------------------
# TRANSFORM
# ----------------------------

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Remove duplicate records
df = df.drop_duplicates()

# Handle missing values
df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")

# Remove rows with missing release year
df = df[df["release_year"].notnull()]

# ----------------------------
# LOAD
# ----------------------------

DB_PATH = os.path.join("data", "netflix.db")
conn = sqlite3.connect(DB_PATH)

df.to_sql("netflix_titles", conn, if_exists="replace", index=False)

conn.close()

print("ETL pipeline executed successfully.")