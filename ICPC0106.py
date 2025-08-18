base =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'];
for _ in range(int(input())):
    x = int(input());
    s = input()
    num = 0
    for i in range(len(s)-1,-1,-1):
        num = num*2 + int(s[i])
    ans = []
    while(num > 0):
        tmp = num%x
        ans.append(tmp)
        num = num //x 
    cov = [base[int(i)] for i in ans]
    print(''.join(cov))