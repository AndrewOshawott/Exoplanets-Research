import math

n1 = (2 * math.pi) / (5.24969846)
n2 = (2 * math.pi) / (7.41088006)
n3 = (2 * math.pi) / (10.43545334)

print(n1,n2,n3)

p = 5
q = 7

print(p*n1-q*n2)
print(p*n2-q*n3)

ans = p*n1 - (p+q)*n2 + q*n3
print(ans)