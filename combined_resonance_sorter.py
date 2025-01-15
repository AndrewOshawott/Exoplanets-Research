import pandas

df = pandas.read_csv('periodratios_combined_resonances.csv')

# Sort by KOI_inner and delta (absolute value of delta to prioritize closest to zero)
df_sorted = df.sort_values(by=['KOI_inner', 'delta'], key=lambda x: x.abs() if x.name == 'delta' else x)

# Drop duplicates based on KOI_inner, keeping the first (closest to zero delta)
df_result = df_sorted.drop_duplicates(subset='KOI_inner', keep='first')

print(df_sorted)
df_result.to_csv('periodratios_combined_resonances_filtered.csv')