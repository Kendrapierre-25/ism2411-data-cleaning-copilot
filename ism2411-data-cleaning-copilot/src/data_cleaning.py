"""
Task: Data Cleaning Module

Purpose: This module provides functions to clean and preprocess raw data for analysis.

Steps:
1. Standardize column names (for example, lowercase and underscores).
2. Strip leading/trailing whitespace from product names and categories.
3. Handle missing prices and quantities (drop or fill — but be consistent).
4. Remove rows with clearly invalid values (negative quantity, negative price). 

Output: Cleaned DataFrame ready for analysis.
"""

import pandas as pd
# load data from data/raw/sales_data_raw.csv

def load_data(file_path):
    #What: loading data from a CSV file     
    #Why: to read raw data for cleaning
    df = pd.read_csv(file_path)     

    return df

def clean_column_names(df):
    #What: standardizing column names
    #Why: to ensure consistency and avoid errors in referencing columns
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df       
def handle_missing_values(df):
    #What: handling missing values in price and quantity columns
    #Why: to ensure data integrity and avoid errors during analysis
    df = df.dropna(subset=['price', 'qty'])
    return df   
def remove_invalid_rows(df):
    #What: removing rows with invalid values
    #Why: to ensure data quality and reliability of analysis
    # Convert price and qty to numbers (invalid values become NaN)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')

    # Drop rows where price or qty is missing or negative
    df = df.dropna(subset=['price', 'qty'])
    df = df[(df['price'] >= 0) & (df['qty'] >= 0)]

    return df

#Main pipeline function
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())