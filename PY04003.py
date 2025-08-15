import math
a,b = [int(x) for x in input().split()];
x = math.gcd(a,b);
a/= x
b/=x;
print(f"{a:.0f}/{b:.0f}");