N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != 0:
                q.append((nx, ny))
                if maze[nx][ny] == 1 and maze[nx][ny] > maze[x][y] + 1:
                    maze[nx][ny] = maze[x][y] + 1

bfs(0, 0)
print(maze[N-1][M-1])