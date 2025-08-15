import math
a,b,c,d = [int(x) for x in input().split()]
tu = a*d + b*c
mau = b*d
x = math.gcd(tu,mau)
tu/=x
mau /= x
print(f"{tu:.0f}/{mau:.0f}")