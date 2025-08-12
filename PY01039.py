for test in range(int(input())):
    s = input()
    cnt =0
    a = [0 for i in range(10)]
    for i in s:
        if(a[int(i)]==0):
            cnt += 1
            a[int(i)] = 1
    ok = 1
    if(cnt != 2): ok = 0;
    for i in range(len(s)-1):
        if(s[i] == s[i+1]):
            ok = 0
    if(ok == 1): print('YES')
    else: print('NO')