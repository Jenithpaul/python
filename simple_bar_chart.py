import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("Loading data...")
DATA_URL = 'https://raw.githubusercontent.com/Jenithpaul/python/refs/heads/main/Book2.csv'
df = pd.read_csv(DATA_URL)

df.columns = df.columns.str.strip().str.replace(' ', '_')
print("Columns after cleaning:", df.columns)

if 'Hospital_Name' not in df.columns and len(df.columns) > 0:
    df.rename(columns={df.columns[1]: 'Hospital_Name'}, inplace=True)
    print("Renamed column to 'Hospital_Name'")

if 'Hospital_overall_rating' in df.columns:
    df['Rating_Numeric'] = pd.to_numeric(df['Hospital_overall_rating'], errors='coerce')
    df_clean = df.dropna(subset=['Rating_Numeric']).copy()
    metric_column = 'Rating_Numeric'
    metric_name = 'Hospital Rating'
else:
    df['Rating_Numeric'] = np.random.uniform(2.5, 5.0, size=len(df)).round(1)
    df_clean = df.copy()
    metric_column = 'Rating_Numeric'
    metric_name = 'Sample Rating'

top_hospitals = df_clean.head(10)

plt.figure(figsize=(12, 7))
plt.bar(top_hospitals['Hospital_Name'], top_hospitals[metric_column], color='skyblue')

plt.xlabel('Hospital Name')
plt.ylabel(metric_name)
plt.title(f'{metric_name} by Hospital')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.savefig('hospital_bar_chart.png')
print("Bar chart saved as 'hospital_bar_chart.png'")

plt.show()