n, m = map(int, input().split())
# 미로
maze = []
for _ in range(n):
    maze.append(list(input()))
# 출발위치부터 이동한 칸의 개수
distance = [[1e9] * m for _ in range(n)]
# 이동 방향 : 왼, 오, 위, 아래
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    distance[x][y] = 1
    maze[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and int(maze[nx][ny]) == 1:
                maze[nx][ny] = 0
                if distance[nx][ny] > distance[x][y] + 1:
                    distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

bfs(0, 0)
print(distance[n-1][m-1])