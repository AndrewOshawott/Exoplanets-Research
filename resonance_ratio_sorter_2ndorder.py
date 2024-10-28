import pandas

exoplanet_multiplanetsystem_ratios = pandas.read_csv('exoplanet_multiplanetsystem_ratios.csv')
df = exoplanet_multiplanetsystem_ratios[['KOI_inner','Period_inner','KOI_outer','Period_outer','Period Ratios']]
df = df[(df['Period Ratios']<4.0)]

j = 3
target_value = j/(j-2)

df['Nearest Period Ratio'] = f"{j}:{j-2}"

df["delta"] = df["Period Ratios"] * ((j - 2) / j) - 1
delta = df["delta"]

df['Period_ttv'] = df['Period_outer'] / (j * df['delta'])

df_filtered = df[df["delta"].between(-0.02, 0.02)]
df_sorted = df_filtered.iloc[df_filtered["delta"].abs().argsort()]

print(df_sorted)
df_sorted.to_csv(f'periodratios_{j}to{j-2}.csv')