import math

period = 23.08898942
T0 = 773.589205

theta0 = (-(2*math.pi / period) * (T0 - 780)) % (2 * math.pi)
print(theta0)
