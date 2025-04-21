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

if 'Hospital_Type' in df.columns:
    hospital_types = df['Hospital_Type'].value_counts().head(5)
    labels = hospital_types.index
    sizes = hospital_types.values
    chart_title = 'Distribution of Hospital Types'
else:
    labels = df['Hospital_Name'].head(5)
    sizes = np.random.randint(50, 200, size=5)
    chart_title = 'Sample Hospital Distribution'

plt.figure(figsize=(10, 8))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',  
    startangle=90,
    shadow=True,
    explode=[0.05] * len(labels),  
    colors=plt.cm.Pastel1.colors  
)

plt.title(chart_title)

plt.axis('equal')

plt.savefig('hospital_pie_chart.png')
print("Pie chart saved as 'hospital_pie_chart.png'")

plt.show()