prime =[1 for x in range(1001)]
for i in range(2,1001):
    if(prime[i] == 1):
        for j in range(2*i,1001,i):  prime[j] = 0
prime[0],prime[1] = 0,0
n,m = [int(x) for x in input().split()];
for i in range(n):
    arr =[];
    a = [int(x) for x in input().split()];
    for x in a:
        if(prime[x] == 1): arr.append(str("1"));
        else: arr.append(str("0"));
    print(' '.join(arr));