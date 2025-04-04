import math

n1 = (2 * math.pi) / (0.98678597)
n2 = (2 * math.pi) / (3.07215234)
n3 = (2 * math.pi) / (4.64539336)

print(n1,n2,n3)

p = 1
q = 6

print(p*n1-q*n2)
print(p*n2-q*n3)

ans = p*n1 - (p+q)*n2 + q*n3
print(ans)