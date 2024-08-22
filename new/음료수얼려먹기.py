N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = 0

from collections import deque

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    board[x][y] = 2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
            

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            bfs(i, j)
            count += 1

print(count)