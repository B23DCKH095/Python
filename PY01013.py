import math

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    s = 0
    for i in str(n):  # Chuyển số thành chuỗi để duyệt các chữ số
        s += int(i)   # Chuyển chữ số thành số để cộng
    return nt(s)      # Trả về trực tiếp kết quả kiểm tra số nguyên tố

for test in range(int(input())):
    a, b = map(int, input().split())
    c = math.gcd(a, b)
    if check(c):
        print('YES')
    else:
        print('NO')