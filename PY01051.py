def check(n):
    if(len(n) < 2): return False
    rev = n[::-1]
    return rev == n
for _ in range(int(input())):
    n = input()
    s = 0
    for i in str(n):
        s += int(i)
    if(check(str(s))): print('YES')
    else: print('NO')    