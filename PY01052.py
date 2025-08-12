import math

def check(n):
    if(n < 2): return False
    for i in range(2,int(math.sqrt(n)+1),1):
        if(n%i == 0): return False
    return True
for _ in range(int(input())):
    n = str(input())
    s = 0
    for i in n:
        s += int(i)
    if(check(s)): print('YES')
    else: print('NO')