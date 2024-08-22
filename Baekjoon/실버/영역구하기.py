# https://www.acmicpc.net/problem/2583
# bfs/dfs 실버1

import sys
input = sys.stdin.readline
from collections import deque

m, n, k = map(int, input().rstrip().split())
board = [[0] * n for _ in range(m)]
for _ in range(k):
    lx, ly, rx, ry = map(int, input().rstrip().split())
    for i in range(m - ry, m - ly):
        for j in range(lx, rx):
            board[i][j] = -1
# print('--------------------------')
# for i in range(m):
#     print(board[i])
# print('--------------------------')

visited = [[False]*n for _ in range(m)]
# 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

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
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] != -1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1
    return cnt

area_num = 0
area_size = []

for i in range(m):
    for j in range(n):
        if not visited[i][j] and board[i][j] != -1:
            area_size.append(bfs(i, j))
            area_num += 1
area_size.sort()
print(area_num)
print(*area_size)