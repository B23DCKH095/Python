
for test in range(int(input())):
    n = input()
    ok = 1
    if(len(n) < 3):
        print("NO");
        continue
    l = 1
    while(l < len(n) and int(n[l]) > int(n[l-1])): l += 1
    r = len(n)-2
    while(r >= 0 and int(n[r]) > int(n[r+1])): r -= 1
    if(l-r == 2):print("YES")
    else: print("NO")