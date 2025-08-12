for test in range(int(input())):
    s = input();
    arr =[]
    for i in range(1,s.__len__(),2):
        for j in range(int(s[int(i)])):
            arr.append(s[i-1])
    print(''.join(arr))