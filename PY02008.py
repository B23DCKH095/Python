prime =[1 for x in range(1000001)]
for i in range(2,1000001):
    if(prime[i] == 1):
        for j in range(2*i,1000001,i):  prime[j] = 0
prime[0],prime[1] = 0,0
n,x =[int(i) for i in input().split()]
arr = [str(x)]
cur = 0
while(n > 0):
    cur +=1
    if(prime[cur]):
        n -= 1
        arr.append(str(x + cur))
        x = x + cur
print(' '.join(arr));