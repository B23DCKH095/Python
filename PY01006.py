for test in range(int(input())):
    arr = [int(x) for x in input()];
    ok = 1
    for i in arr:
        if(not(i==4 or i == 7)): ok = 0
    print('YES') if ok == 1 else print('NO')
