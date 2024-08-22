# 골드5 2589번
# https://www.acmicpc.net/problem/2589

from collections import deque

n, m = map(int, input().split())
Map = []
land = []
for _ in range(n):
    Map.append(list(input()))

# 땅 위치 저장
for i in range(n):
    for j in range(m):
        if Map[i][j] == 'L':
            land.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
for lx, ly in land:
    distance = [[0] * m for _ in range(n)]
    max_d = 0
    q = deque([(lx, ly)])
    distance[lx][ly] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if Map[nx][ny] == 'L' and distance[nx][ny] == 0:
                distance[nx][ny] += distance[x][y] + 1
                max_d = max(max_d, distance[nx][ny])
                q.append((nx, ny))
    
    result = max(result, max_d-1)
    
    
print(result)