def check(n):
    arr = str(n)
    s = 0
    for i in range(len(arr)-1):
        if(abs(int(arr[i]) - int(arr[i+1])) != 2): 
            return False
    for i in arr:
        s += int(i)
    if(s%10 ==0): return True
    return False
for test in range(int(input())):
    n = input()
    if(check(n)): print('YES')
    else: print('NO')