import pandas

df = pandas.read_csv('periodratios_combined_resonances.csv')
df = df[['KOI_inner','Period_inner','KOI_outer','Period_outer','Period Ratios']]
df['KOI_integer'] = df['KOI_inner'].astype(str).str.split('.').str[0]
df_filtered = df[df['KOI_integer'].map(df['KOI_integer'].value_counts()) > 1]
df_filtered = df_filtered.drop(columns=['KOI_integer'])
print(df_filtered)

df_filtered.to_csv('multiplanet_ratios_combined_loose.csv')