for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    mn =  1000000
    mx = -1000000
    sorted(a)
    for i in range(n):
        mn = min(mn,a[i])
        mx = max(mx,a[i])
    cnt = 0
    for i in range(mn,mx+1,1):
        if not(i in a): cnt+= 1
    print(cnt)