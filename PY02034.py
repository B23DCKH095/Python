s = input()
d = {}
for i in range(0,len(s),2):
    tmp = s[i:i+2]
    if(len(tmp) < 2): continue
    d[s[i:i+2]] = d.get(s[i:i+2],0)+1
for x,y in d.items():
    print(f'{x} {y}')