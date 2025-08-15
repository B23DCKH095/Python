for _ in range(int(input())):
    s = input()
    n = len(s)
    ok = True
    for i in range(1,n,1):
        l  = abs(ord(s[i]) - ord(s[i-1]))
        r = abs(ord(s[n-1-i]) - ord(s[n-i]))
        if(l != r): ok = False
    if(ok): print("YES")
    else: print("NO")