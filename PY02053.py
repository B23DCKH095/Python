n = int(input())
l,r = 0,0
for i in range(n):
    arr = [int(x) for x in input().split()]
    for x in range(0,n-i-1,1):
        l += arr[x]
    for x in range(n-i,n,1):
        r += arr[x]
k = int(input())
ans = abs(l-r)
if(ans <= k): print("YES")
else: print("NO")
print(ans)