for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}
    for x in a:
        d[x] = d.get(x,0)+1
    for x in set(a):
        if(d[x]%2 == 1): print(x)