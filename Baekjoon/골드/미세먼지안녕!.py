# 골드4 17144
# https://www.acmicpc.net/problem/17144

R, C, T = map(int, input().split())
room = []
air_cleaner = []
for i in range(R):
    line = list(map(int, input().split()))
    if -1 in line:
        air_cleaner.append(i)
    room.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 미세먼지 확산
def diffusion(x, y):
    count = 0
    move_amount = room[x][y] // 5
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 벽에 안 부딪히고 공기 청정기 아닐 시 확산
        if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
            count += 1
            dust[nx][ny][1] += move_amount  # 확산
    dust[x][y][0] = move_amount * count # 확산되고 줄은 양

# 공기청정기 작동
def air_clean():
    # 반시계 방향 
    for i in range(air_cleaner[0], 0, -1):
        room[i][0], room[i-1][0] = room[i-1][0], room[i][0]
    for i in range(0, C-1):
        room[0][i], room[0][i+1] = room[0][i+1], room[0][i]
    for i in range(0, air_cleaner[0]):
        room[i][C-1], room[i+1][C-1] = room[i+1][C-1], room[i][C-1]
    for i in range(C-1, 0, -1):
        room[air_cleaner[0]][i], room[air_cleaner[0]][i-1] = room[air_cleaner[0]][i-1], room[air_cleaner[0]][i]
    room[air_cleaner[0]][1] = 0     # 깨끗한 바람
    
    # 시계 방향
    for i in range(air_cleaner[1], R-1):
        room[i][0], room[i+1][0] = room[i+1][0], room[i][0]
    for i in range(0, C-1):
        room[R-1][i], room[R-1][i+1] = room[R-1][i+1], room[R-1][i]
    for i in range(R-1, air_cleaner[1], -1):
        room[i][C-1], room[i-1][C-1] =  room[i-1][C-1], room[i][C-1]
    for i in range(C-1, 0, -1):
        room[air_cleaner[1]][i], room[air_cleaner[1]][i-1] = room[air_cleaner[1]][i-1], room[air_cleaner[1]][i]
    room[air_cleaner[1]][1] = 0     # 깨끗한 바람

while T:
    T -= 1
    # 줄어들 먼지 양, 늘어날 먼지 양
    dust = [[[0, 0] for _ in range(C)] for _ in range(R)]
    # 미세먼지 이동 확인
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                diffusion(i, j)
    # 미세먼지 확산 정리
    for i in range(R):
        for j in range(C):
            # 변동사항이 있을 때
            if dust[i][j] != [0, 0]:
                room[i][j] -= dust[i][j][0]
                room[i][j] += dust[i][j][1]
    air_clean()

# 남아있는 미세먼지 양
result = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            result += room[i][j]
print(result)