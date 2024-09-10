import pandas
import math

jupiter_moons = pandas.read_csv('jupiter_moons.csv')
df = jupiter_moons[['Name','a','Period','e','i','m_v']]

periods = jupiter_moons['Period']
n = (2 * math.pi) / periods
print(n[0]-(2*n[1]))
print(n[1]-(2*n[2]))
print(n[0] - (3 * n[1]) + (2 * n[2]))