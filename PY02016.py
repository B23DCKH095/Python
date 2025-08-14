for test in range(int(input())):
    n = int(input());
    a = [int(x) for x in input().split()];
    cnt =[0 for x in range(1000001)];
    for i in a:
        cnt[i] += 1;
    cur = -1
    for i in a:
        if(cnt[i] > n/2):
            if(cur == -1): cur = i;
            if(cnt[i] > cnt[cur]):cur = i;
    if(cur == -1): print("NO");
    else: print(cur)