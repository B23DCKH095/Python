for test in range(int(input())):
    arr =[]
    s = input()
    cur  ='0'
    cnt =1
    for i in range(len(s)):
        if(cur != s[i]):
            arr.append(str(cnt))
            arr.append(s[i])
            cnt = 1
            cur = s[i]
        else:
            cnt += 1
    print(''.join(arr))