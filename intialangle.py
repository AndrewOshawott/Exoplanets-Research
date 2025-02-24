import math

period = 7.13295045
T0 = 789.419586

theta0 = -(2*math.pi / period) * (T0 - 780) + 2*(2 * math.pi)
print(theta0)

