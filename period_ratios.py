import pandas

exoplanet_filtereddata_multiplanet_sorted = pandas.read_csv('exoplanet_filtereddata_multiplanet_sorted.csv')
df = pandas.DataFrame(exoplanet_filtereddata_multiplanet_sorted)

df['KOI_integer'] = df['KOI'].astype(str).str.split('.').str[0].astype(int)

result = []

for _, group in df.groupby('KOI_integer'):
    for i in range(1, len(group)):
        row_inner = group.iloc[i - 1]
        row_outer = group.iloc[i]

        period_ratio = row_outer['Period'] / row_inner['Period']

        result.append({
            'KOI_inner': row_inner['KOI'],
            'Period_inner': row_inner['Period'],
            'KOI_outer': row_outer['KOI'],
            'Period_outer': row_outer['Period'],
            'Period Ratios': period_ratio
        })

df_ratio = pandas.DataFrame(result)

print(df_ratio)

df_ratio.to_csv('exoplanet_multiplanetsystem_ratios.csv')