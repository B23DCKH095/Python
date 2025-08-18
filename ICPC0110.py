for _ in range(int(input())):
    n = int(input());
    a = [int(x) for x in input().split()];
    s = 0
    for i in range(3):
        idx = 0
        for j in range(n):
            if(a[j] > a[idx]): idx = j
        s += a[idx]
        a[idx] = -a[idx]
    print(s)