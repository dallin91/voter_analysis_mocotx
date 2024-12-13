import pdfplumber
import pandas as pd

all_data = []

with pdfplumber.open("2024_November_Precinct_Report.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        for j, table in enumerate(tables):
            df = pd.DataFrame(table)
            df['Page'] = i + 1  # Add page number for reference
            all_data.append(df)

full_data = pd.concat(all_data, ignore_index=True)

print(full_data.head())
