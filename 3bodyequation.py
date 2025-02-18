import math

n1 = (2 * math.pi) / (7.13295045/365.2425)
n2 = (2 * math.pi) / (8.91897737/365.2425)
n3 = (2 * math.pi) / (11.89824703/365.2425)

print(n1,n2,n3)

p = 4
q = 4

print(p*n1-q*n2)
print(p*n2-q*n3)

ans = p*n1 - (p+q)*n2 + q*n3
print(ans)