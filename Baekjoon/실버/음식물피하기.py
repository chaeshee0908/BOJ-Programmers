# 파이썬에서 1000개 이상의 재귀를 기본적으로 제한함으로 제한을 풀어줌
import sys
sys.setrecursionlimit(100000)
# 세로, 가로, 음식물 쓰레기 개수
n, m, k = map(int, input().split())
# 음식물 쓰레기 위치
trash = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    trash[r-1][c-1] = 1
# 위치 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    global count
    if trash[x][y] == 0:
        return
    trash[x][y] = 0
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and trash[nx][ny] == 1:
            dfs(nx, ny)

# 음식물 쓰레기 크기
trash_size = 0

for i in range(n):
    for j in range(m):
        count = 0
        dfs(i, j)
        if trash_size < count:
            trash_size = count 

print(trash_size)           