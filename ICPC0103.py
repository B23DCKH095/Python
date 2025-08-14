import math

for test in range(int(input())):
    s = input()
    arr = []
    current_digits = []  # Đổi tên biến cho rõ nghĩa hơn
    
    for char in s:
        if '0' <= char <= '9':
            current_digits.append(char)
        else:
            if current_digits:  # Chỉ thêm vào arr nếu có số được lưu
                arr.append(''.join(current_digits))
                current_digits = []  # Reset lại mảng
    
    # Thêm số cuối cùng nếu chuỗi kết thúc bằng số
    if current_digits:
        arr.append(''.join(current_digits))
    
    mx = 0;
    for number in arr:
        mx = max(mx,int(number));
    print(mx);