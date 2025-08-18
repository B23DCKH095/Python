base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for _ in range(int(input())):
    num,x = [int(i) for i in input().split()]
    ans = []
    while(num > 0):
        tmp = num%x
        ans.append(tmp)
        num = num //x 
    ans.reverse()
    cov = [base[int(i)] for i in ans]
    
    print(''.join(cov))