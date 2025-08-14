import math
for _ in range(int(input())):
    a = ["1"];
    n = int(input());
    for i in range(2,int(math.sqrt(n)+1),1):
        if(n%i ==0):
            cnt = 0;
            while(n%i ==0):
                cnt += 1
                n/=i;
            a.append(str(i) + "^"+ str(cnt));
    if(n >1): a.append(str(int(n)) + "^"+ str(1));
    print(" * ".join(a));