import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir('Practical10')  # Change to the directory where the CSV file is located
# Check the current working directory and list files to ensure the CSV file is accessible
print('Current directory:', os.getcwd())
# List files in the directory to confirm the presence of the CSV file
print('Files in directory:', os.listdir())
dalys_data = pd.read_csv('dalys-rate-from-all-causes.csv')
print('Data type:', type(dalys_data)) # Check the type of the loaded data
print('First 5 rows:')  # Display the first 5 rows of the DataFrame to verify it loaded correctly
print(dalys_data.head(5))
print('Data info:') # Display information about the DataFrame, including column names, data types, and non-null counts
dalys_data.info()
print('Data description:')# Display statistical summary of the DataFrame, including count, mean, std, min, 25%, 50%, 75%, and max for numeric columns
print(dalys_data.describe())
print('Entity column:') # Display the 'Entity' column to verify its contents and ensure it is loaded correctly
print(dalys_data["Entity"].unique())
# Display the first 10 rows of columns 2 to 4
first_10 = dalys_data.iloc[0:10,2:4] 
print('First 10 rows of columns 2 to 4:')
print(first_10)

dalys_col = dalys_data.columns[3]  # Assuming the DALYs (rate) column is the 4th column (index 3)

# Find the year with the maximum DALYs among these first 10 rows
max_row_afghan_first10 = first_10.loc[first_10[dalys_col].idxmax()]
max_year_afghan_first10 = int(max_row_afghan_first10["Year"])

print('Year with maximum DALYs among the first 10 rows:', max_year_afghan_first10)
print(max_row_afghan_first10)

# comment:
# Among the first 10 years recorded for Afghanistan, the year with the maximum DALYs is 1990 with a DALYs (rate) of 50000.0.

zimabbwe_mask = dalys_data["Entity"] == "Zimbabwe"
zimabbwe_years = dalys_data.loc[zimabbwe_mask, 'Year']
print('Years recorded for Zimbabwe:')
print(zimabbwe_years.to_string(index=False))

zimabbwe_first_year = int(zimabbwe_years.min())
zimabbwe_last_year = int(zimabbwe_years.max())
print('First year recorded for Zimbabwe:', zimabbwe_first_year)
print('Last year recorded for Zimbabwe:', zimabbwe_last_year)

#comment:
#Zimbabwe data were recorded from 1990 to 2019, with the first year being 1990 and the last year being 2019.

#find countries with maximum and minimum DALYs in the year 2019
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ['Entity',dalys_col]]

max_2019 = recent_data.loc[recent_data[dalys_col].idxmax()]
min_2019 = recent_data.loc[recent_data[dalys_col].idxmin()]

print('Country with maximum DALYs in 2019:', max_2019["Entity"], 'with a rate of', max_2019[dalys_col])
print('Country with minimum DALYs in 2019:', min_2019["Entity"], 'with a rate of', min_2019[dalys_col])

#Comment:
#In 2019, the country with the maximum DALYs was Lesotho with a rate of 90771.64, while the country with the minimum DALYs was Singapore with a rate of 15045.11.

#plot DALYs over time for one of the countries identified above
plot_country = max_2019["Entity"]  # You can change this to min_2019["Entity"] to plot the other country
country_data = dalys_data.loc[dalys_data["Entity"] == plot_country, ['Year', dalys_col]]
plt.figure(figsize=(8, 5))
plt.plot(country_data['Year'], country_data[dalys_col], marker='o')
plt.title(f'DALYs (rate) over time for {plot_country}')
plt.xlabel('Year')
plt.ylabel('DALYs (rate)')
plt.xticks(country_data['Year'].unique(), rotation=90)  # Set x-ticks to the unique years available for the country
plt.grid()
plt.tight_layout()  # Adjust layout to prevent overlap
plt.savefig('dalys_over_time_' + str(plot_country).replace(" ", "_") + '.png', dpi=300)  # Save the plot as a PNG file with a name based on the country
plt.show()

#Own question: What was the distribution of DALYs across all countriese in 2019?
mean_2019 = recent_data[dalys_col].mean()
median_2019 = recent_data[dalys_col].median()
min_value_2019 = recent_data[dalys_col].min()
max_value_2019 = recent_data[dalys_col].max()

print('Own question: What was the distribution of DALYs across all countries in 2019?')
print('Mean DALYs (rate) in 2019:', mean_2019)
print('Median DALYs (rate) in 2019:', median_2019)
print('Minimum DALYs (rate) in 2019:', min_value_2019)
print('Maximum DALYs (rate) in 2019:', max_value_2019)

plt.figure(figsize=(8, 5))
plt.hist(recent_data[dalys_col], bins=20)
plt.axvline(mean_2019, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_2019:.2f}')
plt.axvline(median_2019, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_2019:.2f}')
plt.legend()
plt.title('Distribution of DALYs (rate) across all countries in 2019')
plt.xlabel('DALYs (rate)')
plt.ylabel('Number of Countries')
plt.grid()
plt.tight_layout()  # Adjust layout to prevent overlap
plt.savefig('dalys_distribution_2019.png', dpi=300)  # Save the plot as a PNG file
plt.show()