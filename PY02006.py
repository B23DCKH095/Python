for _ in range(int(input())):
    n = int(input());
    a = [int(x) for x in input().split()];
    b = [int(x) for x in input().split()];
    a.sort();
    b.sort();
    ok = True;
    for i in range(n):
        if(a[i] > b[i]): ok = False;
    if(ok): print("YES");
    else: print("NO");