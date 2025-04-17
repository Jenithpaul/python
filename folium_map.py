
import pandas as pd
import folium
import numpy as np


DATA_URL = 'https://raw.githubusercontent.com/Jenithpaul/python/refs/heads/main/Book2.csv'

df = pd.read_csv(DATA_URL)

print("Original columns:", df.columns)
print(df.head())

df.columns = df.columns.str.strip().str.replace(' ', '_')
print("Cleaned columns:", df.columns)

if 'Hospital_Name' not in df.columns:
    print("Warning: 'Hospital_Name' column not found. Renaming first column as 'Hospital_Name'.")
    df.rename(columns={df.columns[0]: 'Hospital_Name'}, inplace=True)

if 'Patients' not in df.columns:
    np.random.seed(0)
    df['Patients'] = np.random.randint(50, 500, size=len(df))
    print("Added dummy 'Patients' column.")

if 'Latitude' not in df.columns or 'Longitude' not in df.columns:
    np.random.seed(0)
    df['Latitude'] = np.random.uniform(25, 49, size=len(df))
    df['Longitude'] = np.random.uniform(-124, -67, size=len(df))
    print("Added dummy 'Latitude' and 'Longitude' columns.")

map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=6)

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=(row['Patients'] / df['Patients'].max()) * 10, 
        popup=(f"<b>{row['Hospital_Name']}</b><br>"
               f"Patients: {row['Patients']}"),
        color='crimson',
        fill=True,
        fill_color='crimson',
        fill_opacity=0.6,
        tooltip=row['Hospital_Name']
    ).add_to(m)

m.save('hospitals_map.html')
print("Folium map has been saved as hospitals_map.html")
