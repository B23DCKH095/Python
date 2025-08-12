import math

def check(n):
    if(n < 2): return False;
    for i in range(2,int(math.sqrt(n)+1),1):
        if(n%i==0): return False
    return True
for test in range(int(input())):
    s = input()
    print('YES') if(check(int(s[:3])) and check(int(s[-3:]))) else print('NO')