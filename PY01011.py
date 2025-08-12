def check(n):
    arr = [0 for i in range(10)];
    cnt = 0
    for i in str(n):
        if(arr[int(i)] ==0):
            cnt += 1
            arr[int(i)] = 1
    if(cnt%2 == 0): return False
    rev = n[::-1]
    return rev ==n
for _ in range(int(input())):
    n = int(input())
    arr =[]
    for i in range(22,n,22):
        if(check(str(i))): arr.append(str(i))
    print(' '.join(arr))