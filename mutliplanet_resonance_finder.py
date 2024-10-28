import pandas

df = pandas.read_csv('periodratios_combined_resonances.csv')
df = df[['KOI_inner','Period_inner','KOI_outer','Period_outer','Period Ratios','Nearest Period Ratio','delta','Period_ttv']]
df['KOI_integer'] = df['KOI_inner'].astype(str).str.split('.').str[0]
df = df[df['KOI_integer'].map(df['KOI_integer'].value_counts()) > 1]

inner_matches_outer = df['KOI_inner'].isin(df['KOI_outer'])
outer_matches_inner = df['KOI_outer'].isin(df['KOI_inner'])

matches = df[inner_matches_outer | outer_matches_inner]
nonmatches = df[~(inner_matches_outer | outer_matches_inner)]

matches_sorted = matches.sort_values(by="KOI_outer").reset_index(drop=True).drop(columns=['KOI_integer'])
nonmatches_sorted = nonmatches.sort_values(by="KOI_outer").reset_index(drop=True).drop(columns=['KOI_integer'])

print(matches_sorted)
print(nonmatches_sorted)

matches_sorted.to_csv('multiplanet_matches.csv')
nonmatches_sorted.to_csv('multiplanet_nonmatches.csv')