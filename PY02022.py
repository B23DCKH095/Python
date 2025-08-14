prime =[1 for x in range(1000001)]
for i in range(2,1000001):
    if(prime[i] == 1):
        for j in range(2*i,1000001,i):  prime[j] = 0
prime[0],prime[1] = 0,0
cnt = [0 for x in range(1000001)]
v = [False for x in range(1000001)]
n = int(input());
a = [int(x) for x in input().split()]
for i in a:
    if(prime[i] == 1): cnt[i] += 1
for i in a:
    if not v[i]:
        v[i] = True;
        if(prime[i]):
            pt =[str(i),str(cnt[i])];
            print(' '.join(pt));
        
