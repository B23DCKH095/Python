for test in range(int(input())):
    n,x,m=[float(x) for x in input().split()]
    cnt = 0;
    lai = (1 + x/100);
    while(n <m):
        n = n*lai;
        cnt += 1;
    print(cnt);
