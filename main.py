import matplotlib.pyplot as plt
import pandas


exoplanet_rawdata = pandas.read_csv('exoplanet_rawdata.csv')
df = exoplanet_rawdata[['KIC', 'KOI', 'Kepler', 'Period', 'Rp', 'Status']]
df = df[(df['Period']>0) & df['Status'].astype(str).str.startswith(' P')]
df['KOI_integer'] = df['KOI'].astype(str).str.split('.').str[0]
df['KOI_integer_count'] = df['KOI_integer'].map(df['KOI_integer'].value_counts())
koi_integer_count_array = df['KOI_integer_count'].value_counts().sort_index().to_numpy()
#print(koi_integer_count_array)
print(df)

#df_sorted = df.sort_values(by='KOI_integer_count')
#print(df_sorted)

df.to_csv('exoplanet_filtereddata_KOI.csv')

markers = {
    1: ('o', '#440154', 2, 'One', koi_integer_count_array[0]),
    2: ('o', '#46327e', 10, 'Two', koi_integer_count_array[1]),
    3: ('^', '#365c8d', 20, 'Three', koi_integer_count_array[2]),
    4: ('s', '#277f8e', 25, 'Four', koi_integer_count_array[3]),
    5: ('*', '#1fa187', 50, 'Five', koi_integer_count_array[4]),
    6: ('H', '#4ac16d', 55, 'Six', koi_integer_count_array[5]),
    7: ('X', '#a0da39', 55, 'Seven', koi_integer_count_array[6]),
    8: ('8', '#fde725', 60, 'Eight', koi_integer_count_array[7])
}


for count, (marker, color, size, label, planet_count) in markers.items():
    subset = df[df['KOI_integer_count'] == count]
    plt.scatter(subset['Period'], subset['Rp'], marker=marker, color=color, s=size, edgecolors='black', linewidths=0.4, label=f'{label}: {planet_count}')

plt.legend(loc='lower right')
plt.xlabel('Period (days)')
plt.ylabel('Radius of planet (Earth radii)')
plt.xscale('log')
plt.yscale('log')
plt.xticks([1, 4, 10, 40, 100, 400,1000])
plt.yticks([1, 4, 10, 20])
plt.gca().set_xticklabels([1, 4, 10, 40, 100, 400,1000])
plt.gca().set_yticklabels([1, 4, 10, 20])
plt.ylim(0,25)
plt.axhline(y=1, color='blue', linestyle='--')
plt.text(0.12, 1.12, r'$R_{Earth}$', color='blue', verticalalignment='center')
plt.axhline(y=3.86, color='blue', linestyle='--')
plt.text(0.12, 0.59, r'$R_{Mars}$', color='blue', verticalalignment='center')
plt.axhline(y=0.53, color='blue', linestyle='--')
plt.text(0.12, 4.30, r'$R_{Neptune}$', color='blue', verticalalignment='center')
plt.axhline(y=11.2, color='blue', linestyle='--')
plt.text(0.12, 12.4, r'$R_{Jupiter}$', color='blue', verticalalignment='center')
plt.title('Exoplanet data: Period v Radius (Filtered)')
plt.show()