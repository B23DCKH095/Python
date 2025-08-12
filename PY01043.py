def check(n):
    n = str(n)
    if len(n) % 2 == 1: 
        return False
    for i in n:
        if int(i) % 2 == 1: 
            return False
    rev = n[::-1]
    return rev == n

test_cases = int(input())
for _ in range(test_cases):
    arr = []
    N = int(input())
    for i in range(0, N,22):  # Start from 1 to avoid checking 0
        if check(i):
            arr.append(str(i))
    print(' '.join(arr))