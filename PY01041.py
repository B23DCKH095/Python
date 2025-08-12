def tang(n):
    for i in range(len(n)-1):
        if(n[i] >= n[i+1]): return False
    return True
def giam(n):
    for i in range(len(n)-1):
        if(n[i] <= n[i+1]): return False
    return True
def chat(n):
    for i in range(len(n)-1):
        if(n[i] == n[i+1]): return True
    return False
for test in range(int(input())):
    n = input()
    ok = 1
    if(len(n) < 3): ok = 0
    if (tang(n) or giam(n) or chat(n)): ok = 0
    if(ok == 1):print('YES')
    else: print('NO')