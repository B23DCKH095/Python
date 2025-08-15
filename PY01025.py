s = input()
cnt = 0
arr =[]
for i in range(len(s)-1,-1,-1):
    cnt += 1
    arr.append(s[i])
    if(cnt == 3 and i != 0):
        arr.append(',')
        cnt = 0

arr.reverse()
print(''.join(arr))
    