# https://www.acmicpc.net/problem/7562
# bfs/dfs 실버 1

import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
# 이동 경로
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    dist[x][y] = 0
    while queue:
        x, y = queue.popleft()
        if x == m and y == n:
            print(dist[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not dist[nx][ny]:
                queue.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

for _ in range(t):
    l = int(input())
    dist = [[0] * l for _ in range(l)]
    a, b = map(int, input().rstrip().split())
    m, n = map(int, input().rstrip().split())
    bfs(a, b)
