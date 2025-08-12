for _ in range(int(input())):
    n = input()
    ex = 0
    s = 1
    t = 0
    for i in range(len(n)):
        if(i%2 == 1):
            if(int(n[i])!= 0):
                ex = 1
                s *= int(n[i])
        else:
            t += int(n[i])
    if(ex ==0): s = 0
    print(f'{t} {s}')