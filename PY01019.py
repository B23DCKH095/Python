def check(n):
    rev = n[::-1]
    for i in range(len(n)-1):
        if(abs(ord(rev[i+1])-ord(rev[i]))!= abs(ord(n[i+1])-ord(n[i]))): return False
    return True
for _ in range(int(input())):
    n = input()
    if(check(n)): print('YES')
    else: print('NO')