for _ in range(int(input())):
    s = input()
    ok = True
    for i in s:
        if not (i == '1' or i == '2' or i == '0'):
            ok = False
    if(ok): print("YES")
    else: print("NO")