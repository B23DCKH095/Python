n = int(input());
a = [];
for i in range(n):
    s = input();
    a.append(s);
myset = set(a);
print(len(myset));