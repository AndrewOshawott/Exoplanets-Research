import math

n1 = 2 * math.pi / 10.43545334
n2 = 2 * math.pi / 17.45319318
n3 = 2 * math.pi / 21.72027051



p = 7
q = 24

ans = p*n1 - (p+q)*n2 + q*n3
print(ans)