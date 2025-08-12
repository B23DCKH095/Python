for test in range(int(input())):
    arr = [int(x) for x in input()];
    if(arr[0] == arr[-2] and arr[1] == arr[-1]):
        print("YES")
    else: print("NO")