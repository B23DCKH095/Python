for test in range(int(input())):
    s = input();
    ok = 1;
    sz = s.__len__();
    if(s[0] == s[1] or sz%2 ==0): ok = 0
    for i in range(2,sz,2):
        if(s[i] != s[i-2]):ok = 0
    if(ok == 1): print('YES') 
    else: print('NO')
    