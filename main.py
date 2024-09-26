import matplotlib.pyplot as plt
import pandas

exoplanet_rawdata = pandas.read_csv('exoplanet_rawdata.csv')
df = exoplanet_rawdata[['KIC', 'KOI', 'Kepler', 'Period', 'Rp', 'Status']]
df = df[(df['Period']>0) & (df['Rp']<15) & df['Status'].astype(str).str.startswith(' P')]
df['KOI_integer'] = df['KOI'].astype(str).str.split('.').str[0]
df['KOI_decimal'] = df['KOI'].astype(str).str.split('.').str[1]
print(df)

#df.to_csv('exoplanet_filtereddata.csv')

plot = df.plot.scatter(x='Period', y='Rp', c='blue', s=1)
plt.xlabel('Period (days)')
plt.ylabel('Radius of planet (Earth radii)')
plt.xscale('log')
plt.yscale('log')
plt.xticks([1, 4, 10, 40, 100, 400,1000])
plt.yticks([1, 4, 10, 20])
plt.gca().set_xticklabels([1, 4, 10, 40, 100, 400,1000])
plt.gca().set_yticklabels([1, 4, 10, 20])
plt.axhline(y=1, color='blue', linestyle='--')
plt.text(0.12, 1.1, r'$R_{Earth}$', color='blue', verticalalignment='center')
plt.axhline(y=3.86, color='blue', linestyle='--')
plt.text(0.12, 0.58, r'$R_{Mars}$', color='blue', verticalalignment='center')
plt.axhline(y=0.53, color='blue', linestyle='--')
plt.text(0.12, 4.22, r'$R_{Neptune}$', color='blue', verticalalignment='center')
plt.axhline(y=11.2, color='blue', linestyle='--')
plt.text(0.12, 12.4, r'$R_{Jupiter}$', color='blue', verticalalignment='center')
plt.title('Exoplanet data: Period v Radius (Filtered)')
plt.show()