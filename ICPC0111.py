for _ in range(int(input())):
    n,k = input().split();
    a = [int(x) for x in input().split()];
    b = [];
    for i in range(int(k),int(n),1): b.append(str(a[i]));
    for i in range(int(k)): b.append(str(a[i]));
    print(' '.join(b));