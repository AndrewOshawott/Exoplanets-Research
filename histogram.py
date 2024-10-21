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
plt.axvline(x=(5/4), color='black', linestyle=':')
plt.axvline(x=(4/3), color='black', linestyle=':')
plt.axvline(x=(7/5), color='black', linestyle=':')
plt.axvline(x=(3/2), color='black', linestyle=':')
plt.axvline(x=(5/3), color='black', linestyle=':')
plt.axvline(x=(2/1), color='black', linestyle=':')
plt.axvline(x=(3/1), color='black', linestyle=':')
plt.text(1.17, 39, r'$5:4$', color='black', verticalalignment='center', rotation=90, fontsize=8)
plt.text(1.265, 39, r'$4:3$', color='black', verticalalignment='center', rotation=90, fontsize=8)
plt.text(1.34, 36.5, r'$7:5$', color='black', verticalalignment='center', rotation=90, fontsize=8)
plt.text(1.43, 39, r'$3:2$', color='black', verticalalignment='center', rotation=90, fontsize=8)
plt.text(1.6, 39, r'$5:3$', color='black', verticalalignment='center', rotation=90, fontsize=8)
plt.text(1.93, 39, r'$2:1$', color='black', verticalalignment='center', rotation=90, fontsize=8)
plt.text(2.93, 39, r'$3:1$', color='black', verticalalignment='center', rotation=90, fontsize=8)

plt.show()