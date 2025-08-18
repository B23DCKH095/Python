for _ in range(int(input())):
    s = input()
    words = [x for x in s.split()]
    arr = []
    cnt = 0
    for x in words:
        d = len(x)
        if(cnt + d > 100): break
        cnt += d + 1
        arr.append(x)
    print(' '.join(arr))