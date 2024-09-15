import matplotlib.pyplot as plt
import pandas

exoplanet_rawdata = pandas.read_csv('exoplanet_rawdata.csv')
df = exoplanet_rawdata[['KIC', 'KOI', 'Kepler', 'Period', 'Rp/R*', 'Status']]
df = df[(df['Period']>0) & (df['Rp/R*']<15) & df['Status'].astype(str).str.startswith(' P')]
print(df)

df.to_csv('exoplanet_filtereddata.csv')

plot = df.plot.scatter(x='Period', y='Rp/R*', c='blue', s=1)
plt.xlabel('Period (days)')
plt.ylabel('Radius of planet (Earth radii)')
plt.xscale('log')
plt.yscale('log')
plt.title('Exoplanet data: Period v Radius (Filtered)')
plt.show()