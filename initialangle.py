import math

period = 10.30132666
T0 = 788.984754

theta0 = (-(2*math.pi / period) * (T0 - 780)) % (2 * math.pi)
print(theta0)
