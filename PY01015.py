for test in range(int(input())):
    s = input();
    ok = 1;
    for i in range(0,s.__len__()-1,1):
        if(s[int(i)] > s[int(i+1)]): ok = 0
    if(ok == 1): print('YES') 
    else: print('NO')