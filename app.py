import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
data_2007 = pd.read_csv('baby_names_2007.csv')
data_2020 = pd.read_csv('baby_names_2020.csv')

# Filter top 100 names from 2007
top_100_2007 = data_2007[data_2007['rank'] <= 100]

# Filter names outside top 100 in 2020
outside_top_100_2020 = data_2020[data_2020['rank'] > 100]

# Merge datasets on 'name'
merged_data = pd.merge(top_100_2007[['name', 'rank']], outside_top_100_2020[['name', 'rank']], on='name', suffixes=('_2007', '_2020'))

# Calculate rank difference
merged_data['rank_diff'] = merged_data['rank_2007'] - merged_data['rank_2020']

# Sort by rank difference
merged_data_sorted = merged_data.sort_values(by='rank_diff', ascending=False)

# Select top 10 names
top_10_decline = merged_data_sorted.head(10)

# Plotting
plt.figure(figsize=(10, 6))
plt.barh(top_10_decline['name'], top_10_decline['rank_diff'], color='skyblue')
plt.xlabel('Rank Difference (2007 - 2020)')
plt.title('Top 10 Baby Names with Significant Decline in Popularity (2007 to 2020)')
plt.gca().invert_yaxis()
plt.show()
