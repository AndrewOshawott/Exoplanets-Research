import math

n1 = (2 * math.pi) / (7.38445597)
n2 = (2 * math.pi) / (9.84821114)
n3 = (2 * math.pi) / (14.78701236)

print(n1,n2,n3)

p = 3
q = 3

print(p*n1-q*n2)
print(p*n2-q*n3)

ans = p*n1 - (p+q)*n2 + q*n3
print(ans)