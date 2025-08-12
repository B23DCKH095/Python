import math
def nt(n):
    if(n < 2): return False
    for i in range(2,int(math.sqrt(n)+1),1):
        if(n%i==0): return False
    return True
    
def check(n):
    s = 0
    for i in range(len(n)):
        s += int(n[i])
        if(i%2 == 1 and int(n[i])%2 == 0): return False
        if(i%2 == 0 and int(n[i])%2 == 1): return False
    return nt(s)
for _ in range(int(input())):
    n = input()
    if(check(n)):print('YES')
    else: print('NO')