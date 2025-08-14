t = int(input());
cur = 1;
a = [0 for i in range(10)];
a[0] = 1;
for i in range(1,10):
    cur *=i;
    a[i] = cur;

while(t > 0):
    t-= 1;
    s = input();
    r = int(s);
    res = 0;
    for i in s:
        res += a[int(i)];
    if(res == r): print("Yes");
    else: print("No");