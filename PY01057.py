import math
def nt(i):
    return (i == 2 or i == 3 or i == 5 or i== 7)
def nt2(n):
    if(n < 2): return False
    for i in range(2,int(math.sqrt(n)+1),1):
        if(n%i==0): return False
    return True
def check(n):
    for i in range(len(n)):
        if(nt2(i) and not nt(int(n[i]))): return False
        if not nt2(i) and nt(int(n[i])): return False
    return True
for _ in range(int(input())):
    n = input();
    if(check(n)): print('YES')
    else: print('NO')