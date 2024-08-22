# https://www.acmicpc.net/problem/2667
# bfs/dfs 실버 1

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(list(input().rstrip()))
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        board[i][j] = int(board[i][j])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

apart = []

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            apart.append(bfs(i, j))

print(len(apart))
apart.sort()
for i in range(len(apart)):
    print(apart[i])