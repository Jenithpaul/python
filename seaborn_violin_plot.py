# seaborn_violin_plot.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------
# Data Ingestion & Preprocessing
# ----------------------------------
# URL for the CSV data.
DATA_URL = 'https://raw.githubusercontent.com/Jenithpaul/python/refs/heads/main/Book2.csv'

# Read the CSV file into a DataFrame.
df = pd.read_csv(DATA_URL)

# Debug: print original columns and first few rows.
print("Original columns:", df.columns)
print(df.head())

# Clean the column names.
df.columns = df.columns.str.strip().str.replace(' ', '_')
print("Cleaned columns:", df.columns)

# Ensure 'Hospital_Name' exists.
if 'Hospital_Name' not in df.columns:
    print("Warning: 'Hospital_Name' column not found. Renaming first column as 'Hospital_Name'.")
    df.rename(columns={df.columns[0]: 'Hospital_Name'}, inplace=True)

# Ensure 'Rating' exists; add dummy data if missing.
if 'Rating' not in df.columns:
    np.random.seed(0)
    df['Rating'] = np.random.uniform(1, 5, size=len(df)).round(1)
    print("Added dummy 'Rating' column.")

# ----------------------------------
# Seaborn Visualization: Violin Plot for Rating Distribution
# ----------------------------------
plt.figure(figsize=(12, 7))
# Violin plot showing the distribution of ratings for each hospital.
sns.violinplot(x='Hospital_Name', y='Rating', data=df, inner="quartile", palette="Pastel1")
plt.xlabel('Hospital')
plt.ylabel('Rating')
plt.title('Distribution of Ratings by Hospital')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save and show the plot.
plt.savefig('seaborn_violin_plot.png')
plt.show()
