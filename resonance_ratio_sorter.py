import pandas

exoplanet_multiplanetsystem_ratios = pandas.read_csv('exoplanet_multiplanetsystem_ratios.csv')
df = exoplanet_multiplanetsystem_ratios[['KOI_inner','Period_inner','KOI_outer','Period_outer','Period Ratios']]
df = df[(df['Period Ratios']<4.0)]

threshold = 2/96
target_value = 3/2

df_filtered = df[abs(df['Period Ratios'] - target_value) <= threshold]
df_sorted = df_filtered.assign(Difference=abs(df_filtered['Period Ratios'] - target_value)) \
                       .sort_values(by='Difference')
df_sorted = df_sorted.drop(columns=['Difference'])
print(df_sorted)

df_sorted.to_csv('periodratios_3to2.csv')