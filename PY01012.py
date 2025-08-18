s = input()
t = input()
idx = int(input());
line = s[:idx-1] + t + s[idx-1:]
print(line)