f = [0 for i in range(93)];
f[0] = 0;
f[1] = 1;
for i in range(2,93,1):
    f[i] = f[i-1] + f[i-2];
for test in range(int(input())):
    a,b = [int(x) for x in input().split()]
    arr = [];
    for x in range(a,b+1,1): arr.append(str(f[x]));
    print(' '.join(arr))