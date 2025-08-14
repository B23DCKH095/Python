def add_large_numbers(a, b):
    # Hàm cộng hai số lớn dạng chuỗi
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        
        total = digit_a + digit_b + carry
        carry = total // 10
        result.append(str(total % 10))
        
        i -= 1
        j -= 1
    
    return ''.join(reversed(result))

T = int(input())
for _ in range(T):
    a, b = input().split()
    x = input().strip()
    y = input().strip()
    
    if a > b:
        a, b = b, a
    
    # Tạo số nhỏ nhất (thay b bằng a)
    x_min = x.replace(b, a)
    y_min = y.replace(b, a)
    
    # Tạo số lớn nhất (thay a bằng b)
    x_max = x.replace(a, b)
    y_max = y.replace(a, b)
    
    # Tính tổng dạng chuỗi
    min_sum = add_large_numbers(x_min, y_min)
    max_sum = add_large_numbers(x_max, y_max)
    
    print(min_sum, max_sum)