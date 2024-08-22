# https://www.acmicpc.net/problem/1012
# bfs/dfs 실버 2

import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
# 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, m, n):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and field[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny)) 

for _ in range(t):
    m, n, k = map(int, input().rstrip().split())
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, input().rstrip().split())
        field[j][i] = 1
    visited = [[False] * m for _ in range(n)]
    worm = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and field[i][j] == 1:
                bfs(i, j, m, n)
                worm += 1
    print(worm)
