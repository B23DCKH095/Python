n = int(input())
a = []
d = {}
for i in range(n):
    s = input()
    d[s] = d.get(s,0) + 1
cnt = 0
for i in d.keys():
    cnt += 1
print(cnt)