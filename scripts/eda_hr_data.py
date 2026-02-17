import pandas as pd
import numpy as np
import os

# read data
df = pd.read_csv("data/processed/hr_processed.csv")


# shaping the data
shape = print("\nDataset shape (Rows, Columns): ",df.shape)

# first 5 rows
print("\n",df.head())

# missing values
print(df.isnull().sum())

# attrition analysis
print(df["Attrition"].value_counts())

# department distribution
print(df["Department"].value_counts())

#average working years
print(df["TotalWorkingYears"].mean())

# attrition rate
print(df["Attrition"].value_counts(normalize=True)*100)

#dapertment wise attrition
jk=print(pd.crosstab(df["Department"],df["Attrition"], normalize= "index")*100)

print(df.groupby("Attrition")["TotalWorkingYears"].mean())

print(df.groupby("Attrition")["PerformanceRating"].mean())

print("\nAttrition rate by Job Role (%):")
job_attrition = pd.crosstab(df["JobRole"], df["Attrition"], normalize="index") * 100
print(job_attrition)

print("\nAttrition by WorkLifeBalance:")
print(pd.crosstab(df["WorkLifeBalance"], df["Attrition"], normalize="index") * 100)

print("\nAttrition by JobSatisfaction:")
print(pd.crosstab(df["JobSatisfaction"], df["Attrition"], normalize="index") * 100)

