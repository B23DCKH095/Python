n,m = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(n)]
mx = -10000
mn = 10000
for i in range(n):
    for j in range(m):
        mx = max(mx,matrix[i][j])
        mn = min(mn,matrix[i][j])
luck = mx - mn;
ok = 0
for i in range(n):
    for j in range(m):
        if(matrix[i][j]==luck): ok = 1
if(ok==0): 
    print("NOT FOUND")
else:
    print(luck)
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==luck):print(f'Vi tri [{i}][{j}]')