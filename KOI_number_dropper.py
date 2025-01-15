import pandas

df = pandas.read_csv('periodratios_combined_resonances_filtered.csv')
print(df)

df['KOI_integer'] = df['KOI_inner'].astype(str).str.split('.').str[0]
df_filtered = df[df['KOI_integer'].map(df['KOI_integer'].value_counts()) > 1]
df_filtered = df_filtered.drop(columns=['KOI_integer'])
print(df_filtered)

df_filtered.to_csv('periodratios_combined_resonances_filtered_drop_nonduplicates.csv')