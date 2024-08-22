N, M = map(int, input().split())
# 이동 거리 체크
dist = [[1000] * M for _ in range(N)]
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    dist[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 괴물이 없는 부분일 때
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

bfs(0, 0)
print(dist[N-1][M-1])