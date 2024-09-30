import matplotlib.pyplot as plt
import pandas

exoplanet_multiplanetsystem_ratios = pandas.read_csv('exoplanet_multiplanetsystem_ratios.csv')
df = exoplanet_multiplanetsystem_ratios[['KOI_inner','Period_inner','KOI_outer','Period_outer','Period Ratios']]
df = df[(df['Period Ratios']<4.0)]
print(df)

histogram = df.plot.hist(column='Period Ratios', bins=96, color='blue')
plt.xlabel('Period Ratios $(P_{outer}/P_{inner})$')
plt.ylabel('$N$')
plt.xlim(1,4.0)
plt.ylim(0,41)
plt.legend().remove()
plt.title('Exoplanet data: Histogram of period ratios')
plt.show()