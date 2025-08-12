def check(i):
    s = ord(i) - ord('0')
    return (s >= 0 and s <= 2)
for _ in range(int(input())):
    n = input()
    ok = 1
    for i in n:
        if(not check(i)):
            ok = 0
            break
    if(ok==1): print('YES')
    else: print('NO')