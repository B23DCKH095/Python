for test in range(int(input())):
    st = input()
    t = 0
    s = 1
    for i in range(len(st)):
        if(i%2 == 1): t += int(st[i])
        else: 
            if(int(st[i]) != 0):s *= int(st[i])
    print(f'{s} {t}')