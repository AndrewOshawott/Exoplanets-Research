import matplotlib.pyplot as plt
import pandas

exoplanet_multiplanetsystem_ratios = pandas.read_csv('exoplanet_multiplanetsystem_ratios.csv')
df = exoplanet_multiplanetsystem_ratios[['KOI_inner','Period_inner','KOI_outer','Period_outer','Period Ratios']]
print(df)

histogram = df.plot.hist(column='Period Ratios', bins=96)
plt.xlabel('Period Ratios')
plt.xscale('log')

plt.title('Exoplanet data: Histogram of period ratios')
plt.show()

histogram2 = df.plot.hist(column='Period Ratios', bins=96)
plt.xlabel('Period Ratios')
plt.xlim(1,4.1)
plt.title('Exoplanet data: Histogram of period ratios')
plt.show()