s = input();
tg = 0
hoa = 0
for x in s:
    if(x >= 'a' and x <='z'): tg += 1
    else: hoa += 1
if(tg >= hoa): print(s.lower())
else: print(s.upper())