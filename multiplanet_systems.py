import pandas

exoplanet_filtereddata = pandas.read_csv('exoplanet_filtereddata.csv')
df = exoplanet_filtereddata[['KIC', 'KOI', 'Kepler', 'Period', 'Rp']]
print(df)

df['KOI_integer'] = df['KOI'].astype(str).str.split('.').str[0]
df_filtered = df[df['KOI_integer'].map(df['KOI_integer'].value_counts()) > 1]
df_filtered = df_filtered.drop(columns=['KOI_integer'])
print(df_filtered)

df_filtered.to_csv('exoplanet_filtereddata_multiplanet.csv')

df_filtered['KOI_integer'] = df_filtered['KOI'].astype(str).str.split('.').str[0].astype(int)
df_sorted = df_filtered.sort_values(by=['KOI_integer', 'Period'], ascending=[True, True])
df_sorted = df_sorted.drop(columns=['KOI_integer'])
print(df_sorted)

df_sorted.to_csv('exoplanet_filtereddata_multiplanet_sorted.csv')