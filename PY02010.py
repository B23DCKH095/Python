import math
n = int(input())
while(n != 0):
    a = [int(input()) for _ in range(n)]
    a.sort()
    if(a[0] == a[-1]): print("BANG NHAU")
    else: print(f'{a[0]} {a[-1]}')
    n = int(input())
