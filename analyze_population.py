import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'API_SP.POP.TOTL_DS2_en_csv_v2_45183.csv'
population_data = pd.read_csv(file_path, skiprows=4)

# Filter data for the year 2020
population_2020 = population_data[['Country Name', '2020']]

# Select specific countries
selected_countries = ['United States', 'China', 'India', 'Brazil', 'Indonesia']
population_2020_selected = population_2020[population_2020['Country Name'].isin(selected_countries)]

# Rename columns for clarity
population_2020_selected.columns = ['Country', 'Population']

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(population_2020_selected['Country'], population_2020_selected['Population'], color=['blue', 'red', 'green', 'orange', 'purple'])
plt.xlabel('Country')
plt.ylabel('Total Population in 2020')
plt.title('Total Population of Selected Countries in 2020')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure
plt.savefig('population_distribution_2020.png')

# Show the plot
plt.show()
