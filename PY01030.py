import math

n,k = input().split()
s = 1
arr =[]
for i in range(int(k)):
    s *= 10
for i in range(int(s/10) ,s,1):
    if(math.gcd(i,int(n))==1): arr.append(str(i))
for i in range(0,len(arr),10):
    x = [str(a) for a in arr[i:i+10]];
    print(' '.join(x))