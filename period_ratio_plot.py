import matplotlib.pyplot as plt
import pandas
from matplotlib.colors import LogNorm
from matplotlib.ticker import LogFormatter

exoplanet_multiplanetsystem_ratios = pandas.read_csv('exoplanet_multiplanetsystem_ratios.csv')
df = exoplanet_multiplanetsystem_ratios[['KOI_inner','Period_inner','KOI_outer','Period_outer','Period Ratios']]
print(df)

plot = df.plot.scatter(x='Period_inner', y='Period_outer', c='Period Ratios', s=1, colormap='viridis', norm=LogNorm(),colorbar=True)
plt.xlabel('Period of inner planet in pair (days)')
plt.ylabel('Period of outer planet in pair (days)')
plt.xscale('log')
plt.yscale('log')
plt.title('Exoplanet data: Periods of inner planet vs outer planet in pair')
plt.show()