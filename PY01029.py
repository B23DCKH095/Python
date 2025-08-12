import math
def check(n):
    rev = n[::-1]
    return math.gcd(int(n),int(rev)) ==1
for _ in range(int(input())):
    n = input()
    if(check(n)): print('YES')
    else: print('NO')   