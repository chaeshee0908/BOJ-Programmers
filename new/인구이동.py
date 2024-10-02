N, L, R = map(int, input().split())
ground = []
for _ in range(N):
    ground.append(list(map(int, input().split())))

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    united = [[(x, y)], ground[x][y], 1] # 연합국 위치, 총 인구수, 총 국가수 
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(ground[x][y] - ground[nx][ny]) <= R:
                visited[nx][ny] = True
                q.append((nx, ny))
                united[0].append((nx, ny))
                united[1] += ground[nx][ny]
                united[2] += 1
    return united

canMove = True
count = 0
while canMove:
    canMove = False
    visited = [[False] * N for _ in range(N)]
    result_set = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result = bfs(i, j)
                if len(result[0]) > 1:
                    canMove = True
                    result_set.append(result)
    if canMove:
        count += 1
        for result in result_set:
            people = result[1] // result[2]
            for r, c in result[0]:
                ground[r][c] = people

print(count)