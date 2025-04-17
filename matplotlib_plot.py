import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import numpy as np

# URL of the healthcare dataset (replace with your actual URL if necessary)
DATA_URL = 'https://raw.githubusercontent.com/Jenithpaul/python/refs/heads/main/Book2.csv'
# Read the CSV data into a pandas DataFrame
df = pd.read_csv(DATA_URL)

# Print original columns and a sample of the data for debugging
print("Original columns:", df.columns)
print(df.head())

# Clean column names: remove extra spaces and replace spaces with underscores
df.columns = df.columns.str.strip().str.replace(' ', '_')
print("Cleaned columns:", df.columns)

# Assuming the file contains 'Hospital_Name'. If not, try to map accordingly.
if 'Hospital_Name' not in df.columns:
    # If the hospital name is under a different column, you might update this mapping.
    print("Warning: 'Hospital_Name' column not found. Using first column as Hospital_Name.")
    df.rename(columns={df.columns[0]: 'Hospital_Name'}, inplace=True)

# Check and create dummy columns if not present
if 'Patients' not in df.columns:
    np.random.seed(0)
    df['Patients'] = np.random.randint(50, 500, size=len(df))
    print("Added dummy 'Patients' column.")

if 'Rating' not in df.columns:
    np.random.seed(0)
    df['Rating'] = np.random.uniform(1, 5, size=len(df)).round(1)
    print("Added dummy 'Rating' column.")

if 'Latitude' not in df.columns or 'Longitude' not in df.columns:
    np.random.seed(0)
    df['Latitude'] = np.random.uniform(25, 49, size=len(df))
    df['Longitude'] = np.random.uniform(-124, -67, size=len(df))
    print("Added dummy 'Latitude' and 'Longitude' columns.")

# ------------------------
# 1. Matplotlib Visualization: Sorted Bar Chart
# ------------------------
# Sort the DataFrame by 'Patients' (descending) for a clearer bar chart
df_sorted = df.sort_values(by='Patients', ascending=False)

plt.figure(figsize=(12, 7))
bars = plt.bar(df_sorted['Hospital_Name'], df_sorted['Patients'], color='skyblue')
plt.xlabel('Hospital')
plt.ylabel('Number of Patients')
plt.title('Number of Patients by Hospital (Sorted)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Add data labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{int(height)}', ha='center', va='bottom')

plt.savefig('matplotlib_bar_chart.png')
plt.show()

# ------------------------
# 2. Seaborn Visualization: Correlation Heatmap
# ------------------------
# Compute correlation between 'Patients' and 'Rating' (you can extend to more numeric columns if available)
corr = df[['Patients', 'Rating']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Healthcare Data')
plt.tight_layout()
plt.savefig('seaborn_heatmap.png')
plt.show()

# ------------------------
# 3. Folium Visualization: Hospital Locations with Circle Markers
# ------------------------
# Create a map centered around the average coordinates
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=6)

# Add circle markers; the circle radius is proportional to number of patients
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=(row['Patients'] / df['Patients'].max()) * 20,  # Scale radius (max radius = 20)
        popup=(f"<b>{row['Hospital_Name']}</b><br>"
               f"Patients: {row['Patients']}<br>"
               f"Rating: {row['Rating']}"),
        color='crimson',
        fill=True,
        fill_color='crimson',
        fill_opacity=0.6,
        tooltip=row['Hospital_Name']
    ).add_to(m)

# Save the interactive map as an HTML file.
m.save('hospitals_map.html')
print("Folium map has been saved as hospitals_map.html")
