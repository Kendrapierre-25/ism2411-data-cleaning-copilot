# ism2411-data-cleaning-copilot

This project showcases a simple but clean data-processing for messy sales data.  
The script loads a raw CSV file, applies several cleaning steps, and outputs a cleaned dataset ready for analysis.

# Project Structure
ism2411-data-cleaning-copilot/
├── data/
│ ├── raw/
│ │ └── sales_data_raw.csv
│ └── processed/
│ └── sales_data_clean.csv
├── src/
│ └── data_cleaning.py
├── README.md
└── reflection.md

# Cleaning Steps

The script performs:

- Standardizing column names  
- Removing whitespace in product/category fields  
- Handling missing values consistently  
- Removing rows with negative quantities/prices  
- Saving cleaned data to data/processed/

# How to Run

From the project root: python src/data_cleaning.py

This Creates:
data/processed/sales_data_clean.csv
which prints a preview4 of the cleamed dataset
