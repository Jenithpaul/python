import pandas as pd
import folium
import numpy as np

print("Loading data...")
DATA_URL = 'https://raw.githubusercontent.com/Jenithpaul/python/refs/heads/main/Book2.csv'
df = pd.read_csv(DATA_URL)

df.columns = df.columns.str.strip().str.replace(' ', '_')
print("Columns after cleaning:", df.columns)

if 'Hospital_Name' not in df.columns and len(df.columns) > 0:
    df.rename(columns={df.columns[1]: 'Hospital_Name'}, inplace=True)
    print("Renamed column to 'Hospital_Name'")

df['Patient_Count'] = np.random.randint(100, 1000, size=len(df))
print("Added 'Patient_Count' column with random values for visualization")

if 'Latitude' not in df.columns or 'Longitude' not in df.columns:
    np.random.seed(0)  # For reproducible results
    df['Latitude'] = np.random.uniform(25, 49, size=len(df))  # US latitude range
    df['Longitude'] = np.random.uniform(-124, -67, size=len(df))  # US longitude range
    print("Added 'Latitude' and 'Longitude' columns with random values")

map_center = [df['Latitude'].mean(), df['Longitude'].mean()]

m = folium.Map(location=map_center, zoom_start=4)

for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<b>{row['Hospital_Name']}</b><br>Rating: {row.get('Hospital_overall_rating', 'N/A')}",
        tooltip=row['Hospital_Name']
    ).add_to(m)

m.save('index.html')
print("Folium map saved as 'hospital_map.html'")