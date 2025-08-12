

def f(a,b,c,n):
    if(n==0): return
    f(a,c,b,n-1)
    print(f'{a} -> {c}')
    f(b,a,c,n-1)
n = int(input());
a = 'A'
b = 'B'
c = 'C'
f(a,b,c,n)