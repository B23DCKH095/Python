s = input()
s += '6'
mx = 0
cur = 0
ok = 1
for x in s:
    if(x=='6' or x == '8'):
        if(x=='8'):
            cur += 1
            mx = max(mx,cur)
        else:cur = 0 
    else:
        ok = 0
if not ok or mx > 2:
    print("NO")
else: print("YES")