import matplotlib.pyplot as plt
import pandas
from matplotlib.colors import LogNorm
from matplotlib.ticker import LogFormatter

exoplanet_multiplanetsystem_ratios = pandas.read_csv('exoplanet_multiplanetsystem_ratios.csv')
df = exoplanet_multiplanetsystem_ratios[['KOI_inner','Period_inner','KOI_outer','Period_outer','Period Ratios']]
print(df)

plot = df.plot.scatter(x='Period_inner', y='Period Ratios', s=1)
plt.xlabel('Period of inner planet in pair (days)')
plt.ylabel('Period ratios')
plt.xscale('log')
plt.yscale('log')
plt.title('Exoplanet data: placeholder')
plt.show()