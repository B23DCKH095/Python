def check(s):
    if(len(s) < 4): return False;
    if(s[-1] == 'y' and s[-2] == 'p' and s[-3] == '.'): return True;
    return False;
s = input();
if(check(s.lower())): print("yes");
else: print("no")