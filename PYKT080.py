M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

# 8 hướng đi (8 directions: lên, xuống, trái, phải và 4 đường chéo)
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

total_risk = 0

for i in range(M):
    for j in range(N):
        if matrix[i][j] == -1:  # Nếu là bệnh nhân
            for di, dj in directions:
                ni, nj = i + di, j + dj  # Tọa độ ô xung quanh
                # Kiểm tra ô xung quanh có hợp lệ và không phải bệnh nhân
                if 0 <= ni < M and 0 <= nj < N and matrix[ni][nj] >= 0:
                    total_risk += matrix[ni][nj]

print(total_risk)