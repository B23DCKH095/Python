n = int(input());
a = [int(x) for x in input().split()];
a.sort();
cur =1;
for i in a:
    if(i == cur): cur +=1
print(cur);