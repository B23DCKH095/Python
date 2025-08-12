import math
def check1(n):
    n = int(n)
    if(n == 2 or n == 3 or n == 5 or n==7): return True
    return False
def check(n):
    if(n < 2): return False
    for i in range(2,int(math.sqrt(n)+1),1):
        if(n%i==0): return False
    return True
for test in range(int(input())):
    n = input()
    nt = 0
    pnt = 0
    ok = 1
    for i in n:
        if(check1(i)): nt += 1
        else: pnt += 1
    if(nt <= pnt): ok = 0
    if not check(len(n)): ok = 0
    if(ok == 1): print('YES')
    else: print('NO')