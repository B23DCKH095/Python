d = {}
for _ in range(int(input())):
    s = input().lower()
    # Thay thế các ký tự đặc biệt bằng khoảng trắng
    for char in [',', '.', '?', '!', ':', ';', '-', '/']:
        s = s.replace(char, ' ')
    words = s.split()
    for x in words:
        d[x] = d.get(x, 0) + 1  # Tăng giá trị của key x lên 1 (nếu không tồn tại, mặc định là 0)

# Sắp xếp từ điển theo giá trị (tần suất) giảm dần
sorted_items = sorted(d.items(), key=lambda item: (-item[1], item[0]))  # Sắp xếp theo value giảm dần, nếu bằng nhau thì sắp xếp theo key tăng dần

# In kết quả
for word, count in sorted_items:
    print(f'{word} {count}')