import pandas as pd
import numpy as np
import os

# to read file
df = pd.read_excel("data/raw/HREmployee_data.xlsx")

# print number of rows and columns
print("Number of rows: ",len(df))
print("Number of columns: ",len(df.columns))

# Step 3: Show column names
print("Columns:", df.columns.tolist())

# Step 4: Create processed folder
os.makedirs("data/processed", exist_ok=True)

# Step 5: Save dataset as CSV (for Power BI and SQL)
df.to_csv("data/processed/hr_processed.csv", index=False)

print("Processed dataset saved successfully.")