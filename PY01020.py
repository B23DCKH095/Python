for test in range(int(input())):
    s = input();
    ok = 0;
    if(s.__len__() >1):
        if(int(s[-2]) == 8 and int(s[-1]) == 6): ok = 1
    if(ok == 1): print('YES')
    else: print('NO')