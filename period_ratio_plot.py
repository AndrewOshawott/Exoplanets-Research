import matplotlib.pyplot as plt
import pandas

exoplanet_multiplanetsystem_ratios = pandas.read_csv('exoplanet_multiplanetsystem_ratios.csv')
df = exoplanet_multiplanetsystem_ratios[['KOI_inner','Period_inner','KOI_outer','Period_outer','Period Ratios']]
print(df)

plot = df.plot.scatter(x='Period_inner', y='Period_outer', c='Period Ratios', s=1, colormap='viridis')
plt.xlabel('Period of inner planet in pair (days)')
plt.ylabel('Period of outer planet in pair (days)')
plt.xscale('log')
plt.yscale('log')
plt.title('Exoplanet data: Period of inner planet in pair vs Period of outer planet in pair')
plt.show()