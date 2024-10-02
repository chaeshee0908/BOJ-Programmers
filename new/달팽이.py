N = int(input())
number = int(input())
snail = [[0] * N for _ in range(N)]

# 1의 위치 
x, y = N//2, N//2
# 이동 방향(북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
idx = 0

snail[x][y] = 1
now = 2
while now <= N**2:
    nx, ny = x + dx[idx], y + dy[idx]
    # 달팽이 숫자 채우기 
    if 0 <= nx < N and 0 <= ny < N:
        snail[nx][ny] = now
        now += 1
        x, y = nx, ny
    # 방향 정하기 
    next_idx = idx + 1 if idx + 1 < 4 else 0
    next_x, next_y = x + dx[next_idx], y + dy[next_idx]
    # 방향 변경 가능하면 변경
    if snail[next_x][next_y] == 0:
        idx = next_idx

rx, ry = 0, 0
for i in range(N):
    for j in range(N):
        if snail[i][j] == number:
            rx, ry = i+1, j+1
        print(snail[i][j], end=' ')
    print()

print(rx, ry)
    
