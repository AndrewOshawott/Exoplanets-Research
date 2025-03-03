import math

period = 7.38445597
T0 = 794.14943

theta0 = -(2*math.pi / period) * (T0 - 780) + 2*(2 * math.pi)
print(theta0)

