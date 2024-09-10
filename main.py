#import numpy as np
import matplotlib.pyplot as plt
import pandas
from IPython.display import display

exoplanet_rawdata = pandas.read_csv('exoplanet_rawdata.csv')
df = exoplanet_rawdata[['Period', 'Rp/R*']]
display(df)


plot = df.plot.scatter(x='Period', y='Rp/R*', c='blue', s=2)
plt.xlim(left=0, right=60)
plt.xlabel('Period (days)')
plt.ylabel('Radius of planet (Earth radii)')
plt.title('Exoplanet data: Period v Radius (Short periods only)')
plt.show()