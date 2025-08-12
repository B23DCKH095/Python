import math
def check(n):
    if(n < 2): return False
    for i in range(2,int(math.sqrt(n)+1),1):
        if(n%i ==0): return False
    return True
for _ in range(int(input())):
    n = input()
    if(check(int(n[-4:]))):print('YES')
    else: print('NO')
    