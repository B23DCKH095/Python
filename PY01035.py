base = {"000":"0","001":"1","010":"2","011":"3","100":"4","101":"5","110":"6","111":"7"}
s = input()
du = len(s)%3
if(du != 0):
    for i in range(3- du):
        s = "0"+ s
arr = []
for i in range(0,len(s),3):
    tmp  = s[i:i+3]
    arr.append(base[tmp])
reversed(arr)
print("".join(arr))