import pandas

multiplanet_matches = pandas.read_csv('multiplanet_matches.csv')
df = multiplanet_matches[['KOI_inner','Period_inner','KOI_outer','Period_outer','Period Ratios','Nearest Period Ratio','delta','Period_ttv']]

# Remove the 'Unnamed: 0' column, sort by 'KOI_outer', and round numeric columns to 6 significant figures
df_cleaned = df.sort_values(by='KOI_outer')

# Round all numeric columns to 6 significant figures
df_cleaned = df_cleaned.apply(lambda x: x.round(6) if x.dtype.kind in 'f' else x)

# Save the modified DataFrame to a new CSV to inspect the result
output_path = '/mnt/data/multiplanet_matches_cleaned.csv'
df_cleaned.to_csv(output_path, index=False)

output_path
