from decimal import Decimal
import math
n = int(input())
mx = 0
mn = 99
arr = [Decimal(x) for x in input().split()]
s = 0
for x in arr:
    mx = max(mx,x)
    mn = min(mn,x)
    s += x
cmx = 0
cmn = 0
for x in arr:
    if(x == mx): cmx += 1
    if(x == mn): cmn += 1
s -= mx*cmx + mn*cmn
ans = s/Decimal(n - cmx - cmn)
print(round(ans,2))