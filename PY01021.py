for _ in range(int(input())):
    s = input()
    tong = 0
    a =[]
    for x in s:
        if(x.isdigit()): tong += int(x)
        else: a.append(x)
    a = sorted(a)
    line = ''.join(a) + str(tong)
    print(line)