n = int(input())
a = [[x for x in input()] for _ in range(n)]
cnt = 0
for x in range(n):
    for i in range(n):
        for j in range(i+1,n):
            if(a[x][i] =='C' and a[x][j] =='C'): cnt += 1
            if(a[i][x] =='C' and a[j][x]== 'C'): cnt += 1
print(cnt)