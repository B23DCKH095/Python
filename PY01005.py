cnt = 0
a = [int(x) for x in input()];
for i in a:
    if(i==4 or i == 7):
        cnt += 1
print('YES') if (cnt == 7 or cnt == 4) else print("NO")